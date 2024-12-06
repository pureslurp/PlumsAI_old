import { Plugin } from "@ai16z/eliza";
// import { spreadAction } from "./actions/odds.ts";
import { oddsProvider } from "./providers/odds.ts";

export const nflPlugin: Plugin = {
    name: "nfl",
    description: "Agent NFL database and tools",
    actions: [],
    providers : [oddsProvider]
};