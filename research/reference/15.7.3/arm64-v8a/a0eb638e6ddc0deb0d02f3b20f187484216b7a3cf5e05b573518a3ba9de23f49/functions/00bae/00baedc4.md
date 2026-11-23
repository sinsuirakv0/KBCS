# 00baedc4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baecfc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baecfc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-d9b5193dc229d47e684e6753ea7810e5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baee08`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-a4542958aa72bca5627f27a847ad51e4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baedc4",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c40a8757b5ea11543cf697482040ab344830964da19c77c63874c961f33ce110",
  "source_text_sha256": "c40a8757b5ea11543cf697482040ab344830964da19c77c63874c961f33ce110",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baedc4",
        "00baee33"
      ]
    ],
    "bytes_sha256": "f57f9806b4dc0196ad4c4fe2fe925fa45b67d8983ef3c7353b7ef0b6da4ba962",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bae6f8](../00bae/00bae6f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 922 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* catch() { ... } // from try @ 00baed28 with catch @ 00baede0 */
                    /* catch() { ... } // from try @ 00baed1c with catch @ 00baedf8 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* catch() { ... } // from try @ 00baecf0 with catch @ 00baee10 */
  FUN_00bae6f8(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
                    /* catch() { ... } // from try @ 00baecc4 with catch @ 00baee20 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baedc4"></a> `00baedc4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baedc8"></a> `00baedc8` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baedcc"></a> `00baedcc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baedd0"></a> `00baedd0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baedd4"></a> `00baedd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baedd8"></a> `00baedd8` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baeddc"></a> `00baeddc` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baede0"></a> `00baede0` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baede4"></a> `00baede4` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baede8"></a> `00baede8` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baedec"></a> `00baedec` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baedf0"></a> `00baedf0` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baedf4"></a> `00baedf4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baedf8"></a> `00baedf8` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baedfc"></a> `00baedfc` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baee00"></a> `00baee00` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baee04"></a> `00baee04` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baee08"></a> `00baee08` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baee0c"></a> `00baee0c` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baee10"></a> `00baee10` | `3a fe ff 97` | bl 0x00bae6f8 | `UNCONDITIONAL_CALL`
<a id="insn-00baee14"></a> `00baee14` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baee18"></a> `00baee18` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baee1c"></a> `00baee1c` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baee20"></a> `00baee20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baee24"></a> `00baee24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baee28"></a> `00baee28` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baee2c"></a> `00baee2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baee30"></a> `00baee30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baedc4`](#insn-00baedc4) 範囲 `[['00baedc4', '00baeddf']]`
  - `FALL_THROUGH` [`00baeddc`](#insn-00baeddc) → [`00baede0`](#insn-00baede0)
- ブロック [`00baede0`](#insn-00baede0) 範囲 `[['00baede0', '00baedf7']]`
  - `FALL_THROUGH` [`00baedf4`](#insn-00baedf4) → [`00baedf8`](#insn-00baedf8)
- ブロック [`00baedf8`](#insn-00baedf8) 範囲 `[['00baedf8', '00baee0f']]`
  - `FALL_THROUGH` [`00baee0c`](#insn-00baee0c) → [`00baee10`](#insn-00baee10)
- ブロック [`00baee10`](#insn-00baee10) 範囲 `[['00baee10', '00baee1f']]`
  - `FALL_THROUGH` [`00baee1c`](#insn-00baee1c) → [`00baee20`](#insn-00baee20)
- ブロック [`00baee20`](#insn-00baee20) 範囲 `[['00baee20', '00baee33']]`

## 命令位置別の参照

- [`00baedcc`](#insn-00baedcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedd0`](#insn-00baedd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baedf8`](#insn-00baedf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee10`](#insn-00baee10) → [`00bae6f8`](00bae6f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bae6f8` · 推定シンボル `None` · 推定型 `None`
- [`00baee14`](#insn-00baee14) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee20`](#insn-00baee20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baee24`](#insn-00baee24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baedcc`](#insn-00baedcc)

~~~json
{
  "source": "00baedcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedd0`](#insn-00baedd0)

~~~json
{
  "source": "00baedd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baedf8`](#insn-00baedf8)

~~~json
{
  "source": "00baedf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee10`](#insn-00baee10)

~~~json
{
  "source": "00baee10",
  "target": "00bae6f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baee14`](#insn-00baee14)

~~~json
{
  "source": "00baee14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee20`](#insn-00baee20)

~~~json
{
  "source": "00baee20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baee24`](#insn-00baee24)

~~~json
{
  "source": "00baee24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
