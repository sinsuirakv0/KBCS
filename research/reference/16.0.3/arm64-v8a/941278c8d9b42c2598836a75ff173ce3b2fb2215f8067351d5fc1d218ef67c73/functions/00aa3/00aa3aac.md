# 00aa3aac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aa2ab8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aa2/00aa2ab8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-4a14c613b9d48cee076776e19e377018)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa3aac",
  "name": "FUN_00aa3aac",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db867518f3ae7ef51d647a048bccefb0f593acb2590ad5284e61256279c6c820",
  "source_text_sha256": "db867518f3ae7ef51d647a048bccefb0f593acb2590ad5284e61256279c6c820",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa3aac",
        "00aa3b5f"
      ]
    ],
    "bytes_sha256": "0bda600cb1dd1fab045d569f9bb360c13ddc7db1ee1d443a3ed815a26a3d18f7",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a2c310](../00a2c/00a2c310.md)

## 呼び出し先

- [00480e98](../00480/00480e98.md)
- [00480ef0](../00480/00480ef0.md)
- [00480f48](../00480/00480f48.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2605 bytes

~~~c

void FUN_00aa3aac(long param_1,undefined8 param_2)

{
  undefined4 uVar1;
  long lVar2;
  long *plVar3;
  bool bVar4;
  long *plVar5;
  long *plVar6;
  
                    /* catch() { ... } // from try @ 00aa2674 with catch @ 00aa3ab0 */
                    /* catch() { ... } // from try @ 00aa3614 with catch @ 00aa3ab8
                       catch() { ... } // from try @ 00aa37d0 with catch @ 00aa3ab8
                       catch() { ... } // from try @ 00aa384c with catch @ 00aa3ab8 */
                    /* catch() { ... } // from try @ 00aa350c with catch @ 00aa3ac0
                       catch() { ... } // from try @ 00aa37b4 with catch @ 00aa3ac0
                       catch() { ... } // from try @ 00aa3834 with catch @ 00aa3ac0 */
                    /* catch() { ... } // from try @ 00aa29ec with catch @ 00aa3ac8
                       catch() { ... } // from try @ 00aa3798 with catch @ 00aa3ac8
                       catch() { ... } // from try @ 00aa381c with catch @ 00aa3ac8 */
                    /* catch() { ... } // from try @ 00aa28e4 with catch @ 00aa3ad0
                       catch() { ... } // from try @ 00aa377c with catch @ 00aa3ad0
                       catch() { ... } // from try @ 00aa3804 with catch @ 00aa3ad0 */
  FUN_00480ef0(param_2,*(undefined2 *)(param_1 + 0x28));
                    /* catch() { ... } // from try @ 00aa2774 with catch @ 00aa3ad8
                       catch() { ... } // from try @ 00aa3760 with catch @ 00aa3ad8
                       catch() { ... } // from try @ 00aa37ec with catch @ 00aa3ad8 */
  plVar5 = *(long **)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 00aa36d4 with catch @ 00aa3ae0 */
                    /* catch() { ... } // from try @ 00aa2650 with catch @ 00aa3ae4 */
  while (plVar5 != (long *)(param_1 + 0x20)) {
    lVar2 = plVar5[4];
    uVar1 = *(undefined4 *)((long)plVar5 + 0x24);
    FUN_00480f48(param_2,*(undefined4 *)((long)plVar5 + 0x1c));
    FUN_00480e98(param_2,(int)lVar2);
    FUN_00480e98(param_2,uVar1);
    plVar3 = (long *)plVar5[1];
    plVar6 = plVar5;
    if ((long *)plVar5[1] == (long *)0x0) {
      do {
        plVar5 = (long *)plVar6[2];
        bVar4 = (long *)*plVar5 != plVar6;
        plVar6 = plVar5;
      } while (bVar4);
    }
    else {
      do {
        plVar5 = plVar3;
        plVar3 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
    }
  }
                    /* catch() { ... } // from try @ 00aa36b0 with catch @ 00aa3aec
                       catch() { ... } // from try @ 00aa3744 with catch @ 00aa3aec */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa3aac"></a> `00aa3aac` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aa3ab0"></a> `00aa3ab0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3ab4"></a> `00aa3ab4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3ab8"></a> `00aa3ab8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa3abc"></a> `00aa3abc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa3ac0"></a> `00aa3ac0` | `08 50 40 79` | ldrh w8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aa3ac4"></a> `00aa3ac4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa3ac8"></a> `00aa3ac8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aa3acc"></a> `00aa3acc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aa3ad0"></a> `00aa3ad0` | `e1 03 08 2a` | mov w1,w8 | `FALL_THROUGH`
<a id="insn-00aa3ad4"></a> `00aa3ad4` | `07 75 e7 97` | bl 0x00480ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3ad8"></a> `00aa3ad8` | `97 0e 40 f9` | ldr x23,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00aa3adc"></a> `00aa3adc` | `96 82 00 91` | add x22,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00aa3ae0"></a> `00aa3ae0` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00aa3ae4"></a> `00aa3ae4` | `21 01 00 54` | b.ne 0x00aa3b08 | `CONDITIONAL_JUMP`
<a id="insn-00aa3ae8"></a> `00aa3ae8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa3aec"></a> `00aa3aec` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3af0"></a> `00aa3af0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa3af4"></a> `00aa3af4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aa3af8"></a> `00aa3af8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa3afc"></a> `00aa3afc` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00aa3b00"></a> `00aa3b00` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00aa3b04"></a> `00aa3b04` | `20 ff ff 54` | b.eq 0x00aa3ae8 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b08"></a> `00aa3b08` | `e1 d2 43 29` | ldp w1,w20,[x23, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa3b0c"></a> `00aa3b0c` | `f5 26 40 b9` | ldr w21,[x23, #0x24] | `FALL_THROUGH`
<a id="insn-00aa3b10"></a> `00aa3b10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa3b14"></a> `00aa3b14` | `0d 75 e7 97` | bl 0x00480f48 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b18"></a> `00aa3b18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa3b1c"></a> `00aa3b1c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa3b20"></a> `00aa3b20` | `de 74 e7 97` | bl 0x00480e98 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b24"></a> `00aa3b24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa3b28"></a> `00aa3b28` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00aa3b2c"></a> `00aa3b2c` | `db 74 e7 97` | bl 0x00480e98 | `UNCONDITIONAL_CALL`
<a id="insn-00aa3b30"></a> `00aa3b30` | `e9 06 40 f9` | ldr x9,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00aa3b34"></a> `00aa3b34` | `a9 00 00 b4` | cbz x9,0x00aa3b48 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b38"></a> `00aa3b38` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aa3b3c"></a> `00aa3b3c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aa3b40"></a> `00aa3b40` | `c9 ff ff b5` | cbnz x9,0x00aa3b38 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b44"></a> `00aa3b44` | `ee ff ff 17` | b 0x00aa3afc | `UNCONDITIONAL_JUMP`
<a id="insn-00aa3b48"></a> `00aa3b48` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00aa3b4c"></a> `00aa3b4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00aa3b50"></a> `00aa3b50` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00aa3b54"></a> `00aa3b54` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00aa3b58"></a> `00aa3b58` | `81 ff ff 54` | b.ne 0x00aa3b48 | `CONDITIONAL_JUMP`
<a id="insn-00aa3b5c"></a> `00aa3b5c` | `e8 ff ff 17` | b 0x00aa3afc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aa3aac`](#insn-00aa3aac) 範囲 `[['00aa3aac', '00aa3aaf']]`
  - `FALL_THROUGH` [`00aa3aac`](#insn-00aa3aac) → [`00aa3ab0`](#insn-00aa3ab0)
- ブロック [`00aa3ab0`](#insn-00aa3ab0) 範囲 `[['00aa3ab0', '00aa3ab7']]`
  - `FALL_THROUGH` [`00aa3ab4`](#insn-00aa3ab4) → [`00aa3ab8`](#insn-00aa3ab8)
- ブロック [`00aa3ab8`](#insn-00aa3ab8) 範囲 `[['00aa3ab8', '00aa3abf']]`
  - `FALL_THROUGH` [`00aa3abc`](#insn-00aa3abc) → [`00aa3ac0`](#insn-00aa3ac0)
- ブロック [`00aa3ac0`](#insn-00aa3ac0) 範囲 `[['00aa3ac0', '00aa3ac7']]`
  - `FALL_THROUGH` [`00aa3ac4`](#insn-00aa3ac4) → [`00aa3ac8`](#insn-00aa3ac8)
- ブロック [`00aa3ac8`](#insn-00aa3ac8) 範囲 `[['00aa3ac8', '00aa3acf']]`
  - `FALL_THROUGH` [`00aa3acc`](#insn-00aa3acc) → [`00aa3ad0`](#insn-00aa3ad0)
- ブロック [`00aa3ad0`](#insn-00aa3ad0) 範囲 `[['00aa3ad0', '00aa3ad7']]`
  - `FALL_THROUGH` [`00aa3ad4`](#insn-00aa3ad4) → [`00aa3ad8`](#insn-00aa3ad8)
- ブロック [`00aa3ad8`](#insn-00aa3ad8) 範囲 `[['00aa3ad8', '00aa3adf']]`
  - `FALL_THROUGH` [`00aa3adc`](#insn-00aa3adc) → [`00aa3ae0`](#insn-00aa3ae0)
- ブロック [`00aa3ae0`](#insn-00aa3ae0) 範囲 `[['00aa3ae0', '00aa3ae3']]`
  - `FALL_THROUGH` [`00aa3ae0`](#insn-00aa3ae0) → [`00aa3ae4`](#insn-00aa3ae4)
- ブロック [`00aa3ae4`](#insn-00aa3ae4) 範囲 `[['00aa3ae4', '00aa3ae7']]`
  - `CONDITIONAL_JUMP` [`00aa3ae4`](#insn-00aa3ae4) → [`00aa3b08`](#insn-00aa3b08)
  - `FALL_THROUGH` [`00aa3ae4`](#insn-00aa3ae4) → [`00aa3ae8`](#insn-00aa3ae8)
- ブロック [`00aa3ae8`](#insn-00aa3ae8) 範囲 `[['00aa3ae8', '00aa3aeb']]`
  - `FALL_THROUGH` [`00aa3ae8`](#insn-00aa3ae8) → [`00aa3aec`](#insn-00aa3aec)
- ブロック [`00aa3aec`](#insn-00aa3aec) 範囲 `[['00aa3aec', '00aa3afb']]`
- ブロック [`00aa3afc`](#insn-00aa3afc) 範囲 `[['00aa3afc', '00aa3b07']]`
  - `CONDITIONAL_JUMP` [`00aa3b04`](#insn-00aa3b04) → [`00aa3ae8`](#insn-00aa3ae8)
  - `FALL_THROUGH` [`00aa3b04`](#insn-00aa3b04) → [`00aa3b08`](#insn-00aa3b08)
- ブロック [`00aa3b08`](#insn-00aa3b08) 範囲 `[['00aa3b08', '00aa3b37']]`
  - `CONDITIONAL_JUMP` [`00aa3b34`](#insn-00aa3b34) → [`00aa3b48`](#insn-00aa3b48)
  - `FALL_THROUGH` [`00aa3b34`](#insn-00aa3b34) → [`00aa3b38`](#insn-00aa3b38)
- ブロック [`00aa3b38`](#insn-00aa3b38) 範囲 `[['00aa3b38', '00aa3b43']]`
  - `CONDITIONAL_JUMP` [`00aa3b40`](#insn-00aa3b40) → [`00aa3b38`](#insn-00aa3b38)
  - `FALL_THROUGH` [`00aa3b40`](#insn-00aa3b40) → [`00aa3b44`](#insn-00aa3b44)
- ブロック [`00aa3b44`](#insn-00aa3b44) 範囲 `[['00aa3b44', '00aa3b47']]`
  - `UNCONDITIONAL_JUMP` [`00aa3b44`](#insn-00aa3b44) → [`00aa3afc`](#insn-00aa3afc)
- ブロック [`00aa3b48`](#insn-00aa3b48) 範囲 `[['00aa3b48', '00aa3b5b']]`
  - `CONDITIONAL_JUMP` [`00aa3b58`](#insn-00aa3b58) → [`00aa3b48`](#insn-00aa3b48)
  - `FALL_THROUGH` [`00aa3b58`](#insn-00aa3b58) → [`00aa3b5c`](#insn-00aa3b5c)
- ブロック [`00aa3b5c`](#insn-00aa3b5c) 範囲 `[['00aa3b5c', '00aa3b5f']]`
  - `UNCONDITIONAL_JUMP` [`00aa3b5c`](#insn-00aa3b5c) → [`00aa3afc`](#insn-00aa3afc)

## 命令位置別の参照

- [`00aa3aac`](#insn-00aa3aac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ab0`](#insn-00aa3ab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ab4`](#insn-00aa3ab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ab8`](#insn-00aa3ab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ad4`](#insn-00aa3ad4) → [`00480ef0`](../00480/00480ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480ef0` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ae4`](#insn-00aa3ae4) → [`00aa3b08`](#insn-00aa3b08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3ae8`](#insn-00aa3ae8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3aec`](#insn-00aa3aec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3af0`](#insn-00aa3af0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3af4`](#insn-00aa3af4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b04`](#insn-00aa3b04) → [`00aa3ae8`](#insn-00aa3ae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b14`](#insn-00aa3b14) → [`00480f48`](../00480/00480f48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480f48` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b20`](#insn-00aa3b20) → [`00480e98`](../00480/00480e98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e98` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b2c`](#insn-00aa3b2c) → [`00480e98`](../00480/00480e98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00480e98` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b34`](#insn-00aa3b34) → [`00aa3b48`](#insn-00aa3b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b40`](#insn-00aa3b40) → [`00aa3b38`](#insn-00aa3b38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b44`](#insn-00aa3b44) → [`00aa3afc`](#insn-00aa3afc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b58`](#insn-00aa3b58) → [`00aa3b48`](#insn-00aa3b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa3b5c`](#insn-00aa3b5c) → [`00aa3afc`](#insn-00aa3afc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa3aac`](#insn-00aa3aac)

~~~json
{
  "source": "00aa3aac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ab0`](#insn-00aa3ab0)

~~~json
{
  "source": "00aa3ab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ab4`](#insn-00aa3ab4)

~~~json
{
  "source": "00aa3ab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ab8`](#insn-00aa3ab8)

~~~json
{
  "source": "00aa3ab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ad4`](#insn-00aa3ad4)

~~~json
{
  "source": "00aa3ad4",
  "target": "00480ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3ae4`](#insn-00aa3ae4)

~~~json
{
  "source": "00aa3ae4",
  "target": "00aa3b08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3ae8`](#insn-00aa3ae8)

~~~json
{
  "source": "00aa3ae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3aec`](#insn-00aa3aec)

~~~json
{
  "source": "00aa3aec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3af0`](#insn-00aa3af0)

~~~json
{
  "source": "00aa3af0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3af4`](#insn-00aa3af4)

~~~json
{
  "source": "00aa3af4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b04`](#insn-00aa3b04)

~~~json
{
  "source": "00aa3b04",
  "target": "00aa3ae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b14`](#insn-00aa3b14)

~~~json
{
  "source": "00aa3b14",
  "target": "00480f48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b20`](#insn-00aa3b20)

~~~json
{
  "source": "00aa3b20",
  "target": "00480e98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b2c`](#insn-00aa3b2c)

~~~json
{
  "source": "00aa3b2c",
  "target": "00480e98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa3b34`](#insn-00aa3b34)

~~~json
{
  "source": "00aa3b34",
  "target": "00aa3b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b40`](#insn-00aa3b40)

~~~json
{
  "source": "00aa3b40",
  "target": "00aa3b38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b44`](#insn-00aa3b44)

~~~json
{
  "source": "00aa3b44",
  "target": "00aa3afc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b58`](#insn-00aa3b58)

~~~json
{
  "source": "00aa3b58",
  "target": "00aa3b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa3b5c`](#insn-00aa3b5c)

~~~json
{
  "source": "00aa3b5c",
  "target": "00aa3afc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
