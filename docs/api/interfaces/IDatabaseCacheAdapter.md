[@ai16z/eliza v0.1.5-alpha.1](../index.md) / IDatabaseCacheAdapter

# Interface: IDatabaseCacheAdapter

## Methods

### getCache()

> **getCache**(`params`): `Promise`\<`string`\>

#### Parameters

• **params**

• **params.agentId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

• **params.key**: `string`

#### Returns

`Promise`\<`string`\>

#### Defined in

packages/core/src/types.ts:890

***

### setCache()

> **setCache**(`params`): `Promise`\<`boolean`\>

#### Parameters

• **params**

• **params.agentId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

• **params.key**: `string`

• **params.value**: `string`

#### Returns

`Promise`\<`boolean`\>

#### Defined in

packages/core/src/types.ts:895

***

### deleteCache()

> **deleteCache**(`params`): `Promise`\<`boolean`\>

#### Parameters

• **params**

• **params.agentId**: \`$\{string\}-$\{string\}-$\{string\}-$\{string\}-$\{string\}\`

• **params.key**: `string`

#### Returns

`Promise`\<`boolean`\>

#### Defined in

packages/core/src/types.ts:901
