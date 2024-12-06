import {
    type ActionExample,
    type HandlerCallback,
    type IAgentRuntime,
    type Memory,
    type State,
    type Action,
    type Content,
    composeContext,
    generateText,
    ModelClass,
  } from "@ai16z/eliza";
  // Use fetch instead of axios to avoid node dependencies
  import { fetch } from 'cross-fetch';

  interface OddsResponse {
    id: string;
    sport_key: string;
    commence_time: string;
    home_team: string;
    away_team: string;
    bookmakers: Array<{
      key: string;
      markets: Array<{
        key: string;
        outcomes: Array<{
          name: string;
          price: number;
          point?: number;
        }>;
      }>;
    }>;
  }

  function getSpreadLine(game: OddsResponse): string {
    const bookmaker = game.bookmakers[0]; // DraftKings
    const spreadMarket = bookmaker?.markets.find(m => m.key === 'spreads');

    if (!spreadMarket) return 'No spread available';

    const homeTeamSpread = spreadMarket.outcomes.find(o => o.name === game.home_team);
    if (!homeTeamSpread?.point) return 'No spread available';

    // If point is positive, it means team is underdog. If negative, team is favorite
    return homeTeamSpread.point > 0
      ? `${game.home_team} +${homeTeamSpread.point}`
      : `${game.home_team} ${homeTeamSpread.point}`;
  }

  async function getUpcomingNFLOdds(teamName: string): Promise<OddsResponse> {
    const API_KEY = process.env.THE_ODDS_API_KEY;
    const SPORT = 'americanfootball_nfl';
    const REGIONS = 'us';
    const MARKETS = 'spreads';
    const ODDS_FORMAT = 'american';
    const DATE_FORMAT = 'iso';
    const BOOKMAKERS = 'draftkings';

    try {
      if (!API_KEY) {
        throw new Error('THE_ODDS_API_KEY environment variable is not set');
      }

      const url = new URL(`https://api.the-odds-api.com/v4/sports/${SPORT}/odds`);
      url.searchParams.append('apiKey', API_KEY);
      url.searchParams.append('regions', REGIONS);
      url.searchParams.append('markets', MARKETS);
      url.searchParams.append('oddsFormat', ODDS_FORMAT);
      url.searchParams.append('dateFormat', DATE_FORMAT);
      url.searchParams.append('bookmakers', BOOKMAKERS);

      const response = await fetch(url.toString());

      if (!response.ok) {
        const errorText = await response.text();
        console.error('API Error Response:', errorText);
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: OddsResponse[] = await response.json();

      // Filter games where the team is either home or away team
      const teamGames = data.filter(game =>
        game.home_team.toLowerCase().includes(teamName.toLowerCase()) ||
        game.away_team.toLowerCase().includes(teamName.toLowerCase())
      );

      if (teamGames.length === 0) {
        throw new Error(`No upcoming games found for ${teamName}`);
      }

      // Sort by commence_time and return the earliest game
      const nextGame = teamGames.sort((a, b) =>
        new Date(a.commence_time).getTime() - new Date(b.commence_time).getTime()
      )[0];

      return nextGame;
    } catch (error) {
      console.error('Error fetching NFL odds:', error);
      throw error;
    }
  }

  function formatDateTime(dateString: string): string {
    const date = new Date(dateString);
    const options: Intl.DateTimeFormatOptions = {
      month: 'numeric',
      day: 'numeric',
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  }

  export const spreadAction: Action = {
    name: "SPREAD",
    similes: ["LINE", "ODDS"],

    validate: async (_runtime: IAgentRuntime, _message: Memory) => {
      return true;
    },

    description: "Respond with the upcoming spread odds of NFL games given a team name",

    handler: async (
      _runtime: IAgentRuntime,
      _message: Memory,
      _state: State,
      _options: { [key: string]: unknown},
      _callback: HandlerCallback,
    ): Promise<boolean> => {


        const context = `
        Extract the NFL team from the user's message. The message is: ${_message.content.text}
        Only respond with the NFL team, do not include any other text.
        Format the NFL team name so that it is the full team name. For example, the Jets should be "New York Jets".
        `

        const response = await generateText({
            runtime: _runtime,
            context,
            modelClass: ModelClass.SMALL,
            stop: ["/n"]
        })

        // const context = await composeContext({
        //     state: _state,
        //     template
        // });


        const spread = await getUpcomingNFLOdds(response);
        const spreadLine = getSpreadLine(spread);
        const formattedText = `${spread.away_team} @ ${spread.home_team} (${spreadLine}) - ${formatDateTime(spread.commence_time)}`;

        const newMemory: Memory = {
            userId: _message.agentId,
            agentId: _message.agentId,
            roomId: _message.roomId,
            content: {
                text: formattedText,
                action: "SPREAD_RESPONSE",
                source: _message.content?.source
                } as Content,
            };

        await _runtime.messageManager.createMemory(newMemory);

        _callback({
            text: formattedText || `No upcoming games found for ${response}`
          });
        return true;
    },
    examples: [
        [
          {
            user: "{{user1}}",
            content: { text: "What's the spread for the Lions game?" },
          },
          {
            user: "{{user2}}",
            content: {
                text: "Detroit Lions @ Green Bay Packers (Lions -3) - 1/1, 1:00 PM",
                action: "SPREAD"
            },
          },
        ],
        [
          {
            user: "{{user1}}",
            content: { text: "What's the spread for Cowboys Eagles?" },
          },
          {
            user: "{{user2}}",
            content: {
                text: "Philadelphia Eagles @ Dallas Cowboys (Cowboys -4.5) - 1/1, 4:25 PM",
                action: "SPREAD"
            },
          },
        ],
        [
          {
            user: "{{user1}}",
            content: { text: "What's the spread for the Bills?" },
          },
          {
            user: "{{user2}}",
            content: {
                text: "Buffalo Bills @ Miami Dolphins (Dolphins -2.5) - 1/1, 1:00 PM",
                action: "SPREAD"
            },
          },
        ],
        [
          {
            user: "{{user1}}",
            content: { text: "Give me the spread for the Ravens game" },
          },
          {
            user: "{{user2}}",
            content: {
                text: "Pittsburgh Steelers @ Baltimore Ravens (Ravens -3) - 1/1, 1:00 PM",
                action: "SPREAD"
            },
          },
    ]
] as ActionExample[][],
} as Action;
