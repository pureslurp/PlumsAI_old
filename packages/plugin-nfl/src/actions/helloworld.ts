import {
    ActionExample,
    HandlerCallback,
    IAgentRuntime,
    Memory,
    State,
    type Action,
} from "@ai16z/eliza";


export const helloworldAction: Action = {
    name: "HELLO_WORLD",
    similes: [
    ],
    validate: async (_runtime: IAgentRuntime, _message: Memory) => {
        return true;
    },
    description:
        "Respond with HELLO_WORLD",
    handler: async (
        _runtime: IAgentRuntime,
        _message: Memory,
        _state: State,
        _options: { [key: string]: unknown},
        _callback: HandlerCallback,
    ): Promise<boolean> => {

        _callback({
            text: "HELLO_WORLD"
        })
        return true;
    },
    examples: [
        [
            {
                user: "{{user1}}",
                content: { text: "Say hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Can you give me a hello world?" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Hello world please" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "I want to see hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Show me hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Print hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Output hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],

        [
            {
                user: "{{user1}}",
                content: { text: "Run hello world" },
            },
            {
                user: "{{user2}}",
                content: { text: "HELLO_WORLD", action: "HELLO_WORLD" },
            },
        ],
    ] as ActionExample[][],
} as Action;
