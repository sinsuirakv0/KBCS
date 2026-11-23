# 00aecd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecde4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-fecec2368226fac118abdebf88274e8a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecd1c",
  "name": "_ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0554a05f96dc9ecd50eee59ceff7c09d54aec73eeecf21b2e06062f3c7622c6a",
  "source_text_sha256": "0554a05f96dc9ecd50eee59ceff7c09d54aec73eeecf21b2e06062f3c7622c6a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecd1c",
        "00aecd5f"
      ]
    ],
    "bytes_sha256": "9997dd00ed32f7dc6257f79918fe830f0d7e45498a02d5346738d3eee302bc17",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 557 bytes

~~~c

long _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
                    /* try { // try from 00aecd28 to 00bedab3 has its CatchHandler @ 00aeadc8 */
  if (DAT_010a08c8 == 0) {
    DAT_010a08c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",param_3);
  }
  return DAT_010a08c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecd1c"></a> `00aecd1c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecd20"></a> `00aecd20` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd24"></a> `00aecd24` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aecd28"></a> `00aecd28` | `b3 2d 00 90` | adrp x19,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecd2c"></a> `00aecd2c` | `68 66 44 f9` | ldr x8,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecd30"></a> `00aecd30` | `08 01 00 b5` | cbnz x8,0x00aecd50 | `CONDITIONAL_JUMP`
<a id="insn-00aecd34"></a> `00aecd34` | `83 bd ff f0` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00aecd38"></a> `00aecd38` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00aecd3c"></a> `00aecd3c` | `63 c8 3c 91` | add x3,x3,#0xf32 | `FALL_THROUGH`
<a id="insn-00aecd40"></a> `00aecd40` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aecd44"></a> `00aecd44` | `93 c4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aecd48"></a> `00aecd48` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aecd4c"></a> `00aecd4c` | `60 66 04 f9` | str x0,[x19, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecd50"></a> `00aecd50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecd54"></a> `00aecd54` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00aecd58"></a> `00aecd58` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aecd5c"></a> `00aecd5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecd1c`](#insn-00aecd1c) 範囲 `[['00aecd1c', '00aecd27']]`
  - `FALL_THROUGH` [`00aecd24`](#insn-00aecd24) → [`00aecd28`](#insn-00aecd28)
- ブロック [`00aecd28`](#insn-00aecd28) 範囲 `[['00aecd28', '00aecd33']]`
  - `CONDITIONAL_JUMP` [`00aecd30`](#insn-00aecd30) → [`00aecd50`](#insn-00aecd50)
  - `FALL_THROUGH` [`00aecd30`](#insn-00aecd30) → [`00aecd34`](#insn-00aecd34)
- ブロック [`00aecd34`](#insn-00aecd34) 範囲 `[['00aecd34', '00aecd4f']]`
  - `FALL_THROUGH` [`00aecd4c`](#insn-00aecd4c) → [`00aecd50`](#insn-00aecd50)
- ブロック [`00aecd50`](#insn-00aecd50) 範囲 `[['00aecd50', '00aecd5f']]`

## 命令位置別の参照

- [`00aecd1c`](#insn-00aecd1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd20`](#insn-00aecd20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd2c`](#insn-00aecd2c) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecd30`](#insn-00aecd30) → [`00aecd50`](#insn-00aecd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecd3c`](#insn-00aecd3c) → `0029ff32`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aecd44`](#insn-00aecd44) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aecd4c`](#insn-00aecd4c) → `010a08c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecd50`](#insn-00aecd50) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecd1c`](#insn-00aecd1c)

~~~json
{
  "source": "00aecd1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd20`](#insn-00aecd20)

~~~json
{
  "source": "00aecd20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd2c`](#insn-00aecd2c)

~~~json
{
  "source": "00aecd2c",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecd30`](#insn-00aecd30)

~~~json
{
  "source": "00aecd30",
  "target": "00aecd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecd3c`](#insn-00aecd3c)

~~~json
{
  "source": "00aecd3c",
  "target": "0029ff32",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029ff32",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "0029ff32",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aecd44`](#insn-00aecd44)

~~~json
{
  "source": "00aecd44",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aecd4c`](#insn-00aecd4c)

~~~json
{
  "source": "00aecd4c",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecd50`](#insn-00aecd50)

~~~json
{
  "source": "00aecd50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
