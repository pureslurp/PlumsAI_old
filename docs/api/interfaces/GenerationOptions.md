[@ai16z/eliza v0.1.5-alpha.1](../index.md) / GenerationOptions

# Interface: GenerationOptions

Configuration options for generating objects with a model.

## Properties

### runtime

> **runtime**: [`IAgentRuntime`](IAgentRuntime.md)

#### Defined in

packages/core/src/generation.ts:1044

***

### context

> **context**: `string`

#### Defined in

packages/core/src/generation.ts:1045

***

### modelClass

> **modelClass**: [`ModelClass`](../enumerations/ModelClass.md)

#### Defined in

packages/core/src/generation.ts:1046

***

### schema?

> `optional` **schema**: `ZodType`\<`any`, `ZodTypeDef`, `any`\>

#### Defined in

packages/core/src/generation.ts:1047

***

### schemaName?

> `optional` **schemaName**: `string`

#### Defined in

packages/core/src/generation.ts:1048

***

### schemaDescription?

> `optional` **schemaDescription**: `string`

#### Defined in

packages/core/src/generation.ts:1049

***

### stop?

> `optional` **stop**: `string`[]

#### Defined in

packages/core/src/generation.ts:1050

***

### mode?

> `optional` **mode**: `"auto"` \| `"json"` \| `"tool"`

#### Defined in

packages/core/src/generation.ts:1051

***

### experimental\_providerMetadata?

> `optional` **experimental\_providerMetadata**: `Record`\<`string`, `unknown`\>

#### Defined in

packages/core/src/generation.ts:1052
