# 00adfacc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adfb94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adf/00adfb94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-a39d7947dac4a1885c2525c0ade646f1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adfacc",
  "name": "FUN_00adfacc",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0efc6a615a4b1bf28df52abff604d4cfcfbdb777745e0992455b30d6bdfbbae",
  "source_text_sha256": "b0efc6a615a4b1bf28df52abff604d4cfcfbdb777745e0992455b30d6bdfbbae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adfacc",
        "00adfbab"
      ]
    ],
    "bytes_sha256": "f03cb298628071044cbb2dc8504e574a5dc7ffcf98d642c1af2c52fc30349ed6",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00444c54](../00444/00444c54.md)
- [0044592c](../00445/0044592c.md)
- [00467c58](../00467/00467c58.md)
- [00886014](../00886/00886014.md)
- [00bdb6c0](../00bdb/00bdb6c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1773 bytes

~~~c

void FUN_00adfacc(undefined8 param_1,undefined8 *param_2,undefined8 *param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int extraout_var;
  int extraout_w1;
  int extraout_var_00;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
                    /* try { // try from 00adfad0 to 00bdfad7 has its CatchHandler @ 00adfc30 */
  uVar4 = *param_3;
  uVar5 = *param_2;
                    /* try { // try from 00adfaec to 00bdfb0b has its CatchHandler @ 00adfc0c */
  FUN_00444c54(uVar4,0xbe,0xbe,0xbe,0xff);
                    /* try { // try from 00adfb20 to 00bdfb23 has its CatchHandler @ 00adfc30 */
  lVar3 = __dynamic_cast(DAT_00c249b8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8d98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8da8,0);
  uVar6 = *(undefined8 *)(lVar3 + 0x38);
  iVar1 = FUN_00886014(uVar5);
                    /* try { // try from 00adfb38 to 00bdfb3f has its CatchHandler @ 00adfc00 */
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb54 to 00bdfb5b has its CatchHandler @ 00adfbfc */
  lVar3 = __dynamic_cast(DAT_00c249b8,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00be8d98,
                         &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00be8da8,0);
  iVar2 = FUN_00467c58(*(undefined8 *)(lVar3 + 0x38));
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb70 to 00bdfb77 has its CatchHandler @ 00adfc00 */
  FUN_00886014(uVar5);
                    /* try { // try from 00adfb8c to 00bdfb93 has its CatchHandler @ 00adfbe4 */
                    /* try { // try from 00adfba8 to 00bdfbab has its CatchHandler @ 00adfc00 */
  FUN_0044592c(uVar4,uVar6,(extraout_w1 + iVar1) - iVar2,extraout_var_00 + extraout_var,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adfacc"></a> `00adfacc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00adfad0"></a> `00adfad0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfad4"></a> `00adfad4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfad8"></a> `00adfad8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfadc"></a> `00adfadc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adfae0"></a> `00adfae0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adfae4"></a> `00adfae4` | `53 00 40 f9` | ldr x19,[x2] | `FALL_THROUGH`
<a id="insn-00adfae8"></a> `00adfae8` | `34 00 40 f9` | ldr x20,[x1] | `FALL_THROUGH`
<a id="insn-00adfaec"></a> `00adfaec` | `c1 17 80 52` | mov w1,#0xbe | `FALL_THROUGH`
<a id="insn-00adfaf0"></a> `00adfaf0` | `c2 17 80 52` | mov w2,#0xbe | `FALL_THROUGH`
<a id="insn-00adfaf4"></a> `00adfaf4` | `c3 17 80 52` | mov w3,#0xbe | `FALL_THROUGH`
<a id="insn-00adfaf8"></a> `00adfaf8` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-00adfafc"></a> `00adfafc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfb00"></a> `00adfb00` | `55 94 e5 97` | bl 0x00444c54 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb04"></a> `00adfb04` | `39 0a 00 b0` | adrp x25,0xc24000 | `FALL_THROUGH`
<a id="insn-00adfb08"></a> `00adfb08` | `55 08 00 b0` | adrp x21,0xbe8000 | `FALL_THROUGH`
<a id="insn-00adfb0c"></a> `00adfb0c` | `b5 62 36 91` | add x21,x21,#0xd98 | `FALL_THROUGH`
<a id="insn-00adfb10"></a> `00adfb10` | `20 df 44 f9` | ldr x0,[x25, #0x9b8] | `FALL_THROUGH`
<a id="insn-00adfb14"></a> `00adfb14` | `56 08 00 b0` | adrp x22,0xbe8000 | `FALL_THROUGH`
<a id="insn-00adfb18"></a> `00adfb18` | `d6 a2 36 91` | add x22,x22,#0xda8 | `FALL_THROUGH`
<a id="insn-00adfb1c"></a> `00adfb1c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adfb20"></a> `00adfb20` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00adfb24"></a> `00adfb24` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00adfb28"></a> `00adfb28` | `e6 ee 03 94` | bl 0x00bdb6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb2c"></a> `00adfb2c` | `17 1c 40 f9` | ldr x23,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00adfb30"></a> `00adfb30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfb34"></a> `00adfb34` | `38 99 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb38"></a> `00adfb38` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00adfb3c"></a> `00adfb3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfb40"></a> `00adfb40` | `35 99 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb44"></a> `00adfb44` | `20 df 44 f9` | ldr x0,[x25, #0x9b8] | `FALL_THROUGH`
<a id="insn-00adfb48"></a> `00adfb48` | `38 00 18 0b` | add w24,w1,w24 | `FALL_THROUGH`
<a id="insn-00adfb4c"></a> `00adfb4c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00adfb50"></a> `00adfb50` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00adfb54"></a> `00adfb54` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00adfb58"></a> `00adfb58` | `da ee 03 94` | bl 0x00bdb6c0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb5c"></a> `00adfb5c` | `00 1c 40 f9` | ldr x0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00adfb60"></a> `00adfb60` | `3e 20 e6 97` | bl 0x00467c58 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb64"></a> `00adfb64` | `15 03 00 4b` | sub w21,w24,w0 | `FALL_THROUGH`
<a id="insn-00adfb68"></a> `00adfb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfb6c"></a> `00adfb6c` | `2a 99 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb70"></a> `00adfb70` | `16 fc 60 d3` | lsr x22,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00adfb74"></a> `00adfb74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adfb78"></a> `00adfb78` | `27 99 f6 97` | bl 0x00886014 | `UNCONDITIONAL_CALL`
<a id="insn-00adfb7c"></a> `00adfb7c` | `28 fc 60 d3` | lsr x8,x1,#0x20 | `FALL_THROUGH`
<a id="insn-00adfb80"></a> `00adfb80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adfb84"></a> `00adfb84` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00adfb88"></a> `00adfb88` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00adfb8c"></a> `00adfb8c` | `03 01 16 0b` | add w3,w8,w22 | `FALL_THROUGH`
<a id="insn-00adfb90"></a> `00adfb90` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00adfb94"></a> `00adfb94` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00adfb98"></a> `00adfb98` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfb9c"></a> `00adfb9c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfba0"></a> `00adfba0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfba4"></a> `00adfba4` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00adfba8"></a> `00adfba8` | `61 97 e5 17` | b 0x0044592c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adfacc`](#insn-00adfacc) 範囲 `[['00adfacc', '00adfacf']]`
  - `FALL_THROUGH` [`00adfacc`](#insn-00adfacc) → [`00adfad0`](#insn-00adfad0)
- ブロック [`00adfad0`](#insn-00adfad0) 範囲 `[['00adfad0', '00adfaeb']]`
  - `FALL_THROUGH` [`00adfae8`](#insn-00adfae8) → [`00adfaec`](#insn-00adfaec)
- ブロック [`00adfaec`](#insn-00adfaec) 範囲 `[['00adfaec', '00adfb1f']]`
  - `FALL_THROUGH` [`00adfb1c`](#insn-00adfb1c) → [`00adfb20`](#insn-00adfb20)
- ブロック [`00adfb20`](#insn-00adfb20) 範囲 `[['00adfb20', '00adfb37']]`
  - `FALL_THROUGH` [`00adfb34`](#insn-00adfb34) → [`00adfb38`](#insn-00adfb38)
- ブロック [`00adfb38`](#insn-00adfb38) 範囲 `[['00adfb38', '00adfb53']]`
  - `FALL_THROUGH` [`00adfb50`](#insn-00adfb50) → [`00adfb54`](#insn-00adfb54)
- ブロック [`00adfb54`](#insn-00adfb54) 範囲 `[['00adfb54', '00adfb6f']]`
  - `FALL_THROUGH` [`00adfb6c`](#insn-00adfb6c) → [`00adfb70`](#insn-00adfb70)
- ブロック [`00adfb70`](#insn-00adfb70) 範囲 `[['00adfb70', '00adfb8b']]`
  - `FALL_THROUGH` [`00adfb88`](#insn-00adfb88) → [`00adfb8c`](#insn-00adfb8c)
- ブロック [`00adfb8c`](#insn-00adfb8c) 範囲 `[['00adfb8c', '00adfba7']]`
  - `FALL_THROUGH` [`00adfba4`](#insn-00adfba4) → [`00adfba8`](#insn-00adfba8)
- ブロック [`00adfba8`](#insn-00adfba8) 範囲 `[['00adfba8', '00adfbab']]`

## 命令位置別の参照

- [`00adfacc`](#insn-00adfacc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfad0`](#insn-00adfad0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfad4`](#insn-00adfad4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfad8`](#insn-00adfad8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfadc`](#insn-00adfadc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb00`](#insn-00adfb00) → [`00444c54`](../00444/00444c54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00444c54` · 推定シンボル `None` · 推定型 `None`
- [`00adfb10`](#insn-00adfb10) → `00c249b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfb1c`](#insn-00adfb1c) → `00be8d98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfb20`](#insn-00adfb20) → `00be8da8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfb28`](#insn-00adfb28) → [`00bdb6c0`](../00bdb/00bdb6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6c0` · 推定シンボル `None` · 推定型 `None`
- [`00adfb34`](#insn-00adfb34) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfb40`](#insn-00adfb40) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfb44`](#insn-00adfb44) → `00c249b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00adfb4c`](#insn-00adfb4c) → `00be8d98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfb50`](#insn-00adfb50) → `00be8da8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00adfb58`](#insn-00adfb58) → [`00bdb6c0`](../00bdb/00bdb6c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb6c0` · 推定シンボル `None` · 推定型 `None`
- [`00adfb60`](#insn-00adfb60) → [`00467c58`](../00467/00467c58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467c58` · 推定シンボル `None` · 推定型 `None`
- [`00adfb6c`](#insn-00adfb6c) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfb78`](#insn-00adfb78) → [`00886014`](../00886/00886014.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00886014` · 推定シンボル `None` · 推定型 `None`
- [`00adfb94`](#insn-00adfb94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb98`](#insn-00adfb98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb9c`](#insn-00adfb9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfba0`](#insn-00adfba0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfba4`](#insn-00adfba4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfba8`](#insn-00adfba8) → [`0044592c`](../00445/0044592c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044592c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adfacc`](#insn-00adfacc)

~~~json
{
  "source": "00adfacc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfad0`](#insn-00adfad0)

~~~json
{
  "source": "00adfad0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfad4`](#insn-00adfad4)

~~~json
{
  "source": "00adfad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfad8`](#insn-00adfad8)

~~~json
{
  "source": "00adfad8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfadc`](#insn-00adfadc)

~~~json
{
  "source": "00adfadc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb00`](#insn-00adfb00)

~~~json
{
  "source": "00adfb00",
  "target": "00444c54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb10`](#insn-00adfb10)

~~~json
{
  "source": "00adfb10",
  "target": "00c249b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfb1c`](#insn-00adfb1c)

~~~json
{
  "source": "00adfb1c",
  "target": "00be8d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8d98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfb20`](#insn-00adfb20)

~~~json
{
  "source": "00adfb20",
  "target": "00be8da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8da8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfb28`](#insn-00adfb28)

~~~json
{
  "source": "00adfb28",
  "target": "00bdb6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb34`](#insn-00adfb34)

~~~json
{
  "source": "00adfb34",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb40`](#insn-00adfb40)

~~~json
{
  "source": "00adfb40",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb44`](#insn-00adfb44)

~~~json
{
  "source": "00adfb44",
  "target": "00c249b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c249b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00adfb4c`](#insn-00adfb4c)

~~~json
{
  "source": "00adfb4c",
  "target": "00be8d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8d98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfb50`](#insn-00adfb50)

~~~json
{
  "source": "00adfb50",
  "target": "00be8da8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be8da8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00adfb58`](#insn-00adfb58)

~~~json
{
  "source": "00adfb58",
  "target": "00bdb6c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb60`](#insn-00adfb60)

~~~json
{
  "source": "00adfb60",
  "target": "00467c58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb6c`](#insn-00adfb6c)

~~~json
{
  "source": "00adfb6c",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb78`](#insn-00adfb78)

~~~json
{
  "source": "00adfb78",
  "target": "00886014",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb94`](#insn-00adfb94)

~~~json
{
  "source": "00adfb94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb98`](#insn-00adfb98)

~~~json
{
  "source": "00adfb98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb9c`](#insn-00adfb9c)

~~~json
{
  "source": "00adfb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfba0`](#insn-00adfba0)

~~~json
{
  "source": "00adfba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfba4`](#insn-00adfba4)

~~~json
{
  "source": "00adfba4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfba8`](#insn-00adfba8)

~~~json
{
  "source": "00adfba8",
  "target": "0044592c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
