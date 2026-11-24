# 00affbc0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00affb7c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affb7c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-a94aae1171bda0584d2b00431a3b8628)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5f944`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5f/00b5f944.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0061.md#compare-e99c231cd00b986c200c203e31a066c9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affbc0",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f5f8c341bb802da606a6ac9b2aee797874514b1a88c455042cedfaab4f98b5d",
  "source_text_sha256": "1f5f8c341bb802da606a6ac9b2aee797874514b1a88c455042cedfaab4f98b5d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affbc0",
        "00affc7f"
      ]
    ],
    "bytes_sha256": "215253ea598c020c410be606a088d8b0899deab7c93bd877e6ebd99666863345",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)

## 関連文字列（未確認候補）

~~~text
"Invalid Future"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2330 bytes

~~~c

undefined *
_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  undefined *puVar5;
  long lVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af5cf4 with catch @ 00affbc8 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5ce8 with catch @ 00affbd4 */
                    /* catch() { ... } // from try @ 00af5cdc with catch @ 00affbe0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5cd0 with catch @ 00affbec */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af5c78 with catch @ 00affc04 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5c6c with catch @ 00affc1c */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b9b0;
      if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5c3c with catch @ 00affc64 */
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
                    /* catch() { ... } // from try @ 00af5c30 with catch @ 00affc70 */
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affc38;
    }
  }
                    /* catch() { ... } // from try @ 00af5c60 with catch @ 00affc28 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b9b0;
LAB_00affc38:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5c54 with catch @ 00affc40 */
                    /* catch() { ... } // from try @ 00af5c48 with catch @ 00affc4c */
  return puVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affbc0"></a> `00affbc0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affbc4"></a> `00affbc4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affbc8"></a> `00affbc8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affbcc"></a> `00affbcc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affbd0"></a> `00affbd0` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affbd4"></a> `00affbd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affbd8"></a> `00affbd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affbdc"></a> `00affbdc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affbe0"></a> `00affbe0` | `10 78 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00affbe4"></a> `00affbe4` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affbe8"></a> `00affbe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affbec"></a> `00affbec` | `0d 78 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00affbf0"></a> `00affbf0` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affbf4"></a> `00affbf4` | `a9 01 00 b4` | cbz x9,0x00affc28 | `CONDITIONAL_JUMP`
<a id="insn-00affbf8"></a> `00affbf8` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affbfc"></a> `00affbfc` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affc00"></a> `00affc00` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affc04"></a> `00affc04` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affc08"></a> `00affc08` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affc0c"></a> `00affc0c` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affc10"></a> `00affc10` | `69 ff ff b5` | cbnz x9,0x00affbfc | `CONDITIONAL_JUMP`
<a id="insn-00affc14"></a> `00affc14` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affc18"></a> `00affc18` | `80 00 00 54` | b.eq 0x00affc28 | `CONDITIONAL_JUMP`
<a id="insn-00affc1c"></a> `00affc1c` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affc20"></a> `00affc20` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affc24"></a> `00affc24` | `89 01 00 54` | b.ls 0x00affc54 | `CONDITIONAL_JUMP`
<a id="insn-00affc28"></a> `00affc28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc2c"></a> `00affc2c` | `01 78 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00affc30"></a> `00affc30` | `f4 08 00 90` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00affc34"></a> `00affc34` | `94 da 44 f9` | ldr x20,[x20, #0x9b0] | `FALL_THROUGH`
<a id="insn-00affc38"></a> `00affc38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc3c"></a> `00affc3c` | `fd 77 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00affc40"></a> `00affc40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00affc44"></a> `00affc44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affc48"></a> `00affc48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affc4c"></a> `00affc4c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affc50"></a> `00affc50` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affc54"></a> `00affc54` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affc58"></a> `00affc58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc5c"></a> `00affc5c` | `f5 77 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00affc60"></a> `00affc60` | `94 fe ff b4` | cbz x20,0x00affc30 | `CONDITIONAL_JUMP`
<a id="insn-00affc64"></a> `00affc64` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affc68"></a> `00affc68` | `09 8d 40 38` | ldrb w9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00affc6c"></a> `00affc6c` | `69 00 00 37` | tbnz w9,#0x0,0x00affc78 | `CONDITIONAL_JUMP`
<a id="insn-00affc70"></a> `00affc70` | `14 05 00 91` | add x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00affc74"></a> `00affc74` | `f1 ff ff 17` | b 0x00affc38 | `UNCONDITIONAL_JUMP`
<a id="insn-00affc78"></a> `00affc78` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00affc7c"></a> `00affc7c` | `ef ff ff 17` | b 0x00affc38 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affbc0`](#insn-00affbc0) 範囲 `[['00affbc0', '00affbc7']]`
  - `FALL_THROUGH` [`00affbc4`](#insn-00affbc4) → [`00affbc8`](#insn-00affbc8)
- ブロック [`00affbc8`](#insn-00affbc8) 範囲 `[['00affbc8', '00affbd3']]`
  - `FALL_THROUGH` [`00affbd0`](#insn-00affbd0) → [`00affbd4`](#insn-00affbd4)
- ブロック [`00affbd4`](#insn-00affbd4) 範囲 `[['00affbd4', '00affbdf']]`
  - `FALL_THROUGH` [`00affbdc`](#insn-00affbdc) → [`00affbe0`](#insn-00affbe0)
- ブロック [`00affbe0`](#insn-00affbe0) 範囲 `[['00affbe0', '00affbeb']]`
  - `FALL_THROUGH` [`00affbe8`](#insn-00affbe8) → [`00affbec`](#insn-00affbec)
- ブロック [`00affbec`](#insn-00affbec) 範囲 `[['00affbec', '00affbf7']]`
  - `CONDITIONAL_JUMP` [`00affbf4`](#insn-00affbf4) → [`00affc28`](#insn-00affc28)
  - `FALL_THROUGH` [`00affbf4`](#insn-00affbf4) → [`00affbf8`](#insn-00affbf8)
- ブロック [`00affbf8`](#insn-00affbf8) 範囲 `[['00affbf8', '00affbfb']]`
  - `FALL_THROUGH` [`00affbf8`](#insn-00affbf8) → [`00affbfc`](#insn-00affbfc)
- ブロック [`00affbfc`](#insn-00affbfc) 範囲 `[['00affbfc', '00affc03']]`
  - `FALL_THROUGH` [`00affc00`](#insn-00affc00) → [`00affc04`](#insn-00affc04)
- ブロック [`00affc04`](#insn-00affc04) 範囲 `[['00affc04', '00affc13']]`
  - `CONDITIONAL_JUMP` [`00affc10`](#insn-00affc10) → [`00affbfc`](#insn-00affbfc)
  - `FALL_THROUGH` [`00affc10`](#insn-00affc10) → [`00affc14`](#insn-00affc14)
- ブロック [`00affc14`](#insn-00affc14) 範囲 `[['00affc14', '00affc1b']]`
  - `CONDITIONAL_JUMP` [`00affc18`](#insn-00affc18) → [`00affc28`](#insn-00affc28)
  - `FALL_THROUGH` [`00affc18`](#insn-00affc18) → [`00affc1c`](#insn-00affc1c)
- ブロック [`00affc1c`](#insn-00affc1c) 範囲 `[['00affc1c', '00affc27']]`
  - `CONDITIONAL_JUMP` [`00affc24`](#insn-00affc24) → [`00affc54`](#insn-00affc54)
  - `FALL_THROUGH` [`00affc24`](#insn-00affc24) → [`00affc28`](#insn-00affc28)
- ブロック [`00affc28`](#insn-00affc28) 範囲 `[['00affc28', '00affc2f']]`
  - `FALL_THROUGH` [`00affc2c`](#insn-00affc2c) → [`00affc30`](#insn-00affc30)
- ブロック [`00affc30`](#insn-00affc30) 範囲 `[['00affc30', '00affc37']]`
  - `FALL_THROUGH` [`00affc34`](#insn-00affc34) → [`00affc38`](#insn-00affc38)
- ブロック [`00affc38`](#insn-00affc38) 範囲 `[['00affc38', '00affc3f']]`
  - `FALL_THROUGH` [`00affc3c`](#insn-00affc3c) → [`00affc40`](#insn-00affc40)
- ブロック [`00affc40`](#insn-00affc40) 範囲 `[['00affc40', '00affc4b']]`
  - `FALL_THROUGH` [`00affc48`](#insn-00affc48) → [`00affc4c`](#insn-00affc4c)
- ブロック [`00affc4c`](#insn-00affc4c) 範囲 `[['00affc4c', '00affc53']]`
- ブロック [`00affc54`](#insn-00affc54) 範囲 `[['00affc54', '00affc63']]`
  - `CONDITIONAL_JUMP` [`00affc60`](#insn-00affc60) → [`00affc30`](#insn-00affc30)
  - `FALL_THROUGH` [`00affc60`](#insn-00affc60) → [`00affc64`](#insn-00affc64)
- ブロック [`00affc64`](#insn-00affc64) 範囲 `[['00affc64', '00affc6f']]`
  - `CONDITIONAL_JUMP` [`00affc6c`](#insn-00affc6c) → [`00affc78`](#insn-00affc78)
  - `FALL_THROUGH` [`00affc6c`](#insn-00affc6c) → [`00affc70`](#insn-00affc70)
- ブロック [`00affc70`](#insn-00affc70) 範囲 `[['00affc70', '00affc77']]`
  - `UNCONDITIONAL_JUMP` [`00affc74`](#insn-00affc74) → [`00affc38`](#insn-00affc38)
- ブロック [`00affc78`](#insn-00affc78) 範囲 `[['00affc78', '00affc7f']]`
  - `UNCONDITIONAL_JUMP` [`00affc7c`](#insn-00affc7c) → [`00affc38`](#insn-00affc38)

## 命令位置別の参照

- [`00affbc0`](#insn-00affbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbc4`](#insn-00affbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbc8`](#insn-00affbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbe0`](#insn-00affbe0) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00affbec`](#insn-00affbec) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00affbf4`](#insn-00affbf4) → [`00affc28`](#insn-00affc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc10`](#insn-00affc10) → [`00affbfc`](#insn-00affbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc18`](#insn-00affc18) → [`00affc28`](#insn-00affc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc24`](#insn-00affc24) → [`00affc54`](#insn-00affc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc2c`](#insn-00affc2c) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00affc34`](#insn-00affc34) → `00c1b9b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00affc3c`](#insn-00affc3c) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00affc40`](#insn-00affc40) → `002f5fdc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE` · 推定型 `string`
- [`00affc44`](#insn-00affc44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc48`](#insn-00affc48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc5c`](#insn-00affc5c) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00affc60`](#insn-00affc60) → [`00affc30`](#insn-00affc30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc6c`](#insn-00affc6c) → [`00affc78`](#insn-00affc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc74`](#insn-00affc74) → [`00affc38`](#insn-00affc38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc7c`](#insn-00affc7c) → [`00affc38`](#insn-00affc38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affbc0`](#insn-00affbc0)

~~~json
{
  "source": "00affbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbc4`](#insn-00affbc4)

~~~json
{
  "source": "00affbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbc8`](#insn-00affbc8)

~~~json
{
  "source": "00affbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbe0`](#insn-00affbe0)

~~~json
{
  "source": "00affbe0",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbec`](#insn-00affbec)

~~~json
{
  "source": "00affbec",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbf4`](#insn-00affbf4)

~~~json
{
  "source": "00affbf4",
  "target": "00affc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc10`](#insn-00affc10)

~~~json
{
  "source": "00affc10",
  "target": "00affbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc18`](#insn-00affc18)

~~~json
{
  "source": "00affc18",
  "target": "00affc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc24`](#insn-00affc24)

~~~json
{
  "source": "00affc24",
  "target": "00affc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc2c`](#insn-00affc2c)

~~~json
{
  "source": "00affc2c",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc34`](#insn-00affc34)

~~~json
{
  "source": "00affc34",
  "target": "00c1b9b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b9b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00affc3c`](#insn-00affc3c)

~~~json
{
  "source": "00affc3c",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc40`](#insn-00affc40)

~~~json
{
  "source": "00affc40",
  "target": "002f5fdc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f5fdc",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "496e76616c69642046757475726500",
  "capture_start": "002f5fdc",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00affc44`](#insn-00affc44)

~~~json
{
  "source": "00affc44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc48`](#insn-00affc48)

~~~json
{
  "source": "00affc48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc5c`](#insn-00affc5c)

~~~json
{
  "source": "00affc5c",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc60`](#insn-00affc60)

~~~json
{
  "source": "00affc60",
  "target": "00affc30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc6c`](#insn-00affc6c)

~~~json
{
  "source": "00affc6c",
  "target": "00affc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc74`](#insn-00affc74)

~~~json
{
  "source": "00affc74",
  "target": "00affc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc7c`](#insn-00affc7c)

~~~json
{
  "source": "00affc7c",
  "target": "00affc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
