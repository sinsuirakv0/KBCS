# 00aebdb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0014.md#review-7aa544ba0c61f53466d809289f847e7d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aec1e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec1e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-b58e7a861ca7c885ff83af6490e47170)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebdb8",
  "name": "FUN_00aebdb8",
  "size": 204,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ebd3e7e2221ab26b57a973964953e92bf1c6bc5505b99593ce4d2e7aad65ce85",
  "source_text_sha256": "ebd3e7e2221ab26b57a973964953e92bf1c6bc5505b99593ce4d2e7aad65ce85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebdb8",
        "00aebe83"
      ]
    ],
    "bytes_sha256": "33a91c8901707c4afc58013c7f53a1079fe31ca5b6190fb24b77f41774a88126",
    "instruction_count": 51,
    "instruction_bytes": 204,
    "body_bytes": 204,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00adf01c](../00adf/00adf01c.md)

## 呼び出し先

- [0043bb64](../0043b/0043bb64.md)
- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2908 bytes

~~~c

long * FUN_00aebdb8(long *param_1,int *param_2)

{
  int iVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  
                    /* catch() { ... } // from try @ 00aeb3d4 with catch @ 00aebdc4 */
  iVar1 = *param_2;
  plVar4 = param_1 + 1;
                    /* catch() { ... } // from try @ 00aeb554 with catch @ 00aebddc */
  plVar3 = (long *)*plVar4;
  plVar5 = plVar4;
  if ((long *)*plVar4 != (long *)0x0) {
    do {
                    /* catch() { ... } // from try @ 00aeb458 with catch @ 00aebdf4 */
      while (plVar2 = plVar3, plVar4 = plVar2, iVar1 < (int)plVar2[4]) {
                    /* catch() { ... } // from try @ 00aeb4ec with catch @ 00aebdec */
        plVar3 = (long *)*plVar2;
        plVar5 = plVar2;
        if ((long *)*plVar2 == (long *)0x0) goto LAB_00aebe18;
      }
                    /* catch() { ... } // from try @ 00aeb3c4 with catch @ 00aebe04 */
      if (iVar1 <= (int)plVar2[4]) goto LAB_00aebe6c;
      plVar3 = (long *)plVar2[1];
    } while ((long *)plVar2[1] != (long *)0x0);
                    /* catch() { ... } // from try @ 00aeb6d0 with catch @ 00aebe14 */
    plVar5 = plVar2 + 1;
  }
LAB_00aebe18:
                    /* catch() { ... } // from try @ 00aeb4fc with catch @ 00aebe18 */
  plVar2 = (long *)_Znwm(0x40);
  plVar2[6] = 0;
  plVar2[7] = 0;
  plVar2[5] = 0;
  *plVar2 = 0;
  plVar2[1] = 0;
                    /* catch() { ... } // from try @ 00aebbc0 with catch @ 00aebe38 */
  plVar2[2] = (long)plVar4;
                    /* catch() { ... } // from try @ 00aebb58 with catch @ 00aebe3c */
  *plVar5 = (long)plVar2;
                    /* catch() { ... } // from try @ 00aebaf4 with catch @ 00aebe40 */
  plVar4 = (long *)*param_1;
                    /* catch() { ... } // from try @ 00aeb348 with catch @ 00aebe44 */
  *(int *)(plVar2 + 4) = iVar1;
                    /* catch() { ... } // from try @ 00aeb274 with catch @ 00aebe48 */
  plVar3 = plVar2;
  if (*plVar4 != 0) {
                    /* catch() { ... } // from try @ 00aeb1ec with catch @ 00aebe50 */
    *param_1 = *plVar4;
                    /* catch() { ... } // from try @ 00aeb108 with catch @ 00aebe54 */
    plVar3 = (long *)*plVar5;
  }
                    /* catch() { ... } // from try @ 00aeb2b8 with catch @ 00aebe5c
                       catch() { ... } // from try @ 00aebc54 with catch @ 00aebe5c */
  FUN_0043bb64(param_1[1],plVar3);
                    /* catch() { ... } // from try @ 00aeb064 with catch @ 00aebe60 */
  param_1[2] = param_1[2] + 1;
LAB_00aebe6c:
                    /* catch() { ... } // from try @ 00aeaf8c with catch @ 00aebe74 */
                    /* catch() { ... } // from try @ 00aeb14c with catch @ 00aebe7c
                       catch() { ... } // from try @ 00aebc40 with catch @ 00aebe7c */
                    /* catch() { ... } // from try @ 00aeaf24 with catch @ 00aebe80 */
  return plVar2 + 5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebdb8"></a> `00aebdb8` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00aebdbc"></a> `00aebdbc` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdc0"></a> `00aebdc0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebdc4"></a> `00aebdc4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aebdc8"></a> `00aebdc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aebdcc"></a> `00aebdcc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aebdd0"></a> `00aebdd0` | `35 00 40 b9` | ldr w21,[x1] | `FALL_THROUGH`
<a id="insn-00aebdd4"></a> `00aebdd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebdd8"></a> `00aebdd8` | `c8 8e 40 f8` | ldr x8,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-00aebddc"></a> `00aebddc` | `c8 00 00 b5` | cbnz x8,0x00aebdf4 | `CONDITIONAL_JUMP`
<a id="insn-00aebde0"></a> `00aebde0` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aebde4"></a> `00aebde4` | `0d 00 00 14` | b 0x00aebe18 | `UNCONDITIONAL_JUMP`
<a id="insn-00aebde8"></a> `00aebde8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aebdec"></a> `00aebdec` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00aebdf0"></a> `00aebdf0` | `48 01 00 b4` | cbz x8,0x00aebe18 | `CONDITIONAL_JUMP`
<a id="insn-00aebdf4"></a> `00aebdf4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aebdf8"></a> `00aebdf8` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aebdfc"></a> `00aebdfc` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00aebe00"></a> `00aebe00` | `4b ff ff 54` | b.lt 0x00aebde8 | `CONDITIONAL_JUMP`
<a id="insn-00aebe04"></a> `00aebe04` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00aebe08"></a> `00aebe08` | `2a 03 00 54` | b.ge 0x00aebe6c | `CONDITIONAL_JUMP`
<a id="insn-00aebe0c"></a> `00aebe0c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aebe10"></a> `00aebe10` | `28 ff ff b5` | cbnz x8,0x00aebdf4 | `CONDITIONAL_JUMP`
<a id="insn-00aebe14"></a> `00aebe14` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aebe18"></a> `00aebe18` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aebe1c"></a> `00aebe1c` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00aebe20"></a> `00aebe20` | `1c af 05 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe24"></a> `00aebe24` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aebe28"></a> `00aebe28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aebe2c"></a> `00aebe2c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebe30"></a> `00aebe30` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aebe34"></a> `00aebe34` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aebe38"></a> `00aebe38` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe3c"></a> `00aebe3c` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00aebe40"></a> `00aebe40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebe44"></a> `00aebe44` | `15 20 00 b9` | str w21,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aebe48"></a> `00aebe48` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aebe4c"></a> `00aebe4c` | `68 00 00 b4` | cbz x8,0x00aebe58 | `CONDITIONAL_JUMP`
<a id="insn-00aebe50"></a> `00aebe50` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aebe54"></a> `00aebe54` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00aebe58"></a> `00aebe58` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aebe5c"></a> `00aebe5c` | `42 3f e5 97` | bl 0x0043bb64 | `UNCONDITIONAL_CALL`
<a id="insn-00aebe60"></a> `00aebe60` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe64"></a> `00aebe64` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aebe68"></a> `00aebe68` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe6c"></a> `00aebe6c` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aebe70"></a> `00aebe70` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aebe74"></a> `00aebe74` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebe78"></a> `00aebe78` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aebe7c"></a> `00aebe7c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00aebe80"></a> `00aebe80` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebdb8`](#insn-00aebdb8) 範囲 `[['00aebdb8', '00aebdc3']]`
  - `FALL_THROUGH` [`00aebdc0`](#insn-00aebdc0) → [`00aebdc4`](#insn-00aebdc4)
- ブロック [`00aebdc4`](#insn-00aebdc4) 範囲 `[['00aebdc4', '00aebddb']]`
  - `FALL_THROUGH` [`00aebdd8`](#insn-00aebdd8) → [`00aebddc`](#insn-00aebddc)
- ブロック [`00aebddc`](#insn-00aebddc) 範囲 `[['00aebddc', '00aebddf']]`
  - `CONDITIONAL_JUMP` [`00aebddc`](#insn-00aebddc) → [`00aebdf4`](#insn-00aebdf4)
  - `FALL_THROUGH` [`00aebddc`](#insn-00aebddc) → [`00aebde0`](#insn-00aebde0)
- ブロック [`00aebde0`](#insn-00aebde0) 範囲 `[['00aebde0', '00aebde7']]`
  - `UNCONDITIONAL_JUMP` [`00aebde4`](#insn-00aebde4) → [`00aebe18`](#insn-00aebe18)
- ブロック [`00aebde8`](#insn-00aebde8) 範囲 `[['00aebde8', '00aebdeb']]`
  - `FALL_THROUGH` [`00aebde8`](#insn-00aebde8) → [`00aebdec`](#insn-00aebdec)
- ブロック [`00aebdec`](#insn-00aebdec) 範囲 `[['00aebdec', '00aebdf3']]`
  - `CONDITIONAL_JUMP` [`00aebdf0`](#insn-00aebdf0) → [`00aebe18`](#insn-00aebe18)
  - `FALL_THROUGH` [`00aebdf0`](#insn-00aebdf0) → [`00aebdf4`](#insn-00aebdf4)
- ブロック [`00aebdf4`](#insn-00aebdf4) 範囲 `[['00aebdf4', '00aebe03']]`
  - `CONDITIONAL_JUMP` [`00aebe00`](#insn-00aebe00) → [`00aebde8`](#insn-00aebde8)
  - `FALL_THROUGH` [`00aebe00`](#insn-00aebe00) → [`00aebe04`](#insn-00aebe04)
- ブロック [`00aebe04`](#insn-00aebe04) 範囲 `[['00aebe04', '00aebe0b']]`
  - `CONDITIONAL_JUMP` [`00aebe08`](#insn-00aebe08) → [`00aebe6c`](#insn-00aebe6c)
  - `FALL_THROUGH` [`00aebe08`](#insn-00aebe08) → [`00aebe0c`](#insn-00aebe0c)
- ブロック [`00aebe0c`](#insn-00aebe0c) 範囲 `[['00aebe0c', '00aebe13']]`
  - `CONDITIONAL_JUMP` [`00aebe10`](#insn-00aebe10) → [`00aebdf4`](#insn-00aebdf4)
  - `FALL_THROUGH` [`00aebe10`](#insn-00aebe10) → [`00aebe14`](#insn-00aebe14)
- ブロック [`00aebe14`](#insn-00aebe14) 範囲 `[['00aebe14', '00aebe17']]`
  - `FALL_THROUGH` [`00aebe14`](#insn-00aebe14) → [`00aebe18`](#insn-00aebe18)
- ブロック [`00aebe18`](#insn-00aebe18) 範囲 `[['00aebe18', '00aebe37']]`
  - `FALL_THROUGH` [`00aebe34`](#insn-00aebe34) → [`00aebe38`](#insn-00aebe38)
- ブロック [`00aebe38`](#insn-00aebe38) 範囲 `[['00aebe38', '00aebe3b']]`
  - `FALL_THROUGH` [`00aebe38`](#insn-00aebe38) → [`00aebe3c`](#insn-00aebe3c)
- ブロック [`00aebe3c`](#insn-00aebe3c) 範囲 `[['00aebe3c', '00aebe3f']]`
  - `FALL_THROUGH` [`00aebe3c`](#insn-00aebe3c) → [`00aebe40`](#insn-00aebe40)
- ブロック [`00aebe40`](#insn-00aebe40) 範囲 `[['00aebe40', '00aebe43']]`
  - `FALL_THROUGH` [`00aebe40`](#insn-00aebe40) → [`00aebe44`](#insn-00aebe44)
- ブロック [`00aebe44`](#insn-00aebe44) 範囲 `[['00aebe44', '00aebe47']]`
  - `FALL_THROUGH` [`00aebe44`](#insn-00aebe44) → [`00aebe48`](#insn-00aebe48)
- ブロック [`00aebe48`](#insn-00aebe48) 範囲 `[['00aebe48', '00aebe4f']]`
  - `CONDITIONAL_JUMP` [`00aebe4c`](#insn-00aebe4c) → [`00aebe58`](#insn-00aebe58)
  - `FALL_THROUGH` [`00aebe4c`](#insn-00aebe4c) → [`00aebe50`](#insn-00aebe50)
- ブロック [`00aebe50`](#insn-00aebe50) 範囲 `[['00aebe50', '00aebe53']]`
  - `FALL_THROUGH` [`00aebe50`](#insn-00aebe50) → [`00aebe54`](#insn-00aebe54)
- ブロック [`00aebe54`](#insn-00aebe54) 範囲 `[['00aebe54', '00aebe57']]`
  - `FALL_THROUGH` [`00aebe54`](#insn-00aebe54) → [`00aebe58`](#insn-00aebe58)
- ブロック [`00aebe58`](#insn-00aebe58) 範囲 `[['00aebe58', '00aebe5b']]`
  - `FALL_THROUGH` [`00aebe58`](#insn-00aebe58) → [`00aebe5c`](#insn-00aebe5c)
- ブロック [`00aebe5c`](#insn-00aebe5c) 範囲 `[['00aebe5c', '00aebe5f']]`
  - `FALL_THROUGH` [`00aebe5c`](#insn-00aebe5c) → [`00aebe60`](#insn-00aebe60)
- ブロック [`00aebe60`](#insn-00aebe60) 範囲 `[['00aebe60', '00aebe6b']]`
  - `FALL_THROUGH` [`00aebe68`](#insn-00aebe68) → [`00aebe6c`](#insn-00aebe6c)
- ブロック [`00aebe6c`](#insn-00aebe6c) 範囲 `[['00aebe6c', '00aebe73']]`
  - `FALL_THROUGH` [`00aebe70`](#insn-00aebe70) → [`00aebe74`](#insn-00aebe74)
- ブロック [`00aebe74`](#insn-00aebe74) 範囲 `[['00aebe74', '00aebe7b']]`
  - `FALL_THROUGH` [`00aebe78`](#insn-00aebe78) → [`00aebe7c`](#insn-00aebe7c)
- ブロック [`00aebe7c`](#insn-00aebe7c) 範囲 `[['00aebe7c', '00aebe7f']]`
  - `FALL_THROUGH` [`00aebe7c`](#insn-00aebe7c) → [`00aebe80`](#insn-00aebe80)
- ブロック [`00aebe80`](#insn-00aebe80) 範囲 `[['00aebe80', '00aebe83']]`

## 命令位置別の参照

- [`00aebdb8`](#insn-00aebdb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdbc`](#insn-00aebdbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdc0`](#insn-00aebdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdc4`](#insn-00aebdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebddc`](#insn-00aebddc) → [`00aebdf4`](#insn-00aebdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebde4`](#insn-00aebde4) → [`00aebe18`](#insn-00aebe18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdf0`](#insn-00aebdf0) → [`00aebe18`](#insn-00aebe18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe00`](#insn-00aebe00) → [`00aebde8`](#insn-00aebde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe08`](#insn-00aebe08) → [`00aebe6c`](#insn-00aebe6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe10`](#insn-00aebe10) → [`00aebdf4`](#insn-00aebdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe20`](#insn-00aebe20) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00aebe4c`](#insn-00aebe4c) → [`00aebe58`](#insn-00aebe58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe5c`](#insn-00aebe5c) → [`0043bb64`](../0043b/0043bb64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bb64` · 推定シンボル `None` · 推定型 `None`
- [`00aebe70`](#insn-00aebe70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe74`](#insn-00aebe74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe78`](#insn-00aebe78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebe7c`](#insn-00aebe7c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebdb8`](#insn-00aebdb8)

~~~json
{
  "source": "00aebdb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdbc`](#insn-00aebdbc)

~~~json
{
  "source": "00aebdbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdc0`](#insn-00aebdc0)

~~~json
{
  "source": "00aebdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdc4`](#insn-00aebdc4)

~~~json
{
  "source": "00aebdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebddc`](#insn-00aebddc)

~~~json
{
  "source": "00aebddc",
  "target": "00aebdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebde4`](#insn-00aebde4)

~~~json
{
  "source": "00aebde4",
  "target": "00aebe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdf0`](#insn-00aebdf0)

~~~json
{
  "source": "00aebdf0",
  "target": "00aebe18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe00`](#insn-00aebe00)

~~~json
{
  "source": "00aebe00",
  "target": "00aebde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe08`](#insn-00aebe08)

~~~json
{
  "source": "00aebe08",
  "target": "00aebe6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe10`](#insn-00aebe10)

~~~json
{
  "source": "00aebe10",
  "target": "00aebdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe20`](#insn-00aebe20)

~~~json
{
  "source": "00aebe20",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe4c`](#insn-00aebe4c)

~~~json
{
  "source": "00aebe4c",
  "target": "00aebe58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe5c`](#insn-00aebe5c)

~~~json
{
  "source": "00aebe5c",
  "target": "0043bb64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebe70`](#insn-00aebe70)

~~~json
{
  "source": "00aebe70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe74`](#insn-00aebe74)

~~~json
{
  "source": "00aebe74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe78`](#insn-00aebe78)

~~~json
{
  "source": "00aebe78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebe7c`](#insn-00aebe7c)

~~~json
{
  "source": "00aebe7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
