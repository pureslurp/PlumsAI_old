# Interface: State

Represents the state of the conversation or context in which the agent is operating, including information about users, messages, goals, and other relevant data.

## Indexable

 \[`key`: `string`\]: `unknown`

## Properties

### actionExamples?

> `optional` **actionExamples**: `string`

#### Defined in

[core/src/core/types.ts:139](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L139)

***

### actionNames?

> `optional` **actionNames**: `string`

#### Defined in

[core/src/core/types.ts:136](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L136)

***

### actions?

> `optional` **actions**: `string`

#### Defined in

[core/src/core/types.ts:137](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L137)

***

### actionsData?

> `optional` **actionsData**: [`Action`](Action.md)[]

#### Defined in

[core/src/core/types.ts:138](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L138)

***

### actors

> **actors**: `string`

#### Defined in

[core/src/core/types.ts:126](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L126)

***

### actorsData?

> `optional` **actorsData**: [`Actor`](Actor.md)[]

#### Defined in

[core/src/core/types.ts:127](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L127)

***

### agentId?

> `optional` **agentId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

#### Defined in

[core/src/core/types.ts:118](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L118)

***

### agentName?

> `optional` **agentName**: `string`

#### Defined in

[core/src/core/types.ts:124](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L124)

***

### bio

> **bio**: `string`

#### Defined in

[core/src/core/types.ts:119](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L119)

***

### goals?

> `optional` **goals**: `string`

#### Defined in

[core/src/core/types.ts:128](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L128)

***

### goalsData?

> `optional` **goalsData**: [`Goal`](Goal.md)[]

#### Defined in

[core/src/core/types.ts:129](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L129)

***

### lore

> **lore**: `string`

#### Defined in

[core/src/core/types.ts:120](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L120)

***

### messageDirections

> **messageDirections**: `string`

#### Defined in

[core/src/core/types.ts:121](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L121)

***

### postDirections

> **postDirections**: `string`

#### Defined in

[core/src/core/types.ts:122](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L122)

***

### providers?

> `optional` **providers**: `string`

#### Defined in

[core/src/core/types.ts:140](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L140)

***

### recentFacts?

> `optional` **recentFacts**: `string`

#### Defined in

[core/src/core/types.ts:132](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L132)

***

### recentFactsData?

> `optional` **recentFactsData**: [`Memory`](Memory.md)[]

#### Defined in

[core/src/core/types.ts:133](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L133)

***

### recentInteractions?

> `optional` **recentInteractions**: `string`

#### Defined in

[core/src/core/types.ts:143](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L143)

***

### recentInteractionsData?

> `optional` **recentInteractionsData**: [`Memory`](Memory.md)[]

#### Defined in

[core/src/core/types.ts:142](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L142)

***

### recentMessages

> **recentMessages**: `string`

#### Defined in

[core/src/core/types.ts:130](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L130)

***

### recentMessagesData

> **recentMessagesData**: [`Memory`](Memory.md)[]

#### Defined in

[core/src/core/types.ts:131](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L131)

***

### relevantFacts?

> `optional` **relevantFacts**: `string`

#### Defined in

[core/src/core/types.ts:134](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L134)

***

### relevantFactsData?

> `optional` **relevantFactsData**: [`Memory`](Memory.md)[]

#### Defined in

[core/src/core/types.ts:135](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L135)

***

### responseData?

> `optional` **responseData**: [`Content`](Content.md)

#### Defined in

[core/src/core/types.ts:141](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L141)

***

### roomId

> **roomId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

#### Defined in

[core/src/core/types.ts:123](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L123)

***

### senderName?

> `optional` **senderName**: `string`

#### Defined in

[core/src/core/types.ts:125](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L125)

***

### userId?

> `optional` **userId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

#### Defined in

[core/src/core/types.ts:117](https://github.com/ai16z/eliza/blob/c537cb3e848b54fcb914d8ef84924fa5fdeaec66/core/src/core/types.ts#L117)