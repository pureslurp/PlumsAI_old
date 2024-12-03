[@ai16z/eliza v0.1.4-alpha.3](../index.md) / GenerationOptions

# Interface: GenerationOptions

Configuration options for generating objects with a model.

## Properties

### runtime

> **runtime**: [`IAgentRuntime`](IAgentRuntime.md)

#### Defined in

packages/core/src/generation.ts:1132

***

### context

> **context**: `string`

#### Defined in

packages/core/src/generation.ts:1133

***

### modelClass

> **modelClass**: [`ModelClass`](../enumerations/ModelClass.md)

#### Defined in

packages/core/src/generation.ts:1134

***

### schema?

> `optional` **schema**: `ZodType`\<`any`, `ZodTypeDef`, `any`\>

#### Defined in

packages/core/src/generation.ts:1135

***

### schemaName?

> `optional` **schemaName**: `string`

#### Defined in

packages/core/src/generation.ts:1136

***

### schemaDescription?

> `optional` **schemaDescription**: `string`

#### Defined in

packages/core/src/generation.ts:1137

***

### stop?

> `optional` **stop**: `string`[]

#### Defined in

packages/core/src/generation.ts:1138

***

### mode?

> `optional` **mode**: `"auto"` \| `"json"` \| `"tool"`

#### Defined in

packages/core/src/generation.ts:1139

***

### experimental\_providerMetadata?

> `optional` **experimental\_providerMetadata**: `Record`\<`string`, `unknown`\>

#### Defined in

packages/core/src/generation.ts:1140
