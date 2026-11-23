# 00baecf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baec28`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baec28.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-0ba0ca15cb4608bb043b298f20b0cbb0)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00baed34`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baed34.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-fb456dbad5e44024fcfa0c35e7d0dac3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baecf0",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e77444ccc37635cd39e097a7b1122ca0f6aa9007c8f8a2bc60459c14bb46b02",
  "source_text_sha256": "9e77444ccc37635cd39e097a7b1122ca0f6aa9007c8f8a2bc60459c14bb46b02",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baecf0",
        "00baed5f"
      ]
    ],
    "bytes_sha256": "98c665bafcf7c39184ec76bdbd4eddf133de80836d3c4decd450e5e69fa27f42",
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

- [00bac0ec](../00bac/00bac0ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 864 bytes

~~~c

void _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 *param_5,undefined8 param_6,undefined8 param_7,undefined8 *param_8)

{
  undefined8 local_30;
  undefined8 uStack_28;
  
                    /* try { // try from 00baed1c to 00caed27 has its CatchHandler @ 00baedf8 */
                    /* try { // try from 00baed28 to 00caed37 has its CatchHandler @ 00baede0 */
  local_30 = param_6;
  uStack_28 = param_3;
                    /* try { // try from 00baed38 to 00caeea7 has its CatchHandler @ 00baeb80 */
  FUN_00bac0ec(param_3,param_4,&uStack_28,param_6,param_7,&local_30,*(undefined8 *)(param_1 + 0x10),
               *(undefined4 *)(param_1 + 0x18));
  *param_5 = uStack_28;
  *param_8 = local_30;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baecf0"></a> `00baecf0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baecf4"></a> `00baecf4` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baecf8"></a> `00baecf8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baecfc"></a> `00baecfc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed00"></a> `00baed00` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00baed04"></a> `00baed04` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00baed08"></a> `00baed08` | `ea 03 06 aa` | mov x10,x6 | `FALL_THROUGH`
<a id="insn-00baed0c"></a> `00baed0c` | `e8 03 05 aa` | mov x8,x5 | `FALL_THROUGH`
<a id="insn-00baed10"></a> `00baed10` | `e9 03 02 aa` | mov x9,x2 | `FALL_THROUGH`
<a id="insn-00baed14"></a> `00baed14` | `06 08 40 f9` | ldr x6,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baed18"></a> `00baed18` | `07 18 40 b9` | ldr w7,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baed1c"></a> `00baed1c` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00baed20"></a> `00baed20` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00baed24"></a> `00baed24` | `e5 0b 00 a9` | stp x5,x2,[sp] | `FALL_THROUGH`
<a id="insn-00baed28"></a> `00baed28` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00baed2c"></a> `00baed2c` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00baed30"></a> `00baed30` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00baed34"></a> `00baed34` | `e3 03 08 aa` | mov x3,x8 | `FALL_THROUGH`
<a id="insn-00baed38"></a> `00baed38` | `e4 03 0a aa` | mov x4,x10 | `FALL_THROUGH`
<a id="insn-00baed3c"></a> `00baed3c` | `ec f4 ff 97` | bl 0x00bac0ec | `UNCONDITIONAL_CALL`
<a id="insn-00baed40"></a> `00baed40` | `e9 23 40 a9` | ldp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00baed44"></a> `00baed44` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baed48"></a> `00baed48` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00baed4c"></a> `00baed4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baed50"></a> `00baed50` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baed54"></a> `00baed54` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00baed58"></a> `00baed58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baed5c"></a> `00baed5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baecf0`](#insn-00baecf0) 範囲 `[['00baecf0', '00baed1b']]`
  - `FALL_THROUGH` [`00baed18`](#insn-00baed18) → [`00baed1c`](#insn-00baed1c)
- ブロック [`00baed1c`](#insn-00baed1c) 範囲 `[['00baed1c', '00baed27']]`
  - `FALL_THROUGH` [`00baed24`](#insn-00baed24) → [`00baed28`](#insn-00baed28)
- ブロック [`00baed28`](#insn-00baed28) 範囲 `[['00baed28', '00baed37']]`
  - `FALL_THROUGH` [`00baed34`](#insn-00baed34) → [`00baed38`](#insn-00baed38)
- ブロック [`00baed38`](#insn-00baed38) 範囲 `[['00baed38', '00baed5f']]`

## 命令位置別の参照

- [`00baecf8`](#insn-00baecf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baecfc`](#insn-00baecfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed24`](#insn-00baed24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed3c`](#insn-00baed3c) → [`00bac0ec`](../00bac/00bac0ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bac0ec` · 推定シンボル `None` · 推定型 `None`
- [`00baed40`](#insn-00baed40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed4c`](#insn-00baed4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baed50`](#insn-00baed50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baecf8`](#insn-00baecf8)

~~~json
{
  "source": "00baecf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baecfc`](#insn-00baecfc)

~~~json
{
  "source": "00baecfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed24`](#insn-00baed24)

~~~json
{
  "source": "00baed24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed3c`](#insn-00baed3c)

~~~json
{
  "source": "00baed3c",
  "target": "00bac0ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baed40`](#insn-00baed40)

~~~json
{
  "source": "00baed40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed4c`](#insn-00baed4c)

~~~json
{
  "source": "00baed4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baed50`](#insn-00baed50)

~~~json
{
  "source": "00baed50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
