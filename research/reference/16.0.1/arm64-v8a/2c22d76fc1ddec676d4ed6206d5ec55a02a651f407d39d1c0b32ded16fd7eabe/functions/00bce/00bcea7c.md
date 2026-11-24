# 00bcea7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bce654`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-f9f940aca01c9481fe6c1535ce994521)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bceb18`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bceb18.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-a50187fd24ed6ce83e55c78ccd5ec271)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcea7c",
  "name": "_ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2a959116734c5c8062ac470d0a15a4d27ef1397816705e8e27fc624e46093947",
  "source_text_sha256": "2a959116734c5c8062ac470d0a15a4d27ef1397816705e8e27fc624e46093947",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcea7c",
        "00bceaeb"
      ]
    ],
    "bytes_sha256": "d5853797cff8e9bd26f6387b1a62fbdde46b5c397b39c6fb8539450356260420",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5ab90](../00c5a/00c5ab90.md)

## 呼び出し先

- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"provider"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 732 bytes

~~~c

void _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE
               (long param_1,undefined8 *param_2,long *param_3)

{
                    /* catch() { ... } // from try @ 00bcdb58 with catch @ 00bcea88 */
  if (param_3 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x00bceab0. Too many branches */
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
<a id="insn-00bcea7c"></a> `00bcea7c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcea80"></a> `00bcea80` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcea84"></a> `00bcea84` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcea88"></a> `00bcea88` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcea8c"></a> `00bcea8c` | `41 01 00 b4` | cbz x1,0x00bceab4 | `CONDITIONAL_JUMP`
<a id="insn-00bcea90"></a> `00bcea90` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcea94"></a> `00bcea94` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcea98"></a> `00bcea98` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcea9c"></a> `00bcea9c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bceaa0"></a> `00bceaa0` | `02 09 40 f9` | ldr x2,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bceaa4"></a> `00bceaa4` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bceaa8"></a> `00bceaa8` | `e1 03 09 aa` | mov x1,x9 | `FALL_THROUGH`
<a id="insn-00bceaac"></a> `00bceaac` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bceab0"></a> `00bceab0` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`
<a id="insn-00bceab4"></a> `00bceab4` | `20 b7 ff f0` | adrp x0,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bceab8"></a> `00bceab8` | `00 08 2f 91` | add x0,x0,#0xbc2 | `FALL_THROUGH`
<a id="insn-00bceabc"></a> `00bceabc` | `51 31 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bceac0"></a> `00bceac0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bceac4"></a> `00bceac4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bceac8"></a> `00bceac8` | `6a 30 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bceacc"></a> `00bceacc` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00bcead0"></a> `00bcead0` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bcead4"></a> `00bcead4` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bcead8"></a> `00bcead8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bceadc"></a> `00bceadc` | `41 30 02 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceae0"></a> `00bceae0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bceae4"></a> `00bceae4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bceae8"></a> `00bceae8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcea7c`](#insn-00bcea7c) 範囲 `[['00bcea7c', '00bcea87']]`
  - `FALL_THROUGH` [`00bcea84`](#insn-00bcea84) → [`00bcea88`](#insn-00bcea88)
- ブロック [`00bcea88`](#insn-00bcea88) 範囲 `[['00bcea88', '00bcea8f']]`
  - `CONDITIONAL_JUMP` [`00bcea8c`](#insn-00bcea8c) → [`00bceab4`](#insn-00bceab4)
  - `FALL_THROUGH` [`00bcea8c`](#insn-00bcea8c) → [`00bcea90`](#insn-00bcea90)
- ブロック [`00bcea90`](#insn-00bcea90) 範囲 `[['00bcea90', '00bceab3']]`
- ブロック [`00bceab4`](#insn-00bceab4) 範囲 `[['00bceab4', '00bceaeb']]`

## 命令位置別の参照

- [`00bcea7c`](#insn-00bcea7c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcea80`](#insn-00bcea80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcea8c`](#insn-00bcea8c) → [`00bceab4`](#insn-00bceab4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcea98`](#insn-00bcea98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceab8`](#insn-00bceab8) → `002b5bc2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bceabc`](#insn-00bceabc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bceac8`](#insn-00bceac8) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bceadc`](#insn-00bceadc) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00bceae0`](#insn-00bceae0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcea7c`](#insn-00bcea7c)

~~~json
{
  "source": "00bcea7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcea80`](#insn-00bcea80)

~~~json
{
  "source": "00bcea80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcea8c`](#insn-00bcea8c)

~~~json
{
  "source": "00bcea8c",
  "target": "00bceab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcea98`](#insn-00bcea98)

~~~json
{
  "source": "00bcea98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceab8`](#insn-00bceab8)

~~~json
{
  "source": "00bceab8",
  "target": "002b5bc2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5bc2",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "70726f766964657200",
  "capture_start": "002b5bc2",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bceabc`](#insn-00bceabc)

~~~json
{
  "source": "00bceabc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceac8`](#insn-00bceac8)

~~~json
{
  "source": "00bceac8",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceadc`](#insn-00bceadc)

~~~json
{
  "source": "00bceadc",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceae0`](#insn-00bceae0)

~~~json
{
  "source": "00bceae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
