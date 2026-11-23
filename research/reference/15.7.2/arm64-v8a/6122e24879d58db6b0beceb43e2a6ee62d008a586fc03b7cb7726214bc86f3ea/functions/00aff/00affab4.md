# 00affab4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00affb7c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aff/00affb7c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-41a7b82178fd0992ea9832ba2faae5b5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affab4",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl21GetFutureErrorMessageERKNS_12FutureHandleE",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "991fcb4e75c099f43faceeab9951db384533d3d2510038e55bed70d8394ea4dc",
  "source_text_sha256": "991fcb4e75c099f43faceeab9951db384533d3d2510038e55bed70d8394ea4dc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affab4",
        "00affb73"
      ]
    ],
    "bytes_sha256": "931429dd7deed93723208abd90215a4cbe8243d77843f8e384a8ad283d0b4161",
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

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 関連文字列（未確認候補）

~~~text
"Invalid Future"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2852 bytes

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
  
                    /* catch() { ... } // from try @ 00af60a4 with catch @ 00affabc */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af6094 with catch @ 00affac8 */
                    /* catch() { ... } // from try @ 00af6078 with catch @ 00affad0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af6068 with catch @ 00affad8 */
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6058 with catch @ 00affae0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
                    /* catch() { ... } // from try @ 00af6048 with catch @ 00affae8 */
  plVar2 = plVar4;
  if (plVar3 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00af6038 with catch @ 00affaf0 */
                    /* catch() { ... } // from try @ 00af6028 with catch @ 00affaf8 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
                    /* catch() { ... } // from try @ 00af6000 with catch @ 00affb00 */
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5ff0 with catch @ 00affb08 */
                    /* catch() { ... } // from try @ 00af5ee8 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00af5d5c with catch @ 00affb18 */
    if ((plVar2 != plVar4) && ((ulong)plVar2[4] <= uVar7)) {
                    /* catch() { ... } // from try @ 00af5ce0 with catch @ 00affb48 */
      lVar6 = plVar2[5];
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5cd4 with catch @ 00affb54 */
      puVar5 = 
      PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b8b0;
      if (lVar6 != 0) {
        if ((*(byte *)(lVar6 + 8) & 1) == 0) {
          puVar5 = (undefined *)(lVar6 + 9);
        }
        else {
                    /* catch() { ... } // from try @ 00af5cc8 with catch @ 00affb6c */
          puVar5 = *(undefined **)(lVar6 + 0x18);
        }
      }
      goto LAB_00affb2c;
    }
  }
                    /* catch() { ... } // from try @ 00af5d20 with catch @ 00affb20 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  puVar5 = 
  PTR__ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE_00c1b8b0;
LAB_00affb2c:
                    /* catch() { ... } // from try @ 00af5cec with catch @ 00affb30 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  return puVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affab4"></a> `00affab4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affab8"></a> `00affab8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affabc"></a> `00affabc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affac0"></a> `00affac0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affac4"></a> `00affac4` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affac8"></a> `00affac8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affacc"></a> `00affacc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affad0"></a> `00affad0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affad4"></a> `00affad4` | `13 78 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affad8"></a> `00affad8` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affadc"></a> `00affadc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affae0"></a> `00affae0` | `10 78 03 94` | bl 0x00bddb20 | `UNCONDITIONAL_CALL`
<a id="insn-00affae4"></a> `00affae4` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affae8"></a> `00affae8` | `a9 01 00 b4` | cbz x9,0x00affb1c | `CONDITIONAL_JUMP`
<a id="insn-00affaec"></a> `00affaec` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affaf0"></a> `00affaf0` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affaf4"></a> `00affaf4` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affaf8"></a> `00affaf8` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affafc"></a> `00affafc` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affb00"></a> `00affb00` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affb04"></a> `00affb04` | `69 ff ff b5` | cbnz x9,0x00affaf0 | `CONDITIONAL_JUMP`
<a id="insn-00affb08"></a> `00affb08` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affb0c"></a> `00affb0c` | `80 00 00 54` | b.eq 0x00affb1c | `CONDITIONAL_JUMP`
<a id="insn-00affb10"></a> `00affb10` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affb14"></a> `00affb14` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affb18"></a> `00affb18` | `89 01 00 54` | b.ls 0x00affb48 | `CONDITIONAL_JUMP`
<a id="insn-00affb1c"></a> `00affb1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb20"></a> `00affb20` | `04 78 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affb24"></a> `00affb24` | `f4 08 00 90` | adrp x20,0xc1b000 | `FALL_THROUGH`
<a id="insn-00affb28"></a> `00affb28` | `94 5a 44 f9` | ldr x20,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00affb2c"></a> `00affb2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb30"></a> `00affb30` | `00 78 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affb34"></a> `00affb34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00affb38"></a> `00affb38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affb3c"></a> `00affb3c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affb40"></a> `00affb40` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affb44"></a> `00affb44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affb48"></a> `00affb48` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affb4c"></a> `00affb4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb50"></a> `00affb50` | `f8 77 03 94` | bl 0x00bddb30 | `UNCONDITIONAL_CALL`
<a id="insn-00affb54"></a> `00affb54` | `94 fe ff b4` | cbz x20,0x00affb24 | `CONDITIONAL_JUMP`
<a id="insn-00affb58"></a> `00affb58` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affb5c"></a> `00affb5c` | `09 8d 40 38` | ldrb w9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00affb60"></a> `00affb60` | `69 00 00 37` | tbnz w9,#0x0,0x00affb6c | `CONDITIONAL_JUMP`
<a id="insn-00affb64"></a> `00affb64` | `14 05 00 91` | add x20,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00affb68"></a> `00affb68` | `f1 ff ff 17` | b 0x00affb2c | `UNCONDITIONAL_JUMP`
<a id="insn-00affb6c"></a> `00affb6c` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00affb70"></a> `00affb70` | `ef ff ff 17` | b 0x00affb2c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affab4`](#insn-00affab4) 範囲 `[['00affab4', '00affabb']]`
  - `FALL_THROUGH` [`00affab8`](#insn-00affab8) → [`00affabc`](#insn-00affabc)
- ブロック [`00affabc`](#insn-00affabc) 範囲 `[['00affabc', '00affac7']]`
  - `FALL_THROUGH` [`00affac4`](#insn-00affac4) → [`00affac8`](#insn-00affac8)
- ブロック [`00affac8`](#insn-00affac8) 範囲 `[['00affac8', '00affacf']]`
  - `FALL_THROUGH` [`00affacc`](#insn-00affacc) → [`00affad0`](#insn-00affad0)
- ブロック [`00affad0`](#insn-00affad0) 範囲 `[['00affad0', '00affad7']]`
  - `FALL_THROUGH` [`00affad4`](#insn-00affad4) → [`00affad8`](#insn-00affad8)
- ブロック [`00affad8`](#insn-00affad8) 範囲 `[['00affad8', '00affadf']]`
  - `FALL_THROUGH` [`00affadc`](#insn-00affadc) → [`00affae0`](#insn-00affae0)
- ブロック [`00affae0`](#insn-00affae0) 範囲 `[['00affae0', '00affae7']]`
  - `FALL_THROUGH` [`00affae4`](#insn-00affae4) → [`00affae8`](#insn-00affae8)
- ブロック [`00affae8`](#insn-00affae8) 範囲 `[['00affae8', '00affaeb']]`
  - `CONDITIONAL_JUMP` [`00affae8`](#insn-00affae8) → [`00affb1c`](#insn-00affb1c)
  - `FALL_THROUGH` [`00affae8`](#insn-00affae8) → [`00affaec`](#insn-00affaec)
- ブロック [`00affaec`](#insn-00affaec) 範囲 `[['00affaec', '00affaef']]`
  - `FALL_THROUGH` [`00affaec`](#insn-00affaec) → [`00affaf0`](#insn-00affaf0)
- ブロック [`00affaf0`](#insn-00affaf0) 範囲 `[['00affaf0', '00affaf7']]`
  - `FALL_THROUGH` [`00affaf4`](#insn-00affaf4) → [`00affaf8`](#insn-00affaf8)
- ブロック [`00affaf8`](#insn-00affaf8) 範囲 `[['00affaf8', '00affaff']]`
  - `FALL_THROUGH` [`00affafc`](#insn-00affafc) → [`00affb00`](#insn-00affb00)
- ブロック [`00affb00`](#insn-00affb00) 範囲 `[['00affb00', '00affb07']]`
  - `CONDITIONAL_JUMP` [`00affb04`](#insn-00affb04) → [`00affaf0`](#insn-00affaf0)
  - `FALL_THROUGH` [`00affb04`](#insn-00affb04) → [`00affb08`](#insn-00affb08)
- ブロック [`00affb08`](#insn-00affb08) 範囲 `[['00affb08', '00affb0f']]`
  - `CONDITIONAL_JUMP` [`00affb0c`](#insn-00affb0c) → [`00affb1c`](#insn-00affb1c)
  - `FALL_THROUGH` [`00affb0c`](#insn-00affb0c) → [`00affb10`](#insn-00affb10)
- ブロック [`00affb10`](#insn-00affb10) 範囲 `[['00affb10', '00affb17']]`
  - `FALL_THROUGH` [`00affb14`](#insn-00affb14) → [`00affb18`](#insn-00affb18)
- ブロック [`00affb18`](#insn-00affb18) 範囲 `[['00affb18', '00affb1b']]`
  - `CONDITIONAL_JUMP` [`00affb18`](#insn-00affb18) → [`00affb48`](#insn-00affb48)
  - `FALL_THROUGH` [`00affb18`](#insn-00affb18) → [`00affb1c`](#insn-00affb1c)
- ブロック [`00affb1c`](#insn-00affb1c) 範囲 `[['00affb1c', '00affb1f']]`
  - `FALL_THROUGH` [`00affb1c`](#insn-00affb1c) → [`00affb20`](#insn-00affb20)
- ブロック [`00affb20`](#insn-00affb20) 範囲 `[['00affb20', '00affb23']]`
  - `FALL_THROUGH` [`00affb20`](#insn-00affb20) → [`00affb24`](#insn-00affb24)
- ブロック [`00affb24`](#insn-00affb24) 範囲 `[['00affb24', '00affb27']]`
  - `FALL_THROUGH` [`00affb24`](#insn-00affb24) → [`00affb28`](#insn-00affb28)
- ブロック [`00affb28`](#insn-00affb28) 範囲 `[['00affb28', '00affb2b']]`
  - `FALL_THROUGH` [`00affb28`](#insn-00affb28) → [`00affb2c`](#insn-00affb2c)
- ブロック [`00affb2c`](#insn-00affb2c) 範囲 `[['00affb2c', '00affb2f']]`
  - `FALL_THROUGH` [`00affb2c`](#insn-00affb2c) → [`00affb30`](#insn-00affb30)
- ブロック [`00affb30`](#insn-00affb30) 範囲 `[['00affb30', '00affb47']]`
- ブロック [`00affb48`](#insn-00affb48) 範囲 `[['00affb48', '00affb53']]`
  - `FALL_THROUGH` [`00affb50`](#insn-00affb50) → [`00affb54`](#insn-00affb54)
- ブロック [`00affb54`](#insn-00affb54) 範囲 `[['00affb54', '00affb57']]`
  - `CONDITIONAL_JUMP` [`00affb54`](#insn-00affb54) → [`00affb24`](#insn-00affb24)
  - `FALL_THROUGH` [`00affb54`](#insn-00affb54) → [`00affb58`](#insn-00affb58)
- ブロック [`00affb58`](#insn-00affb58) 範囲 `[['00affb58', '00affb63']]`
  - `CONDITIONAL_JUMP` [`00affb60`](#insn-00affb60) → [`00affb6c`](#insn-00affb6c)
  - `FALL_THROUGH` [`00affb60`](#insn-00affb60) → [`00affb64`](#insn-00affb64)
- ブロック [`00affb64`](#insn-00affb64) 範囲 `[['00affb64', '00affb6b']]`
  - `UNCONDITIONAL_JUMP` [`00affb68`](#insn-00affb68) → [`00affb2c`](#insn-00affb2c)
- ブロック [`00affb6c`](#insn-00affb6c) 範囲 `[['00affb6c', '00affb73']]`
  - `UNCONDITIONAL_JUMP` [`00affb70`](#insn-00affb70) → [`00affb2c`](#insn-00affb2c)

## 命令位置別の参照

- [`00affab4`](#insn-00affab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affab8`](#insn-00affab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affabc`](#insn-00affabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affad4`](#insn-00affad4) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affae0`](#insn-00affae0) → [`00bddb20`](../00bdd/00bddb20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb20` · 推定シンボル `None` · 推定型 `None`
- [`00affae8`](#insn-00affae8) → [`00affb1c`](#insn-00affb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb04`](#insn-00affb04) → [`00affaf0`](#insn-00affaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb0c`](#insn-00affb0c) → [`00affb1c`](#insn-00affb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb18`](#insn-00affb18) → [`00affb48`](#insn-00affb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb20`](#insn-00affb20) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affb28`](#insn-00affb28) → `00c1b8b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00affb30`](#insn-00affb30) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affb34`](#insn-00affb34) → `002f5fdc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl34kErrorMessageFutureIsNoLongerValidE` · 推定型 `string`
- [`00affb38`](#insn-00affb38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb3c`](#insn-00affb3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb50`](#insn-00affb50) → [`00bddb30`](../00bdd/00bddb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddb30` · 推定シンボル `None` · 推定型 `None`
- [`00affb54`](#insn-00affb54) → [`00affb24`](#insn-00affb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb60`](#insn-00affb60) → [`00affb6c`](#insn-00affb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb68`](#insn-00affb68) → [`00affb2c`](#insn-00affb2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb70`](#insn-00affb70) → [`00affb2c`](#insn-00affb2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affab4`](#insn-00affab4)

~~~json
{
  "source": "00affab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affab8`](#insn-00affab8)

~~~json
{
  "source": "00affab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affabc`](#insn-00affabc)

~~~json
{
  "source": "00affabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affad4`](#insn-00affad4)

~~~json
{
  "source": "00affad4",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affae0`](#insn-00affae0)

~~~json
{
  "source": "00affae0",
  "target": "00bddb20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affae8`](#insn-00affae8)

~~~json
{
  "source": "00affae8",
  "target": "00affb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb04`](#insn-00affb04)

~~~json
{
  "source": "00affb04",
  "target": "00affaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb0c`](#insn-00affb0c)

~~~json
{
  "source": "00affb0c",
  "target": "00affb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb18`](#insn-00affb18)

~~~json
{
  "source": "00affb18",
  "target": "00affb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb20`](#insn-00affb20)

~~~json
{
  "source": "00affb20",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb28`](#insn-00affb28)

~~~json
{
  "source": "00affb28",
  "target": "00c1b8b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b8b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00affb30`](#insn-00affb30)

~~~json
{
  "source": "00affb30",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb34`](#insn-00affb34)

~~~json
{
  "source": "00affb34",
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
- 参照命令 [`00affb38`](#insn-00affb38)

~~~json
{
  "source": "00affb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb3c`](#insn-00affb3c)

~~~json
{
  "source": "00affb3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb50`](#insn-00affb50)

~~~json
{
  "source": "00affb50",
  "target": "00bddb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb54`](#insn-00affb54)

~~~json
{
  "source": "00affb54",
  "target": "00affb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb60`](#insn-00affb60)

~~~json
{
  "source": "00affb60",
  "target": "00affb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb68`](#insn-00affb68)

~~~json
{
  "source": "00affb68",
  "target": "00affb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb70`](#insn-00affb70)

~~~json
{
  "source": "00affb70",
  "target": "00affb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
