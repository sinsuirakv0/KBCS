# 00affb7c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00affab4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affab4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-41a7b82178fd0992ea9832ba2faae5b5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affbc0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affbc0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-a94aae1171bda0584d2b00431a3b8628)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affb7c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "935deff46d6ce643a92565a3a7bbf9c6424c28034bd0c2630e73c7cc14548ad6",
  "source_text_sha256": "935deff46d6ce643a92565a3a7bbf9c6424c28034bd0c2630e73c7cc14548ad6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affb7c",
        "00affc3b"
      ]
    ],
    "bytes_sha256": "614fe9c981090cac06e378539ebf03b11e95b6b2e739c3853aa7747b4337001e",
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

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

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
  
                    /* catch() { ... } // from try @ 00af5cb0 with catch @ 00affb84 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5ca4 with catch @ 00affb90 */
                    /* catch() { ... } // from try @ 00af5c98 with catch @ 00affb9c */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5c8c with catch @ 00affba8 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af5c34 with catch @ 00affbc0 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5c28 with catch @ 00affbd8 */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b960;
      if (lVar6 != 0) {
                    /* catch() { ... } // from try @ 00af5bf8 with catch @ 00affc20 */
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
                    /* catch() { ... } // from try @ 00af5bec with catch @ 00affc2c */
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affbf4;
    }
  }
                    /* catch() { ... } // from try @ 00af5c1c with catch @ 00affbe4 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b960;
LAB_00affbf4:
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5c10 with catch @ 00affbfc */
                    /* catch() { ... } // from try @ 00af5c04 with catch @ 00affc08 */
  return puVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affb7c"></a> `00affb7c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affb80"></a> `00affb80` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affb84"></a> `00affb84` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affb88"></a> `00affb88` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affb8c"></a> `00affb8c` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affb90"></a> `00affb90` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affb94"></a> `00affb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb98"></a> `00affb98` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affb9c"></a> `00affb9c` | `0d 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affba0"></a> `00affba0` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affba4"></a> `00affba4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affba8"></a> `00affba8` | `0a 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affbac"></a> `00affbac` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affbb0"></a> `00affbb0` | `a9 01 00 b4` | cbz x9,0x00affbe4 | `CONDITIONAL_JUMP`
<a id="insn-00affbb4"></a> `00affbb4` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affbb8"></a> `00affbb8` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affbbc"></a> `00affbbc` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affbc0"></a> `00affbc0` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affbc4"></a> `00affbc4` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affbc8"></a> `00affbc8` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affbcc"></a> `00affbcc` | `69 ff ff b5` | cbnz x9,0x00affbb8 | `CONDITIONAL_JUMP`
<a id="insn-00affbd0"></a> `00affbd0` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affbd4"></a> `00affbd4` | `80 00 00 54` | b.eq 0x00affbe4 | `CONDITIONAL_JUMP`
<a id="insn-00affbd8"></a> `00affbd8` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affbdc"></a> `00affbdc` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affbe0"></a> `00affbe0` | `89 01 00 54` | b.ls 0x00affc10 | `CONDITIONAL_JUMP`
<a id="insn-00affbe4"></a> `00affbe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affbe8"></a> `00affbe8` | `fe 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affbec"></a> `00affbec` | `f4 08 00 90` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00affbf0"></a> `00affbf0` | `94 b2 44 f9` | ldr x20,[x20, #0x960] | `FALL_THROUGH`
<a id="insn-00affbf4"></a> `00affbf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affbf8"></a> `00affbf8` | `fa 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affbfc"></a> `00affbfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00affc00"></a> `00affc00` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affc04"></a> `00affc04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affc08"></a> `00affc08` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affc0c"></a> `00affc0c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affc10"></a> `00affc10` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affc14"></a> `00affc14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc18"></a> `00affc18` | `f2 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affc1c"></a> `00affc1c` | `94 fe ff b4` | cbz x20,0x00affbec | `CONDITIONAL_JUMP`
<a id="insn-00affc20"></a> `00affc20` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affc24"></a> `00affc24` | `09 8d 40 38` | ldrb w9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00affc28"></a> `00affc28` | `69 00 00 37` | tbnz w9,#0x0,0x00affc34 | `CONDITIONAL_JUMP`
<a id="insn-00affc2c"></a> `00affc2c` | `14 05 00 91` | add x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00affc30"></a> `00affc30` | `f1 ff ff 17` | b 0x00affbf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00affc34"></a> `00affc34` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00affc38"></a> `00affc38` | `ef ff ff 17` | b 0x00affbf4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affb7c`](#insn-00affb7c) 範囲 `[['00affb7c', '00affb83']]`
  - `FALL_THROUGH` [`00affb80`](#insn-00affb80) → [`00affb84`](#insn-00affb84)
- ブロック [`00affb84`](#insn-00affb84) 範囲 `[['00affb84', '00affb8f']]`
  - `FALL_THROUGH` [`00affb8c`](#insn-00affb8c) → [`00affb90`](#insn-00affb90)
- ブロック [`00affb90`](#insn-00affb90) 範囲 `[['00affb90', '00affb9b']]`
  - `FALL_THROUGH` [`00affb98`](#insn-00affb98) → [`00affb9c`](#insn-00affb9c)
- ブロック [`00affb9c`](#insn-00affb9c) 範囲 `[['00affb9c', '00affba7']]`
  - `FALL_THROUGH` [`00affba4`](#insn-00affba4) → [`00affba8`](#insn-00affba8)
- ブロック [`00affba8`](#insn-00affba8) 範囲 `[['00affba8', '00affbb3']]`
  - `CONDITIONAL_JUMP` [`00affbb0`](#insn-00affbb0) → [`00affbe4`](#insn-00affbe4)
  - `FALL_THROUGH` [`00affbb0`](#insn-00affbb0) → [`00affbb4`](#insn-00affbb4)
- ブロック [`00affbb4`](#insn-00affbb4) 範囲 `[['00affbb4', '00affbb7']]`
  - `FALL_THROUGH` [`00affbb4`](#insn-00affbb4) → [`00affbb8`](#insn-00affbb8)
- ブロック [`00affbb8`](#insn-00affbb8) 範囲 `[['00affbb8', '00affbbf']]`
  - `FALL_THROUGH` [`00affbbc`](#insn-00affbbc) → [`00affbc0`](#insn-00affbc0)
- ブロック [`00affbc0`](#insn-00affbc0) 範囲 `[['00affbc0', '00affbcf']]`
  - `CONDITIONAL_JUMP` [`00affbcc`](#insn-00affbcc) → [`00affbb8`](#insn-00affbb8)
  - `FALL_THROUGH` [`00affbcc`](#insn-00affbcc) → [`00affbd0`](#insn-00affbd0)
- ブロック [`00affbd0`](#insn-00affbd0) 範囲 `[['00affbd0', '00affbd7']]`
  - `CONDITIONAL_JUMP` [`00affbd4`](#insn-00affbd4) → [`00affbe4`](#insn-00affbe4)
  - `FALL_THROUGH` [`00affbd4`](#insn-00affbd4) → [`00affbd8`](#insn-00affbd8)
- ブロック [`00affbd8`](#insn-00affbd8) 範囲 `[['00affbd8', '00affbe3']]`
  - `CONDITIONAL_JUMP` [`00affbe0`](#insn-00affbe0) → [`00affc10`](#insn-00affc10)
  - `FALL_THROUGH` [`00affbe0`](#insn-00affbe0) → [`00affbe4`](#insn-00affbe4)
- ブロック [`00affbe4`](#insn-00affbe4) 範囲 `[['00affbe4', '00affbeb']]`
  - `FALL_THROUGH` [`00affbe8`](#insn-00affbe8) → [`00affbec`](#insn-00affbec)
- ブロック [`00affbec`](#insn-00affbec) 範囲 `[['00affbec', '00affbf3']]`
  - `FALL_THROUGH` [`00affbf0`](#insn-00affbf0) → [`00affbf4`](#insn-00affbf4)
- ブロック [`00affbf4`](#insn-00affbf4) 範囲 `[['00affbf4', '00affbfb']]`
  - `FALL_THROUGH` [`00affbf8`](#insn-00affbf8) → [`00affbfc`](#insn-00affbfc)
- ブロック [`00affbfc`](#insn-00affbfc) 範囲 `[['00affbfc', '00affc07']]`
  - `FALL_THROUGH` [`00affc04`](#insn-00affc04) → [`00affc08`](#insn-00affc08)
- ブロック [`00affc08`](#insn-00affc08) 範囲 `[['00affc08', '00affc0f']]`
- ブロック [`00affc10`](#insn-00affc10) 範囲 `[['00affc10', '00affc1f']]`
  - `CONDITIONAL_JUMP` [`00affc1c`](#insn-00affc1c) → [`00affbec`](#insn-00affbec)
  - `FALL_THROUGH` [`00affc1c`](#insn-00affc1c) → [`00affc20`](#insn-00affc20)
- ブロック [`00affc20`](#insn-00affc20) 範囲 `[['00affc20', '00affc2b']]`
  - `CONDITIONAL_JUMP` [`00affc28`](#insn-00affc28) → [`00affc34`](#insn-00affc34)
  - `FALL_THROUGH` [`00affc28`](#insn-00affc28) → [`00affc2c`](#insn-00affc2c)
- ブロック [`00affc2c`](#insn-00affc2c) 範囲 `[['00affc2c', '00affc33']]`
  - `UNCONDITIONAL_JUMP` [`00affc30`](#insn-00affc30) → [`00affbf4`](#insn-00affbf4)
- ブロック [`00affc34`](#insn-00affc34) 範囲 `[['00affc34', '00affc3b']]`
  - `UNCONDITIONAL_JUMP` [`00affc38`](#insn-00affc38) → [`00affbf4`](#insn-00affbf4)

## 命令位置別の参照

- [`00affb7c`](#insn-00affb7c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb80`](#insn-00affb80) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb84`](#insn-00affb84) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb9c`](#insn-00affb9c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affba8`](#insn-00affba8) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affbb0`](#insn-00affbb0) → [`00affbe4`](#insn-00affbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbcc`](#insn-00affbcc) → [`00affbb8`](#insn-00affbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbd4`](#insn-00affbd4) → [`00affbe4`](#insn-00affbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbe0`](#insn-00affbe0) → [`00affc10`](#insn-00affc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affbe8`](#insn-00affbe8) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affbf0`](#insn-00affbf0) → `00c1b960`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00affbf8`](#insn-00affbf8) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affbfc`](#insn-00affbfc) → `002f5fdc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE` · 推定型 `string`
- [`00affc00`](#insn-00affc00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc04`](#insn-00affc04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc18`](#insn-00affc18) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affc1c`](#insn-00affc1c) → [`00affbec`](#insn-00affbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc28`](#insn-00affc28) → [`00affc34`](#insn-00affc34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc30`](#insn-00affc30) → [`00affbf4`](#insn-00affbf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc38`](#insn-00affc38) → [`00affbf4`](#insn-00affbf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affb7c`](#insn-00affb7c)

~~~json
{
  "source": "00affb7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb80`](#insn-00affb80)

~~~json
{
  "source": "00affb80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb84`](#insn-00affb84)

~~~json
{
  "source": "00affb84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb9c`](#insn-00affb9c)

~~~json
{
  "source": "00affb9c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affba8`](#insn-00affba8)

~~~json
{
  "source": "00affba8",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbb0`](#insn-00affbb0)

~~~json
{
  "source": "00affbb0",
  "target": "00affbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbcc`](#insn-00affbcc)

~~~json
{
  "source": "00affbcc",
  "target": "00affbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbd4`](#insn-00affbd4)

~~~json
{
  "source": "00affbd4",
  "target": "00affbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbe0`](#insn-00affbe0)

~~~json
{
  "source": "00affbe0",
  "target": "00affc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affbe8`](#insn-00affbe8)

~~~json
{
  "source": "00affbe8",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbf0`](#insn-00affbf0)

~~~json
{
  "source": "00affbf0",
  "target": "00c1b960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b960",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00affbf8`](#insn-00affbf8)

~~~json
{
  "source": "00affbf8",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affbfc`](#insn-00affbfc)

~~~json
{
  "source": "00affbfc",
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
- 参照命令 [`00affc00`](#insn-00affc00)

~~~json
{
  "source": "00affc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc04`](#insn-00affc04)

~~~json
{
  "source": "00affc04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc18`](#insn-00affc18)

~~~json
{
  "source": "00affc18",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc1c`](#insn-00affc1c)

~~~json
{
  "source": "00affc1c",
  "target": "00affbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc28`](#insn-00affc28)

~~~json
{
  "source": "00affc28",
  "target": "00affc34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc30`](#insn-00affc30)

~~~json
{
  "source": "00affc30",
  "target": "00affbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc38`](#insn-00affc38)

~~~json
{
  "source": "00affc38",
  "target": "00affbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
