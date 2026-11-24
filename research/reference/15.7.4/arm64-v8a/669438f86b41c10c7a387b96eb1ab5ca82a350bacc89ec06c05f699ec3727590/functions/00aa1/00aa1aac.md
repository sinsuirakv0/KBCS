# 00aa1aac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa1a68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1a68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0058.md#compare-65a0890cef0a2e6dd5ae087572a6d65e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0088.md#review-c91ac2ed242fa40ed93559030fb44fc8)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1aac",
  "name": "FUN_00aa1aac",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f5a7834c95c2f55525a1f699f3595ce1c742c995c07ad82e51427d7b37300ee",
  "source_text_sha256": "2f5a7834c95c2f55525a1f699f3595ce1c742c995c07ad82e51427d7b37300ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1aac",
        "00aa1b3f"
      ]
    ],
    "bytes_sha256": "c9da9f3da6b1c99776c99494c3a0155505e7c8ce45b5f9433e1ed297a640de09",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [006a0ab4](../006a0/006a0ab4.md)
- [009f1ea8](../009f1/009f1ea8.md)
- [00aa0f64](../00aa0/00aa0f64.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c70](../00aa2/00aa2c70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2410 bytes

~~~c

undefined8 FUN_00aa1aac(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* catch() { ... } // from try @ 00aa04dc with catch @ 00aa1aac */
                    /* catch() { ... } // from try @ 00aa0484 with catch @ 00aa1ab0 */
                    /* catch() { ... } // from try @ 00aa0380 with catch @ 00aa1ab4 */
                    /* catch() { ... } // from try @ 00aa027c with catch @ 00aa1ab8 */
                    /* catch() { ... } // from try @ 00aa03f0 with catch @ 00aa1abc */
                    /* catch() { ... } // from try @ 00aa03dc with catch @ 00aa1ac0 */
                    /* catch() { ... } // from try @ 00aa03c4 with catch @ 00aa1ac4 */
                    /* catch() { ... } // from try @ 00aa0ecc with catch @ 00aa1ac8 */
  lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0f68 with catch @ 00aa1acc */
                    /* catch() { ... } // from try @ 00a9ff74 with catch @ 00aa1ad0 */
                    /* catch() { ... } // from try @ 00a9ff64 with catch @ 00aa1ad4 */
                    /* catch() { ... } // from try @ 00aa0314 with catch @ 00aa1ad8 */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar2 & 1) == 0) {
    uVar3 = 0;
  }
  else {
    lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0300 with catch @ 00aa1af0 */
                    /* catch() { ... } // from try @ 00aa0f74 with catch @ 00aa1b08 */
                    /* catch() { ... } // from try @ 00a9ffc8 with catch @ 00aa1b0c */
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9fdc4) == 0) {
                    /* catch() { ... } // from try @ 00aa052c with catch @ 00aa1b28 */
                    /* catch() { ... } // from try @ 00aa0020 with catch @ 00aa1b2c */
                    /* catch() { ... } // from try @ 00aa0674 with catch @ 00aa1b30 */
                    /* catch() { ... } // from try @ 00aa1774 with catch @ 00aa1b34 */
                    /* catch() { ... } // from try @ 00aa0984 with catch @ 00aa1b38 */
                    /* catch() { ... } // from try @ 00aa0108 with catch @ 00aa1b3c */
      uVar3 = FUN_00aa2c70(lVar1,param_2,param_3,5);
      return uVar3;
    }
                    /* catch() { ... } // from try @ 00a9feb4 with catch @ 00aa1b10 */
    uVar3 = 1;
  }
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa1aac"></a> `00aa1aac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa1ab0"></a> `00aa1ab0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1ab4"></a> `00aa1ab4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1ab8"></a> `00aa1ab8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa1abc"></a> `00aa1abc` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa1ac0"></a> `00aa1ac0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa1ac4"></a> `00aa1ac4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa1ac8"></a> `00aa1ac8` | `ae f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1acc"></a> `00aa1acc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa1ad0"></a> `00aa1ad0` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa1ad4"></a> `00aa1ad4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa1ad8"></a> `00aa1ad8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1adc"></a> `00aa1adc` | `0d 83 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1ae0"></a> `00aa1ae0` | `60 00 00 37` | tbnz w0,#0x0,0x00aa1aec | `CONDITIONAL_JUMP`
<a id="insn-00aa1ae4"></a> `00aa1ae4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa1ae8"></a> `00aa1ae8` | `0b 00 00 14` | b 0x00aa1b14 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1aec"></a> `00aa1aec` | `a5 f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1af0"></a> `00aa1af0` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00aa1af4"></a> `00aa1af4` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa1af8"></a> `00aa1af8` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa1afc"></a> `00aa1afc` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa1b00"></a> `00aa1b00` | `89 b8 9f 52` | mov w9,#0xfdc4 | `FALL_THROUGH`
<a id="insn-00aa1b04"></a> `00aa1b04` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa1b08"></a> `00aa1b08` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa1b0c"></a> `00aa1b0c` | `c8 00 00 34` | cbz w8,0x00aa1b24 | `CONDITIONAL_JUMP`
<a id="insn-00aa1b10"></a> `00aa1b10` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa1b14"></a> `00aa1b14` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1b18"></a> `00aa1b18` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1b1c"></a> `00aa1b1c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa1b20"></a> `00aa1b20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa1b24"></a> `00aa1b24` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa1b28"></a> `00aa1b28` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa1b2c"></a> `00aa1b2c` | `a3 00 80 52` | mov w3,#0x5 | `FALL_THROUGH`
<a id="insn-00aa1b30"></a> `00aa1b30` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1b34"></a> `00aa1b34` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1b38"></a> `00aa1b38` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa1b3c"></a> `00aa1b3c` | `4d 04 00 14` | b 0x00aa2c70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1aac`](#insn-00aa1aac) 範囲 `[['00aa1aac', '00aa1aaf']]`
  - `FALL_THROUGH` [`00aa1aac`](#insn-00aa1aac) → [`00aa1ab0`](#insn-00aa1ab0)
- ブロック [`00aa1ab0`](#insn-00aa1ab0) 範囲 `[['00aa1ab0', '00aa1ab3']]`
  - `FALL_THROUGH` [`00aa1ab0`](#insn-00aa1ab0) → [`00aa1ab4`](#insn-00aa1ab4)
- ブロック [`00aa1ab4`](#insn-00aa1ab4) 範囲 `[['00aa1ab4', '00aa1ab7']]`
  - `FALL_THROUGH` [`00aa1ab4`](#insn-00aa1ab4) → [`00aa1ab8`](#insn-00aa1ab8)
- ブロック [`00aa1ab8`](#insn-00aa1ab8) 範囲 `[['00aa1ab8', '00aa1abb']]`
  - `FALL_THROUGH` [`00aa1ab8`](#insn-00aa1ab8) → [`00aa1abc`](#insn-00aa1abc)
- ブロック [`00aa1abc`](#insn-00aa1abc) 範囲 `[['00aa1abc', '00aa1abf']]`
  - `FALL_THROUGH` [`00aa1abc`](#insn-00aa1abc) → [`00aa1ac0`](#insn-00aa1ac0)
- ブロック [`00aa1ac0`](#insn-00aa1ac0) 範囲 `[['00aa1ac0', '00aa1ac3']]`
  - `FALL_THROUGH` [`00aa1ac0`](#insn-00aa1ac0) → [`00aa1ac4`](#insn-00aa1ac4)
- ブロック [`00aa1ac4`](#insn-00aa1ac4) 範囲 `[['00aa1ac4', '00aa1ac7']]`
  - `FALL_THROUGH` [`00aa1ac4`](#insn-00aa1ac4) → [`00aa1ac8`](#insn-00aa1ac8)
- ブロック [`00aa1ac8`](#insn-00aa1ac8) 範囲 `[['00aa1ac8', '00aa1acb']]`
  - `FALL_THROUGH` [`00aa1ac8`](#insn-00aa1ac8) → [`00aa1acc`](#insn-00aa1acc)
- ブロック [`00aa1acc`](#insn-00aa1acc) 範囲 `[['00aa1acc', '00aa1acf']]`
  - `FALL_THROUGH` [`00aa1acc`](#insn-00aa1acc) → [`00aa1ad0`](#insn-00aa1ad0)
- ブロック [`00aa1ad0`](#insn-00aa1ad0) 範囲 `[['00aa1ad0', '00aa1ad3']]`
  - `FALL_THROUGH` [`00aa1ad0`](#insn-00aa1ad0) → [`00aa1ad4`](#insn-00aa1ad4)
- ブロック [`00aa1ad4`](#insn-00aa1ad4) 範囲 `[['00aa1ad4', '00aa1ad7']]`
  - `FALL_THROUGH` [`00aa1ad4`](#insn-00aa1ad4) → [`00aa1ad8`](#insn-00aa1ad8)
- ブロック [`00aa1ad8`](#insn-00aa1ad8) 範囲 `[['00aa1ad8', '00aa1ae3']]`
  - `CONDITIONAL_JUMP` [`00aa1ae0`](#insn-00aa1ae0) → [`00aa1aec`](#insn-00aa1aec)
  - `FALL_THROUGH` [`00aa1ae0`](#insn-00aa1ae0) → [`00aa1ae4`](#insn-00aa1ae4)
- ブロック [`00aa1ae4`](#insn-00aa1ae4) 範囲 `[['00aa1ae4', '00aa1aeb']]`
  - `UNCONDITIONAL_JUMP` [`00aa1ae8`](#insn-00aa1ae8) → [`00aa1b14`](#insn-00aa1b14)
- ブロック [`00aa1aec`](#insn-00aa1aec) 範囲 `[['00aa1aec', '00aa1aef']]`
  - `FALL_THROUGH` [`00aa1aec`](#insn-00aa1aec) → [`00aa1af0`](#insn-00aa1af0)
- ブロック [`00aa1af0`](#insn-00aa1af0) 範囲 `[['00aa1af0', '00aa1b07']]`
  - `FALL_THROUGH` [`00aa1b04`](#insn-00aa1b04) → [`00aa1b08`](#insn-00aa1b08)
- ブロック [`00aa1b08`](#insn-00aa1b08) 範囲 `[['00aa1b08', '00aa1b0b']]`
  - `FALL_THROUGH` [`00aa1b08`](#insn-00aa1b08) → [`00aa1b0c`](#insn-00aa1b0c)
- ブロック [`00aa1b0c`](#insn-00aa1b0c) 範囲 `[['00aa1b0c', '00aa1b0f']]`
  - `CONDITIONAL_JUMP` [`00aa1b0c`](#insn-00aa1b0c) → [`00aa1b24`](#insn-00aa1b24)
  - `FALL_THROUGH` [`00aa1b0c`](#insn-00aa1b0c) → [`00aa1b10`](#insn-00aa1b10)
- ブロック [`00aa1b10`](#insn-00aa1b10) 範囲 `[['00aa1b10', '00aa1b13']]`
  - `FALL_THROUGH` [`00aa1b10`](#insn-00aa1b10) → [`00aa1b14`](#insn-00aa1b14)
- ブロック [`00aa1b14`](#insn-00aa1b14) 範囲 `[['00aa1b14', '00aa1b23']]`
- ブロック [`00aa1b24`](#insn-00aa1b24) 範囲 `[['00aa1b24', '00aa1b27']]`
  - `FALL_THROUGH` [`00aa1b24`](#insn-00aa1b24) → [`00aa1b28`](#insn-00aa1b28)
- ブロック [`00aa1b28`](#insn-00aa1b28) 範囲 `[['00aa1b28', '00aa1b2b']]`
  - `FALL_THROUGH` [`00aa1b28`](#insn-00aa1b28) → [`00aa1b2c`](#insn-00aa1b2c)
- ブロック [`00aa1b2c`](#insn-00aa1b2c) 範囲 `[['00aa1b2c', '00aa1b2f']]`
  - `FALL_THROUGH` [`00aa1b2c`](#insn-00aa1b2c) → [`00aa1b30`](#insn-00aa1b30)
- ブロック [`00aa1b30`](#insn-00aa1b30) 範囲 `[['00aa1b30', '00aa1b33']]`
  - `FALL_THROUGH` [`00aa1b30`](#insn-00aa1b30) → [`00aa1b34`](#insn-00aa1b34)
- ブロック [`00aa1b34`](#insn-00aa1b34) 範囲 `[['00aa1b34', '00aa1b37']]`
  - `FALL_THROUGH` [`00aa1b34`](#insn-00aa1b34) → [`00aa1b38`](#insn-00aa1b38)
- ブロック [`00aa1b38`](#insn-00aa1b38) 範囲 `[['00aa1b38', '00aa1b3b']]`
  - `FALL_THROUGH` [`00aa1b38`](#insn-00aa1b38) → [`00aa1b3c`](#insn-00aa1b3c)
- ブロック [`00aa1b3c`](#insn-00aa1b3c) 範囲 `[['00aa1b3c', '00aa1b3f']]`

## 命令位置別の参照

- [`00aa1aac`](#insn-00aa1aac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ab0`](#insn-00aa1ab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ab4`](#insn-00aa1ab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ac8`](#insn-00aa1ac8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1adc`](#insn-00aa1adc) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ae0`](#insn-00aa1ae0) → [`00aa1aec`](#insn-00aa1aec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1ae8`](#insn-00aa1ae8) → [`00aa1b14`](#insn-00aa1b14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1aec`](#insn-00aa1aec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b0c`](#insn-00aa1b0c) → [`00aa1b24`](#insn-00aa1b24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b14`](#insn-00aa1b14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b18`](#insn-00aa1b18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b1c`](#insn-00aa1b1c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b30`](#insn-00aa1b30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b34`](#insn-00aa1b34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b38`](#insn-00aa1b38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b3c`](#insn-00aa1b3c) → [`00aa2c70`](../00aa2/00aa2c70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1aac`](#insn-00aa1aac)

~~~json
{
  "source": "00aa1aac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ab0`](#insn-00aa1ab0)

~~~json
{
  "source": "00aa1ab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ab4`](#insn-00aa1ab4)

~~~json
{
  "source": "00aa1ab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ac8`](#insn-00aa1ac8)

~~~json
{
  "source": "00aa1ac8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1adc`](#insn-00aa1adc)

~~~json
{
  "source": "00aa1adc",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1ae0`](#insn-00aa1ae0)

~~~json
{
  "source": "00aa1ae0",
  "target": "00aa1aec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1ae8`](#insn-00aa1ae8)

~~~json
{
  "source": "00aa1ae8",
  "target": "00aa1b14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1aec`](#insn-00aa1aec)

~~~json
{
  "source": "00aa1aec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1b0c`](#insn-00aa1b0c)

~~~json
{
  "source": "00aa1b0c",
  "target": "00aa1b24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b14`](#insn-00aa1b14)

~~~json
{
  "source": "00aa1b14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b18`](#insn-00aa1b18)

~~~json
{
  "source": "00aa1b18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b1c`](#insn-00aa1b1c)

~~~json
{
  "source": "00aa1b1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b30`](#insn-00aa1b30)

~~~json
{
  "source": "00aa1b30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b34`](#insn-00aa1b34)

~~~json
{
  "source": "00aa1b34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b38`](#insn-00aa1b38)

~~~json
{
  "source": "00aa1b38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b3c`](#insn-00aa1b3c)

~~~json
{
  "source": "00aa1b3c",
  "target": "00aa2c70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
