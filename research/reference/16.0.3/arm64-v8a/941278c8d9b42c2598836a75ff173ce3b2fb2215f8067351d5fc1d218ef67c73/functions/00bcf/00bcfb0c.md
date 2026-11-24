# 00bcfb0c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bceb18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb18.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-35336e358553cf5e79c1b4cdebc15107)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfb0c",
  "name": "_ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2efcc22eaa55b65068fa05d6f49da405266be4e6646afc5dcb4b8653b2f631",
  "source_text_sha256": "ed2efcc22eaa55b65068fa05d6f49da405266be4e6646afc5dcb4b8653b2f631",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfb0c",
        "00bcfb7b"
      ]
    ],
    "bytes_sha256": "d8130cf4a240c42f220c5dced4c60a80b3ed6a44e18842c324d7e78610dca77e",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5bc30](../00c5b/00c5bc30.md)

## 呼び出し先

- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)

## 関連文字列（未確認候補）

~~~text
"provider"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 645 bytes

~~~c

void _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE
               (long param_1,undefined8 *param_2,long *param_3)

{
  if (param_3 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bcfb40. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_3 + 0x10))(param_1,param_3,*param_2);
    return;
  }
  _ZN8firebase9LogAssertEPKcz("provider");
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfb0c"></a> `00bcfb0c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcfb10"></a> `00bcfb10` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb14"></a> `00bcfb14` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfb18"></a> `00bcfb18` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcfb1c"></a> `00bcfb1c` | `41 01 00 b4` | cbz x1,0x00bcfb44 | `CONDITIONAL_JUMP`
<a id="insn-00bcfb20"></a> `00bcfb20` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcfb24"></a> `00bcfb24` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcfb28"></a> `00bcfb28` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb2c"></a> `00bcfb2c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bcfb30"></a> `00bcfb30` | `02 09 40 f9` | ldr x2,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb34"></a> `00bcfb34` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bcfb38"></a> `00bcfb38` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-00bcfb3c"></a> `00bcfb3c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcfb40"></a> `00bcfb40` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`
<a id="insn-00bcfb44"></a> `00bcfb44` | `20 b7 ff d0` | adrp x0,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcfb48"></a> `00bcfb48` | `00 44 33 91` | add x0,x0,#0xcd1 | `FALL_THROUGH`
<a id="insn-00bcfb4c"></a> `00bcfb4c` | `55 31 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb50"></a> `00bcfb50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfb54"></a> `00bcfb54` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bcfb58"></a> `00bcfb58` | `6e 30 02 94` | bl 0x00c5bd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb5c"></a> `00bcfb5c` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcfb60"></a> `00bcfb60` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfb64"></a> `00bcfb64` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bcfb68"></a> `00bcfb68` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcfb6c"></a> `00bcfb6c` | `45 30 02 94` | bl 0x00c5bc80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfb70"></a> `00bcfb70` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfb74"></a> `00bcfb74` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcfb78"></a> `00bcfb78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfb0c`](#insn-00bcfb0c) 範囲 `[['00bcfb0c', '00bcfb1f']]`
  - `CONDITIONAL_JUMP` [`00bcfb1c`](#insn-00bcfb1c) → [`00bcfb44`](#insn-00bcfb44)
  - `FALL_THROUGH` [`00bcfb1c`](#insn-00bcfb1c) → [`00bcfb20`](#insn-00bcfb20)
- ブロック [`00bcfb20`](#insn-00bcfb20) 範囲 `[['00bcfb20', '00bcfb43']]`
- ブロック [`00bcfb44`](#insn-00bcfb44) 範囲 `[['00bcfb44', '00bcfb7b']]`

## 命令位置別の参照

- [`00bcfb0c`](#insn-00bcfb0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb10`](#insn-00bcfb10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb1c`](#insn-00bcfb1c) → [`00bcfb44`](#insn-00bcfb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb28`](#insn-00bcfb28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb48`](#insn-00bcfb48) → `002b5cd1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcfb4c`](#insn-00bcfb4c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb58`](#insn-00bcfb58) → [`00c5bd10`](../00c5b/00c5bd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd10` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb6c`](#insn-00bcfb6c) → [`00c5bc80`](../00c5b/00c5bc80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc80` · 推定シンボル `None` · 推定型 `None`
- [`00bcfb70`](#insn-00bcfb70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfb0c`](#insn-00bcfb0c)

~~~json
{
  "source": "00bcfb0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb10`](#insn-00bcfb10)

~~~json
{
  "source": "00bcfb10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb1c`](#insn-00bcfb1c)

~~~json
{
  "source": "00bcfb1c",
  "target": "00bcfb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb28`](#insn-00bcfb28)

~~~json
{
  "source": "00bcfb28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfb48`](#insn-00bcfb48)

~~~json
{
  "source": "00bcfb48",
  "target": "002b5cd1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5cd1",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "70726f766964657200",
  "capture_start": "002b5cd1",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcfb4c`](#insn-00bcfb4c)

~~~json
{
  "source": "00bcfb4c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb58`](#insn-00bcfb58)

~~~json
{
  "source": "00bcfb58",
  "target": "00c5bd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb6c`](#insn-00bcfb6c)

~~~json
{
  "source": "00bcfb6c",
  "target": "00c5bc80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfb70`](#insn-00bcfb70)

~~~json
{
  "source": "00bcfb70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
