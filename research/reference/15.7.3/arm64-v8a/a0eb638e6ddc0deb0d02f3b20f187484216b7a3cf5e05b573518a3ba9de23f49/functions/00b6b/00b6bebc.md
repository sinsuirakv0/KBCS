# 00b6bebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6bdf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bdf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0004.md#compare-6bc3b12a0327b294d09be5b285790fab)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6bf00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6b/00b6bf00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0012.md#compare-bde8920fc76d620988e85daaaae819f0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6bebc",
  "name": "_ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d9fdde45e04b4bf48cf951156c2f3cdd1d440252067e6358602b5ac538a9cb8a",
  "source_text_sha256": "d9fdde45e04b4bf48cf951156c2f3cdd1d440252067e6358602b5ac538a9cb8a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6bebc",
        "00b6bf27"
      ]
    ],
    "bytes_sha256": "8389555afbaf7cf222381e3f0f1f022dd795f1b9fe443046e40bc6068a44bbf8",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005188a4](../00518/005188a4.md)
- [00bde1e0](../00bde/00bde1e0.md)
- [00be0040](../00be0/00be0040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1184 bytes

~~~c

void _ZN8firebase4auth22FederatedOAuthProvider15SetProviderDataERKNS0_26FederatedOAuthProviderDataE
               (long param_1,byte *param_2)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)(param_1 + 8) != param_2) {
    uVar1 = *(ulong *)(param_2 + 8);
    pbVar2 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00b6beec to 00c6beef has its CatchHandler @ 00b6c074 */
    if ((*param_2 & 1) == 0) {
      pbVar2 = param_2 + 1;
      uVar1 = (ulong)(*param_2 >> 1);
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              ((byte *)(param_1 + 8),pbVar2,uVar1);
    _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE6assignIPS6_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS6_NS_15iterator_traitsISC_E9referenceEEE5valueEvE4typeESC_SC_
              (param_1 + 0x20,*(undefined8 *)(param_2 + 0x18),*(undefined8 *)(param_2 + 0x20));
                    /* try { // try from 00b6bf18 to 00c6bf3b has its CatchHandler @ 00b6c01c */
    FUN_005188a4(param_1 + 0x38,*(undefined8 *)(param_2 + 0x30),param_2 + 0x38);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6bebc"></a> `00b6bebc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6bec0"></a> `00b6bec0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6bec4"></a> `00b6bec4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6bec8"></a> `00b6bec8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6becc"></a> `00b6becc` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b6bed0"></a> `00b6bed0` | `1f 00 01 eb` | cmp x0,x1 | `FALL_THROUGH`
<a id="insn-00b6bed4"></a> `00b6bed4` | `40 02 00 54` | b.eq 0x00b6bf1c | `CONDITIONAL_JUMP`
<a id="insn-00b6bed8"></a> `00b6bed8` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00b6bedc"></a> `00b6bedc` | `2a a4 40 a9` | ldp x10,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b6bee0"></a> `00b6bee0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b6bee4"></a> `00b6bee4` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6bee8"></a> `00b6bee8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6beec"></a> `00b6beec` | `21 15 81 9a` | csinc x1,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00b6bef0"></a> `00b6bef0` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b6bef4"></a> `00b6bef4` | `bb c8 01 94` | bl 0x00bde1e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6bef8"></a> `00b6bef8` | `61 8a 41 a9` | ldp x1,x2,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6befc"></a> `00b6befc` | `80 82 00 91` | add x0,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00b6bf00"></a> `00b6bf00` | `50 d0 01 94` | bl 0x00be0040 | `UNCONDITIONAL_CALL`
<a id="insn-00b6bf04"></a> `00b6bf04` | `61 1a 40 f9` | ldr x1,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b6bf08"></a> `00b6bf08` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6bf0c"></a> `00b6bf0c` | `80 e2 00 91` | add x0,x20,#0x38 | `FALL_THROUGH`
<a id="insn-00b6bf10"></a> `00b6bf10` | `62 e2 00 91` | add x2,x19,#0x38 | `FALL_THROUGH`
<a id="insn-00b6bf14"></a> `00b6bf14` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6bf18"></a> `00b6bf18` | `63 b2 e6 17` | b 0x005188a4 | `CALL_TERMINATOR`
<a id="insn-00b6bf1c"></a> `00b6bf1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6bf20"></a> `00b6bf20` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6bf24"></a> `00b6bf24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6bebc`](#insn-00b6bebc) 範囲 `[['00b6bebc', '00b6bed7']]`
  - `CONDITIONAL_JUMP` [`00b6bed4`](#insn-00b6bed4) → [`00b6bf1c`](#insn-00b6bf1c)
  - `FALL_THROUGH` [`00b6bed4`](#insn-00b6bed4) → [`00b6bed8`](#insn-00b6bed8)
- ブロック [`00b6bed8`](#insn-00b6bed8) 範囲 `[['00b6bed8', '00b6beeb']]`
  - `FALL_THROUGH` [`00b6bee8`](#insn-00b6bee8) → [`00b6beec`](#insn-00b6beec)
- ブロック [`00b6beec`](#insn-00b6beec) 範囲 `[['00b6beec', '00b6bf17']]`
  - `FALL_THROUGH` [`00b6bf14`](#insn-00b6bf14) → [`00b6bf18`](#insn-00b6bf18)
- ブロック [`00b6bf18`](#insn-00b6bf18) 範囲 `[['00b6bf18', '00b6bf1b']]`
- ブロック [`00b6bf1c`](#insn-00b6bf1c) 範囲 `[['00b6bf1c', '00b6bf27']]`

## 命令位置別の参照

- [`00b6bebc`](#insn-00b6bebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bec0`](#insn-00b6bec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bed4`](#insn-00b6bed4) → [`00b6bf1c`](#insn-00b6bf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bef4`](#insn-00b6bef4) → [`00bde1e0`](../00bde/00bde1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6bf00`](#insn-00b6bf00) → [`00be0040`](../00be0/00be0040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0040` · 推定シンボル `None` · 推定型 `None`
- [`00b6bf08`](#insn-00b6bf08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6bf18`](#insn-00b6bf18) → [`005188a4`](../00518/005188a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005188a4` · 推定シンボル `None` · 推定型 `None`
- [`00b6bf1c`](#insn-00b6bf1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6bebc`](#insn-00b6bebc)

~~~json
{
  "source": "00b6bebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bec0`](#insn-00b6bec0)

~~~json
{
  "source": "00b6bec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bed4`](#insn-00b6bed4)

~~~json
{
  "source": "00b6bed4",
  "target": "00b6bf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bef4`](#insn-00b6bef4)

~~~json
{
  "source": "00b6bef4",
  "target": "00bde1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6bf00`](#insn-00b6bf00)

~~~json
{
  "source": "00b6bf00",
  "target": "00be0040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6bf08`](#insn-00b6bf08)

~~~json
{
  "source": "00b6bf08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6bf18`](#insn-00b6bf18)

~~~json
{
  "source": "00b6bf18",
  "target": "005188a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6bf1c`](#insn-00b6bf1c)

~~~json
{
  "source": "00b6bf1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
