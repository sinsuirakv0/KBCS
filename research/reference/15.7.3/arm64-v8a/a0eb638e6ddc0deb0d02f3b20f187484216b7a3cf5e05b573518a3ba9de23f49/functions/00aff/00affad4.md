# 00affad4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00affa0c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affa0c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-81308fddcb1696b40a330a381c6b0dd4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affb18`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affb18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-acaa4a11a348302bc1cd9ffb7ef3d355)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affad4",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1837549c645d27ffa23ed9d041f1f4635943f5b2a86e9581de77c54214664a39",
  "source_text_sha256": "1837549c645d27ffa23ed9d041f1f4635943f5b2a86e9581de77c54214664a39",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affad4",
        "00affb7b"
      ]
    ],
    "bytes_sha256": "32100b7dc3bd7136072cc4861cec7cec5ac98f376bdb8daadba30bfcff634d94",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2453 bytes

~~~c

undefined4
_ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined4 uVar4;
  long *plVar5;
  long lVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af6068 with catch @ 00affad8 */
                    /* catch() { ... } // from try @ 00af6058 with catch @ 00affae0 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af6048 with catch @ 00affae8 */
                    /* catch() { ... } // from try @ 00af6038 with catch @ 00affaf0 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
                    /* catch() { ... } // from try @ 00af6028 with catch @ 00affaf8 */
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af6000 with catch @ 00affb00 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar5 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar5;
                    /* catch() { ... } // from try @ 00af5ff0 with catch @ 00affb08 */
  plVar2 = plVar5;
  if (plVar3 == (long *)0x0) {
LAB_00affb3c:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
                    /* catch() { ... } // from try @ 00af5ee8 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00af5d5c with catch @ 00affb18 */
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
                    /* catch() { ... } // from try @ 00af5d20 with catch @ 00affb20 */
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5cf8 with catch @ 00affb28 */
                    /* catch() { ... } // from try @ 00af5cec with catch @ 00affb30 */
    if ((plVar2 == plVar5) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affb3c;
    lVar6 = plVar2[5];
                    /* catch() { ... } // from try @ 00af5cc8 with catch @ 00affb6c */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    if (lVar6 != 0) {
      uVar4 = *(undefined4 *)(lVar6 + 4);
                    /* catch() { ... } // from try @ 00af5cbc with catch @ 00affb78 */
      goto LAB_00affb48;
    }
  }
  uVar4 = 0xffffffff;
LAB_00affb48:
                    /* catch() { ... } // from try @ 00af5ce0 with catch @ 00affb48 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5cd4 with catch @ 00affb54 */
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affad4"></a> `00affad4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affad8"></a> `00affad8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affadc"></a> `00affadc` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affae0"></a> `00affae0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affae4"></a> `00affae4` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affae8"></a> `00affae8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affaec"></a> `00affaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affaf0"></a> `00affaf0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affaf4"></a> `00affaf4` | `37 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affaf8"></a> `00affaf8` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affafc"></a> `00affafc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb00"></a> `00affb00` | `34 78 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affb04"></a> `00affb04` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affb08"></a> `00affb08` | `a9 01 00 b4` | cbz x9,0x00affb3c | `CONDITIONAL_JUMP`
<a id="insn-00affb0c"></a> `00affb0c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affb10"></a> `00affb10` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affb14"></a> `00affb14` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affb18"></a> `00affb18` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affb1c"></a> `00affb1c` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affb20"></a> `00affb20` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affb24"></a> `00affb24` | `69 ff ff b5` | cbnz x9,0x00affb10 | `CONDITIONAL_JUMP`
<a id="insn-00affb28"></a> `00affb28` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affb2c"></a> `00affb2c` | `80 00 00 54` | b.eq 0x00affb3c | `CONDITIONAL_JUMP`
<a id="insn-00affb30"></a> `00affb30` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affb34"></a> `00affb34` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affb38"></a> `00affb38` | `69 01 00 54` | b.ls 0x00affb64 | `CONDITIONAL_JUMP`
<a id="insn-00affb3c"></a> `00affb3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb40"></a> `00affb40` | `28 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affb44"></a> `00affb44` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00affb48"></a> `00affb48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb4c"></a> `00affb4c` | `25 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affb50"></a> `00affb50` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00affb54"></a> `00affb54` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affb58"></a> `00affb58` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affb5c"></a> `00affb5c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affb60"></a> `00affb60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affb64"></a> `00affb64` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affb68"></a> `00affb68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affb6c"></a> `00affb6c` | `1d 78 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affb70"></a> `00affb70` | `b4 fe ff b4` | cbz x20,0x00affb44 | `CONDITIONAL_JUMP`
<a id="insn-00affb74"></a> `00affb74` | `94 06 40 b9` | ldr w20,[x20, #0x4] | `FALL_THROUGH`
<a id="insn-00affb78"></a> `00affb78` | `f4 ff ff 17` | b 0x00affb48 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affad4`](#insn-00affad4) 範囲 `[['00affad4', '00affad7']]`
  - `FALL_THROUGH` [`00affad4`](#insn-00affad4) → [`00affad8`](#insn-00affad8)
- ブロック [`00affad8`](#insn-00affad8) 範囲 `[['00affad8', '00affadf']]`
  - `FALL_THROUGH` [`00affadc`](#insn-00affadc) → [`00affae0`](#insn-00affae0)
- ブロック [`00affae0`](#insn-00affae0) 範囲 `[['00affae0', '00affae7']]`
  - `FALL_THROUGH` [`00affae4`](#insn-00affae4) → [`00affae8`](#insn-00affae8)
- ブロック [`00affae8`](#insn-00affae8) 範囲 `[['00affae8', '00affaef']]`
  - `FALL_THROUGH` [`00affaec`](#insn-00affaec) → [`00affaf0`](#insn-00affaf0)
- ブロック [`00affaf0`](#insn-00affaf0) 範囲 `[['00affaf0', '00affaf7']]`
  - `FALL_THROUGH` [`00affaf4`](#insn-00affaf4) → [`00affaf8`](#insn-00affaf8)
- ブロック [`00affaf8`](#insn-00affaf8) 範囲 `[['00affaf8', '00affaff']]`
  - `FALL_THROUGH` [`00affafc`](#insn-00affafc) → [`00affb00`](#insn-00affb00)
- ブロック [`00affb00`](#insn-00affb00) 範囲 `[['00affb00', '00affb07']]`
  - `FALL_THROUGH` [`00affb04`](#insn-00affb04) → [`00affb08`](#insn-00affb08)
- ブロック [`00affb08`](#insn-00affb08) 範囲 `[['00affb08', '00affb0b']]`
  - `CONDITIONAL_JUMP` [`00affb08`](#insn-00affb08) → [`00affb3c`](#insn-00affb3c)
  - `FALL_THROUGH` [`00affb08`](#insn-00affb08) → [`00affb0c`](#insn-00affb0c)
- ブロック [`00affb0c`](#insn-00affb0c) 範囲 `[['00affb0c', '00affb0f']]`
  - `FALL_THROUGH` [`00affb0c`](#insn-00affb0c) → [`00affb10`](#insn-00affb10)
- ブロック [`00affb10`](#insn-00affb10) 範囲 `[['00affb10', '00affb17']]`
  - `FALL_THROUGH` [`00affb14`](#insn-00affb14) → [`00affb18`](#insn-00affb18)
- ブロック [`00affb18`](#insn-00affb18) 範囲 `[['00affb18', '00affb1f']]`
  - `FALL_THROUGH` [`00affb1c`](#insn-00affb1c) → [`00affb20`](#insn-00affb20)
- ブロック [`00affb20`](#insn-00affb20) 範囲 `[['00affb20', '00affb27']]`
  - `CONDITIONAL_JUMP` [`00affb24`](#insn-00affb24) → [`00affb10`](#insn-00affb10)
  - `FALL_THROUGH` [`00affb24`](#insn-00affb24) → [`00affb28`](#insn-00affb28)
- ブロック [`00affb28`](#insn-00affb28) 範囲 `[['00affb28', '00affb2f']]`
  - `CONDITIONAL_JUMP` [`00affb2c`](#insn-00affb2c) → [`00affb3c`](#insn-00affb3c)
  - `FALL_THROUGH` [`00affb2c`](#insn-00affb2c) → [`00affb30`](#insn-00affb30)
- ブロック [`00affb30`](#insn-00affb30) 範囲 `[['00affb30', '00affb3b']]`
  - `CONDITIONAL_JUMP` [`00affb38`](#insn-00affb38) → [`00affb64`](#insn-00affb64)
  - `FALL_THROUGH` [`00affb38`](#insn-00affb38) → [`00affb3c`](#insn-00affb3c)
- ブロック [`00affb3c`](#insn-00affb3c) 範囲 `[['00affb3c', '00affb43']]`
  - `FALL_THROUGH` [`00affb40`](#insn-00affb40) → [`00affb44`](#insn-00affb44)
- ブロック [`00affb44`](#insn-00affb44) 範囲 `[['00affb44', '00affb47']]`
  - `FALL_THROUGH` [`00affb44`](#insn-00affb44) → [`00affb48`](#insn-00affb48)
- ブロック [`00affb48`](#insn-00affb48) 範囲 `[['00affb48', '00affb53']]`
  - `FALL_THROUGH` [`00affb50`](#insn-00affb50) → [`00affb54`](#insn-00affb54)
- ブロック [`00affb54`](#insn-00affb54) 範囲 `[['00affb54', '00affb63']]`
- ブロック [`00affb64`](#insn-00affb64) 範囲 `[['00affb64', '00affb6b']]`
  - `FALL_THROUGH` [`00affb68`](#insn-00affb68) → [`00affb6c`](#insn-00affb6c)
- ブロック [`00affb6c`](#insn-00affb6c) 範囲 `[['00affb6c', '00affb73']]`
  - `CONDITIONAL_JUMP` [`00affb70`](#insn-00affb70) → [`00affb44`](#insn-00affb44)
  - `FALL_THROUGH` [`00affb70`](#insn-00affb70) → [`00affb74`](#insn-00affb74)
- ブロック [`00affb74`](#insn-00affb74) 範囲 `[['00affb74', '00affb77']]`
  - `FALL_THROUGH` [`00affb74`](#insn-00affb74) → [`00affb78`](#insn-00affb78)
- ブロック [`00affb78`](#insn-00affb78) 範囲 `[['00affb78', '00affb7b']]`
  - `UNCONDITIONAL_JUMP` [`00affb78`](#insn-00affb78) → [`00affb48`](#insn-00affb48)

## 命令位置別の参照

- [`00affad4`](#insn-00affad4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affad8`](#insn-00affad8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affadc`](#insn-00affadc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affaf4`](#insn-00affaf4) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affb00`](#insn-00affb00) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affb08`](#insn-00affb08) → [`00affb3c`](#insn-00affb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb24`](#insn-00affb24) → [`00affb10`](#insn-00affb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb2c`](#insn-00affb2c) → [`00affb3c`](#insn-00affb3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb38`](#insn-00affb38) → [`00affb64`](#insn-00affb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb40`](#insn-00affb40) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affb4c`](#insn-00affb4c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affb54`](#insn-00affb54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb58`](#insn-00affb58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb6c`](#insn-00affb6c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affb70`](#insn-00affb70) → [`00affb44`](#insn-00affb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb78`](#insn-00affb78) → [`00affb48`](#insn-00affb48) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affad4`](#insn-00affad4)

~~~json
{
  "source": "00affad4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affad8`](#insn-00affad8)

~~~json
{
  "source": "00affad8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affadc`](#insn-00affadc)

~~~json
{
  "source": "00affadc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affaf4`](#insn-00affaf4)

~~~json
{
  "source": "00affaf4",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb00`](#insn-00affb00)

~~~json
{
  "source": "00affb00",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb08`](#insn-00affb08)

~~~json
{
  "source": "00affb08",
  "target": "00affb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb24`](#insn-00affb24)

~~~json
{
  "source": "00affb24",
  "target": "00affb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb2c`](#insn-00affb2c)

~~~json
{
  "source": "00affb2c",
  "target": "00affb3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb38`](#insn-00affb38)

~~~json
{
  "source": "00affb38",
  "target": "00affb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb40`](#insn-00affb40)

~~~json
{
  "source": "00affb40",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb4c`](#insn-00affb4c)

~~~json
{
  "source": "00affb4c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb54`](#insn-00affb54)

~~~json
{
  "source": "00affb54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb58`](#insn-00affb58)

~~~json
{
  "source": "00affb58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb6c`](#insn-00affb6c)

~~~json
{
  "source": "00affb6c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb70`](#insn-00affb70)

~~~json
{
  "source": "00affb70",
  "target": "00affb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb78`](#insn-00affb78)

~~~json
{
  "source": "00affb78",
  "target": "00affb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
