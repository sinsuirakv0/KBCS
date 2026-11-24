# 00bafaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bafa60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafa60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-970d73abe66c583655bba01932c08c69)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2c4ec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c4ec.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-c1602a545160e2518fca585cb5542a8c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafaa4",
  "name": "_ZNSt6__ndk114__num_put_base12__format_intEPcPKcbj",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e79090be92b493f74963e7274026d58b7edd228d118b564784e80c94d0cb61e5",
  "source_text_sha256": "e79090be92b493f74963e7274026d58b7edd228d118b564784e80c94d0cb61e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafaa4",
        "00bafb47"
      ]
    ],
    "bytes_sha256": "b468e19b8ec5c0cfeeb442c6c4990e4f094eebe8d435331a4632ead4190b58e1",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1877 bytes

~~~c

void _ZNSt6__ndk114__num_put_base12__format_intEPcPKcbj
               (char *param_1,char *param_2,uint param_3,uint param_4)

{
  char *pcVar1;
  char *pcVar2;
  char cVar3;
  
  pcVar1 = param_1;
  if (((((param_4 >> 0xb & 1) != 0) && ((param_4 & 0x4a) != 8)) && ((param_4 & 0x4a) != 0x40)) &&
     ((param_3 & 1) != 0)) {
                    /* try { // try from 00bafac8 to 00cafacf has its CatchHandler @ 00bafb40 */
    pcVar1 = param_1 + 1;
    *param_1 = '+';
  }
  pcVar2 = pcVar1;
  if ((param_4 >> 9 & 1) != 0) {
    pcVar2 = pcVar1 + 1;
    *pcVar1 = '#';
  }
  cVar3 = *param_2;
  while (cVar3 != '\0') {
    param_2 = param_2 + 1;
    *pcVar2 = cVar3;
    pcVar2 = pcVar2 + 1;
    cVar3 = *param_2;
  }
                    /* try { // try from 00bafaf8 to 00cafaff has its CatchHandler @ 00bafb3c */
                    /* try { // try from 00bafb00 to 00cafb2b has its CatchHandler @ 00baf9fc */
  if ((param_4 & 0x4a) != 0x40) {
    if ((param_4 & 0x4a) == 8) {
      cVar3 = 'x';
      if ((param_4 & 0x4000) != 0) {
        cVar3 = 'X';
      }
      *pcVar2 = cVar3;
      return;
    }
    cVar3 = 'd';
                    /* try { // try from 00bafb34 to 00cafb3b has its CatchHandler @ 00bafb3c */
                    /* catch() { ... } // from try @ 00bafaf8 with catch @ 00bafb3c
                       catch() { ... } // from try @ 00bafb34 with catch @ 00bafb3c
                       try { // try from 00bafb3c to 00cafb5f has its CatchHandler @ 00baf9fc */
    if ((param_3 & 1) == 0) {
      cVar3 = 'u';
    }
                    /* catch() { ... } // from try @ 00bafac8 with catch @ 00bafb40
                       catch() { ... } // from try @ 00bafb2c with catch @ 00bafb40 */
    *pcVar2 = cVar3;
    return;
  }
  *pcVar2 = 'o';
                    /* try { // try from 00bafb2c to 00cafb33 has its CatchHandler @ 00bafb40 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafaa4"></a> `00bafaa4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bafaa8"></a> `00bafaa8` | `43 01 58 36` | tbz w3,#0xb,0x00bafad0 | `CONDITIONAL_JUMP`
<a id="insn-00bafaac"></a> `00bafaac` | `48 09 80 52` | mov w8,#0x4a | `FALL_THROUGH`
<a id="insn-00bafab0"></a> `00bafab0` | `68 00 08 0a` | and w8,w3,w8 | `FALL_THROUGH`
<a id="insn-00bafab4"></a> `00bafab4` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bafab8"></a> `00bafab8` | `c0 00 00 54` | b.eq 0x00bafad0 | `CONDITIONAL_JUMP`
<a id="insn-00bafabc"></a> `00bafabc` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bafac0"></a> `00bafac0` | `80 00 00 54` | b.eq 0x00bafad0 | `CONDITIONAL_JUMP`
<a id="insn-00bafac4"></a> `00bafac4` | `62 00 00 36` | tbz w2,#0x0,0x00bafad0 | `CONDITIONAL_JUMP`
<a id="insn-00bafac8"></a> `00bafac8` | `68 05 80 52` | mov w8,#0x2b | `FALL_THROUGH`
<a id="insn-00bafacc"></a> `00bafacc` | `08 14 00 38` | strb w8,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00bafad0"></a> `00bafad0` | `63 00 48 36` | tbz w3,#0x9,0x00bafadc | `CONDITIONAL_JUMP`
<a id="insn-00bafad4"></a> `00bafad4` | `68 04 80 52` | mov w8,#0x23 | `FALL_THROUGH`
<a id="insn-00bafad8"></a> `00bafad8` | `08 14 00 38` | strb w8,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00bafadc"></a> `00bafadc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bafae0"></a> `00bafae0` | `a8 00 00 34` | cbz w8,0x00bafaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bafae4"></a> `00bafae4` | `29 04 00 91` | add x9,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00bafae8"></a> `00bafae8` | `08 14 00 38` | strb w8,[x0], #0x1 | `FALL_THROUGH`
<a id="insn-00bafaec"></a> `00bafaec` | `28 15 40 38` | ldrb w8,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00bafaf0"></a> `00bafaf0` | `c8 ff ff 35` | cbnz w8,0x00bafae8 | `CONDITIONAL_JUMP`
<a id="insn-00bafaf4"></a> `00bafaf4` | `48 09 80 52` | mov w8,#0x4a | `FALL_THROUGH`
<a id="insn-00bafaf8"></a> `00bafaf8` | `68 00 08 0a` | and w8,w3,w8 | `FALL_THROUGH`
<a id="insn-00bafafc"></a> `00bafafc` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bafb00"></a> `00bafb00` | `20 01 00 54` | b.eq 0x00bafb24 | `CONDITIONAL_JUMP`
<a id="insn-00bafb04"></a> `00bafb04` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bafb08"></a> `00bafb08` | `41 01 00 54` | b.ne 0x00bafb30 | `CONDITIONAL_JUMP`
<a id="insn-00bafb0c"></a> `00bafb0c` | `7f 00 12 72` | tst w3,#0x4000 | `FALL_THROUGH`
<a id="insn-00bafb10"></a> `00bafb10` | `08 0b 80 52` | mov w8,#0x58 | `FALL_THROUGH`
<a id="insn-00bafb14"></a> `00bafb14` | `09 0f 80 52` | mov w9,#0x78 | `FALL_THROUGH`
<a id="insn-00bafb18"></a> `00bafb18` | `28 01 88 1a` | csel w8,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00bafb1c"></a> `00bafb1c` | `08 00 00 39` | strb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bafb20"></a> `00bafb20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafb24"></a> `00bafb24` | `e8 0d 80 52` | mov w8,#0x6f | `FALL_THROUGH`
<a id="insn-00bafb28"></a> `00bafb28` | `08 00 00 39` | strb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bafb2c"></a> `00bafb2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafb30"></a> `00bafb30` | `5f 00 00 72` | tst w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bafb34"></a> `00bafb34` | `a8 0e 80 52` | mov w8,#0x75 | `FALL_THROUGH`
<a id="insn-00bafb38"></a> `00bafb38` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00bafb3c"></a> `00bafb3c` | `28 11 88 1a` | csel w8,w9,w8,ne | `FALL_THROUGH`
<a id="insn-00bafb40"></a> `00bafb40` | `08 00 00 39` | strb w8,[x0] | `FALL_THROUGH`
<a id="insn-00bafb44"></a> `00bafb44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafaa4`](#insn-00bafaa4) 範囲 `[['00bafaa4', '00bafaab']]`
  - `CONDITIONAL_JUMP` [`00bafaa8`](#insn-00bafaa8) → [`00bafad0`](#insn-00bafad0)
  - `FALL_THROUGH` [`00bafaa8`](#insn-00bafaa8) → [`00bafaac`](#insn-00bafaac)
- ブロック [`00bafaac`](#insn-00bafaac) 範囲 `[['00bafaac', '00bafabb']]`
  - `CONDITIONAL_JUMP` [`00bafab8`](#insn-00bafab8) → [`00bafad0`](#insn-00bafad0)
  - `FALL_THROUGH` [`00bafab8`](#insn-00bafab8) → [`00bafabc`](#insn-00bafabc)
- ブロック [`00bafabc`](#insn-00bafabc) 範囲 `[['00bafabc', '00bafac3']]`
  - `CONDITIONAL_JUMP` [`00bafac0`](#insn-00bafac0) → [`00bafad0`](#insn-00bafad0)
  - `FALL_THROUGH` [`00bafac0`](#insn-00bafac0) → [`00bafac4`](#insn-00bafac4)
- ブロック [`00bafac4`](#insn-00bafac4) 範囲 `[['00bafac4', '00bafac7']]`
  - `CONDITIONAL_JUMP` [`00bafac4`](#insn-00bafac4) → [`00bafad0`](#insn-00bafad0)
  - `FALL_THROUGH` [`00bafac4`](#insn-00bafac4) → [`00bafac8`](#insn-00bafac8)
- ブロック [`00bafac8`](#insn-00bafac8) 範囲 `[['00bafac8', '00bafacf']]`
  - `FALL_THROUGH` [`00bafacc`](#insn-00bafacc) → [`00bafad0`](#insn-00bafad0)
- ブロック [`00bafad0`](#insn-00bafad0) 範囲 `[['00bafad0', '00bafad3']]`
  - `CONDITIONAL_JUMP` [`00bafad0`](#insn-00bafad0) → [`00bafadc`](#insn-00bafadc)
  - `FALL_THROUGH` [`00bafad0`](#insn-00bafad0) → [`00bafad4`](#insn-00bafad4)
- ブロック [`00bafad4`](#insn-00bafad4) 範囲 `[['00bafad4', '00bafadb']]`
  - `FALL_THROUGH` [`00bafad8`](#insn-00bafad8) → [`00bafadc`](#insn-00bafadc)
- ブロック [`00bafadc`](#insn-00bafadc) 範囲 `[['00bafadc', '00bafae3']]`
  - `CONDITIONAL_JUMP` [`00bafae0`](#insn-00bafae0) → [`00bafaf4`](#insn-00bafaf4)
  - `FALL_THROUGH` [`00bafae0`](#insn-00bafae0) → [`00bafae4`](#insn-00bafae4)
- ブロック [`00bafae4`](#insn-00bafae4) 範囲 `[['00bafae4', '00bafae7']]`
  - `FALL_THROUGH` [`00bafae4`](#insn-00bafae4) → [`00bafae8`](#insn-00bafae8)
- ブロック [`00bafae8`](#insn-00bafae8) 範囲 `[['00bafae8', '00bafaf3']]`
  - `CONDITIONAL_JUMP` [`00bafaf0`](#insn-00bafaf0) → [`00bafae8`](#insn-00bafae8)
  - `FALL_THROUGH` [`00bafaf0`](#insn-00bafaf0) → [`00bafaf4`](#insn-00bafaf4)
- ブロック [`00bafaf4`](#insn-00bafaf4) 範囲 `[['00bafaf4', '00bafaf7']]`
  - `FALL_THROUGH` [`00bafaf4`](#insn-00bafaf4) → [`00bafaf8`](#insn-00bafaf8)
- ブロック [`00bafaf8`](#insn-00bafaf8) 範囲 `[['00bafaf8', '00bafaff']]`
  - `FALL_THROUGH` [`00bafafc`](#insn-00bafafc) → [`00bafb00`](#insn-00bafb00)
- ブロック [`00bafb00`](#insn-00bafb00) 範囲 `[['00bafb00', '00bafb03']]`
  - `CONDITIONAL_JUMP` [`00bafb00`](#insn-00bafb00) → [`00bafb24`](#insn-00bafb24)
  - `FALL_THROUGH` [`00bafb00`](#insn-00bafb00) → [`00bafb04`](#insn-00bafb04)
- ブロック [`00bafb04`](#insn-00bafb04) 範囲 `[['00bafb04', '00bafb0b']]`
  - `CONDITIONAL_JUMP` [`00bafb08`](#insn-00bafb08) → [`00bafb30`](#insn-00bafb30)
  - `FALL_THROUGH` [`00bafb08`](#insn-00bafb08) → [`00bafb0c`](#insn-00bafb0c)
- ブロック [`00bafb0c`](#insn-00bafb0c) 範囲 `[['00bafb0c', '00bafb23']]`
- ブロック [`00bafb24`](#insn-00bafb24) 範囲 `[['00bafb24', '00bafb2b']]`
  - `FALL_THROUGH` [`00bafb28`](#insn-00bafb28) → [`00bafb2c`](#insn-00bafb2c)
- ブロック [`00bafb2c`](#insn-00bafb2c) 範囲 `[['00bafb2c', '00bafb2f']]`
- ブロック [`00bafb30`](#insn-00bafb30) 範囲 `[['00bafb30', '00bafb33']]`
  - `FALL_THROUGH` [`00bafb30`](#insn-00bafb30) → [`00bafb34`](#insn-00bafb34)
- ブロック [`00bafb34`](#insn-00bafb34) 範囲 `[['00bafb34', '00bafb3b']]`
  - `FALL_THROUGH` [`00bafb38`](#insn-00bafb38) → [`00bafb3c`](#insn-00bafb3c)
- ブロック [`00bafb3c`](#insn-00bafb3c) 範囲 `[['00bafb3c', '00bafb3f']]`
  - `FALL_THROUGH` [`00bafb3c`](#insn-00bafb3c) → [`00bafb40`](#insn-00bafb40)
- ブロック [`00bafb40`](#insn-00bafb40) 範囲 `[['00bafb40', '00bafb47']]`

## 命令位置別の参照

- [`00bafaa8`](#insn-00bafaa8) → [`00bafad0`](#insn-00bafad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafab8`](#insn-00bafab8) → [`00bafad0`](#insn-00bafad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafac0`](#insn-00bafac0) → [`00bafad0`](#insn-00bafad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafac4`](#insn-00bafac4) → [`00bafad0`](#insn-00bafad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafad0`](#insn-00bafad0) → [`00bafadc`](#insn-00bafadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafae0`](#insn-00bafae0) → [`00bafaf4`](#insn-00bafaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafaf0`](#insn-00bafaf0) → [`00bafae8`](#insn-00bafae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb00`](#insn-00bafb00) → [`00bafb24`](#insn-00bafb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafb08`](#insn-00bafb08) → [`00bafb30`](#insn-00bafb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafaa8`](#insn-00bafaa8)

~~~json
{
  "source": "00bafaa8",
  "target": "00bafad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafab8`](#insn-00bafab8)

~~~json
{
  "source": "00bafab8",
  "target": "00bafad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafac0`](#insn-00bafac0)

~~~json
{
  "source": "00bafac0",
  "target": "00bafad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafac4`](#insn-00bafac4)

~~~json
{
  "source": "00bafac4",
  "target": "00bafad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafad0`](#insn-00bafad0)

~~~json
{
  "source": "00bafad0",
  "target": "00bafadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafae0`](#insn-00bafae0)

~~~json
{
  "source": "00bafae0",
  "target": "00bafaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafaf0`](#insn-00bafaf0)

~~~json
{
  "source": "00bafaf0",
  "target": "00bafae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb00`](#insn-00bafb00)

~~~json
{
  "source": "00bafb00",
  "target": "00bafb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafb08`](#insn-00bafb08)

~~~json
{
  "source": "00bafb08",
  "target": "00bafb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
