# 00b2aecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acb43c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acb43c.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-7098324038ac03b4b70c6a6345c39533)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b2b2f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-a86f33226ecfeeba2e0bd6f85fb2c5c5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2aecc",
  "name": "FUN_00b2aecc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fc897cb049238b99bc42715bfe810d78a09f3c7a7621ac26a2a9d5027542af4a",
  "source_text_sha256": "fc897cb049238b99bc42715bfe810d78a09f3c7a7621ac26a2a9d5027542af4a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2aecc",
        "00b2afe7"
      ]
    ],
    "bytes_sha256": "727075abac3f4b53dd621915a423ce6dc403ed31f923d5bb41a7a58e28d60cca",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b2ac48](../00b2a/00b2ac48.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1681 bytes

~~~c

void FUN_00b2aecc(undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  void *__ptr;
  undefined8 *puVar4;
  undefined8 uVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  
  puVar6 = (undefined8 *)*param_1;
  puVar2 = (undefined8 *)param_1[1];
  puVar1 = (undefined8 *)((long)puVar6 + (param_2[1] - (long)puVar2));
  puVar3 = puVar1;
  puVar7 = puVar6;
  if (puVar2 != puVar6) {
    do {
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = 0;
      uVar5 = *puVar7;
      puVar3[1] = puVar7[1];
      *puVar3 = uVar5;
      puVar3[2] = puVar7[2];
      *puVar7 = 0;
      puVar7[1] = 0;
      puVar7[2] = 0;
      puVar7 = puVar7 + 3;
      puVar3 = puVar3 + 3;
    } while (puVar7 != puVar2);
    do {
      puVar7 = (undefined8 *)*puVar6;
      if (puVar7 != (undefined8 *)0x0) {
        puVar4 = (undefined8 *)puVar6[1];
        puVar3 = puVar7;
        if (puVar4 != puVar7) {
          do {
            puVar3 = puVar4 + -3;
            __ptr = (void *)*puVar3;
            if (__ptr != (void *)0x0) {
              puVar4[-2] = __ptr;
              _ZdlPv(__ptr);
            }
            puVar4 = puVar3;
          } while (puVar3 != puVar7);
          puVar3 = (undefined8 *)*puVar6;
        }
        puVar6[1] = puVar7;
        _ZdlPv(puVar3);
      }
      puVar6 = puVar6 + 3;
    } while (puVar6 != puVar2);
  }
  param_2[1] = puVar1;
  uVar5 = *param_1;
  *param_1 = puVar1;
  param_1[1] = uVar5;
  param_2[1] = uVar5;
  uVar5 = param_1[1];
  param_1[1] = param_2[2];
  param_2[2] = uVar5;
  uVar5 = param_1[2];
  param_1[2] = param_2[3];
  param_2[3] = uVar5;
  *param_2 = param_2[1];
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2aecc"></a> `00b2aecc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b2aed0"></a> `00b2aed0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aed4"></a> `00b2aed4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2aed8"></a> `00b2aed8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2aedc"></a> `00b2aedc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2aee0"></a> `00b2aee0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b2aee4"></a> `00b2aee4` | `16 54 40 a9` | ldp x22,x21,[x0] | `FALL_THROUGH`
<a id="insn-00b2aee8"></a> `00b2aee8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b2aeec"></a> `00b2aeec` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00b2aef0"></a> `00b2aef0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b2aef4"></a> `00b2aef4` | `c9 02 15 cb` | sub x9,x22,x21 | `FALL_THROUGH`
<a id="insn-00b2aef8"></a> `00b2aef8` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00b2aefc"></a> `00b2aefc` | `17 01 09 8b` | add x23,x8,x9 | `FALL_THROUGH`
<a id="insn-00b2af00"></a> `00b2af00` | `c0 04 00 54` | b.eq 0x00b2af98 | `CONDITIONAL_JUMP`
<a id="insn-00b2af04"></a> `00b2af04` | `e8 03 17 aa` | mov x8,x23 | `FALL_THROUGH`
<a id="insn-00b2af08"></a> `00b2af08` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00b2af0c"></a> `00b2af0c` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00b2af10"></a> `00b2af10` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b2af14"></a> `00b2af14` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00b2af18"></a> `00b2af18` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00b2af1c"></a> `00b2af1c` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b2af20"></a> `00b2af20` | `0a 09 00 f9` | str x10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b2af24"></a> `00b2af24` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b2af28"></a> `00b2af28` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00b2af2c"></a> `00b2af2c` | `3f 09 00 f9` | str xzr,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00b2af30"></a> `00b2af30` | `29 61 00 91` | add x9,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00b2af34"></a> `00b2af34` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00b2af38"></a> `00b2af38` | `a1 fe ff 54` | b.ne 0x00b2af0c | `CONDITIONAL_JUMP`
<a id="insn-00b2af3c"></a> `00b2af3c` | `07 00 00 14` | b 0x00b2af58 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2af40"></a> `00b2af40` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00b2af44"></a> `00b2af44` | `d8 06 00 f9` | str x24,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00b2af48"></a> `00b2af48` | `da b2 04 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2af4c"></a> `00b2af4c` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00b2af50"></a> `00b2af50` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00b2af54"></a> `00b2af54` | `20 02 00 54` | b.eq 0x00b2af98 | `CONDITIONAL_JUMP`
<a id="insn-00b2af58"></a> `00b2af58` | `d8 02 40 f9` | ldr x24,[x22] | `FALL_THROUGH`
<a id="insn-00b2af5c"></a> `00b2af5c` | `98 ff ff b4` | cbz x24,0x00b2af4c | `CONDITIONAL_JUMP`
<a id="insn-00b2af60"></a> `00b2af60` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00b2af64"></a> `00b2af64` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b2af68"></a> `00b2af68` | `1f 01 18 eb` | cmp x8,x24 | `FALL_THROUGH`
<a id="insn-00b2af6c"></a> `00b2af6c` | `c0 fe ff 54` | b.eq 0x00b2af44 | `CONDITIONAL_JUMP`
<a id="insn-00b2af70"></a> `00b2af70` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b2af74"></a> `00b2af74` | `04 00 00 14` | b 0x00b2af84 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2af78"></a> `00b2af78` | `3f 03 18 eb` | cmp x25,x24 | `FALL_THROUGH`
<a id="insn-00b2af7c"></a> `00b2af7c` | `e8 03 19 aa` | mov x8,x25 | `FALL_THROUGH`
<a id="insn-00b2af80"></a> `00b2af80` | `00 fe ff 54` | b.eq 0x00b2af40 | `CONDITIONAL_JUMP`
<a id="insn-00b2af84"></a> `00b2af84` | `20 8f 5e f8` | ldr x0,[x25, #-0x18]! | `FALL_THROUGH`
<a id="insn-00b2af88"></a> `00b2af88` | `80 ff ff b4` | cbz x0,0x00b2af78 | `CONDITIONAL_JUMP`
<a id="insn-00b2af8c"></a> `00b2af8c` | `00 01 1f f8` | stur x0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00b2af90"></a> `00b2af90` | `c8 b2 04 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2af94"></a> `00b2af94` | `f9 ff ff 17` | b 0x00b2af78 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2af98"></a> `00b2af98` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2af9c"></a> `00b2af9c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b2afa0"></a> `00b2afa0` | `97 22 00 a9` | stp x23,x8,[x20] | `FALL_THROUGH`
<a id="insn-00b2afa4"></a> `00b2afa4` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2afa8"></a> `00b2afa8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2afac"></a> `00b2afac` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b2afb0"></a> `00b2afb0` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b2afb4"></a> `00b2afb4` | `69 0e 40 f9` | ldr x9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b2afb8"></a> `00b2afb8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2afbc"></a> `00b2afbc` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2afc0"></a> `00b2afc0` | `89 0a 00 f9` | str x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2afc4"></a> `00b2afc4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2afc8"></a> `00b2afc8` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b2afcc"></a> `00b2afcc` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00b2afd0"></a> `00b2afd0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2afd4"></a> `00b2afd4` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2afd8"></a> `00b2afd8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2afdc"></a> `00b2afdc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2afe0"></a> `00b2afe0` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b2afe4"></a> `00b2afe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2aecc`](#insn-00b2aecc) 範囲 `[['00b2aecc', '00b2af03']]`
  - `CONDITIONAL_JUMP` [`00b2af00`](#insn-00b2af00) → [`00b2af98`](#insn-00b2af98)
  - `FALL_THROUGH` [`00b2af00`](#insn-00b2af00) → [`00b2af04`](#insn-00b2af04)
- ブロック [`00b2af04`](#insn-00b2af04) 範囲 `[['00b2af04', '00b2af0b']]`
  - `FALL_THROUGH` [`00b2af08`](#insn-00b2af08) → [`00b2af0c`](#insn-00b2af0c)
- ブロック [`00b2af0c`](#insn-00b2af0c) 範囲 `[['00b2af0c', '00b2af3b']]`
  - `CONDITIONAL_JUMP` [`00b2af38`](#insn-00b2af38) → [`00b2af0c`](#insn-00b2af0c)
  - `FALL_THROUGH` [`00b2af38`](#insn-00b2af38) → [`00b2af3c`](#insn-00b2af3c)
- ブロック [`00b2af3c`](#insn-00b2af3c) 範囲 `[['00b2af3c', '00b2af3f']]`
  - `UNCONDITIONAL_JUMP` [`00b2af3c`](#insn-00b2af3c) → [`00b2af58`](#insn-00b2af58)
- ブロック [`00b2af40`](#insn-00b2af40) 範囲 `[['00b2af40', '00b2af43']]`
  - `FALL_THROUGH` [`00b2af40`](#insn-00b2af40) → [`00b2af44`](#insn-00b2af44)
- ブロック [`00b2af44`](#insn-00b2af44) 範囲 `[['00b2af44', '00b2af4b']]`
  - `FALL_THROUGH` [`00b2af48`](#insn-00b2af48) → [`00b2af4c`](#insn-00b2af4c)
- ブロック [`00b2af4c`](#insn-00b2af4c) 範囲 `[['00b2af4c', '00b2af57']]`
  - `CONDITIONAL_JUMP` [`00b2af54`](#insn-00b2af54) → [`00b2af98`](#insn-00b2af98)
  - `FALL_THROUGH` [`00b2af54`](#insn-00b2af54) → [`00b2af58`](#insn-00b2af58)
- ブロック [`00b2af58`](#insn-00b2af58) 範囲 `[['00b2af58', '00b2af5f']]`
  - `CONDITIONAL_JUMP` [`00b2af5c`](#insn-00b2af5c) → [`00b2af4c`](#insn-00b2af4c)
  - `FALL_THROUGH` [`00b2af5c`](#insn-00b2af5c) → [`00b2af60`](#insn-00b2af60)
- ブロック [`00b2af60`](#insn-00b2af60) 範囲 `[['00b2af60', '00b2af6f']]`
  - `CONDITIONAL_JUMP` [`00b2af6c`](#insn-00b2af6c) → [`00b2af44`](#insn-00b2af44)
  - `FALL_THROUGH` [`00b2af6c`](#insn-00b2af6c) → [`00b2af70`](#insn-00b2af70)
- ブロック [`00b2af70`](#insn-00b2af70) 範囲 `[['00b2af70', '00b2af77']]`
  - `UNCONDITIONAL_JUMP` [`00b2af74`](#insn-00b2af74) → [`00b2af84`](#insn-00b2af84)
- ブロック [`00b2af78`](#insn-00b2af78) 範囲 `[['00b2af78', '00b2af83']]`
  - `CONDITIONAL_JUMP` [`00b2af80`](#insn-00b2af80) → [`00b2af40`](#insn-00b2af40)
  - `FALL_THROUGH` [`00b2af80`](#insn-00b2af80) → [`00b2af84`](#insn-00b2af84)
- ブロック [`00b2af84`](#insn-00b2af84) 範囲 `[['00b2af84', '00b2af8b']]`
  - `CONDITIONAL_JUMP` [`00b2af88`](#insn-00b2af88) → [`00b2af78`](#insn-00b2af78)
  - `FALL_THROUGH` [`00b2af88`](#insn-00b2af88) → [`00b2af8c`](#insn-00b2af8c)
- ブロック [`00b2af8c`](#insn-00b2af8c) 範囲 `[['00b2af8c', '00b2af97']]`
  - `UNCONDITIONAL_JUMP` [`00b2af94`](#insn-00b2af94) → [`00b2af78`](#insn-00b2af78)
- ブロック [`00b2af98`](#insn-00b2af98) 範囲 `[['00b2af98', '00b2afe7']]`

## 命令位置別の参照

- [`00b2aecc`](#insn-00b2aecc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aed0`](#insn-00b2aed0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aed4`](#insn-00b2aed4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aed8`](#insn-00b2aed8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aedc`](#insn-00b2aedc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af00`](#insn-00b2af00) → [`00b2af98`](#insn-00b2af98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af38`](#insn-00b2af38) → [`00b2af0c`](#insn-00b2af0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af3c`](#insn-00b2af3c) → [`00b2af58`](#insn-00b2af58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af48`](#insn-00b2af48) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b2af54`](#insn-00b2af54) → [`00b2af98`](#insn-00b2af98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af5c`](#insn-00b2af5c) → [`00b2af4c`](#insn-00b2af4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af6c`](#insn-00b2af6c) → [`00b2af44`](#insn-00b2af44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af74`](#insn-00b2af74) → [`00b2af84`](#insn-00b2af84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af80`](#insn-00b2af80) → [`00b2af40`](#insn-00b2af40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af88`](#insn-00b2af88) → [`00b2af78`](#insn-00b2af78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2af90`](#insn-00b2af90) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b2af94`](#insn-00b2af94) → [`00b2af78`](#insn-00b2af78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2afd0`](#insn-00b2afd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2afd4`](#insn-00b2afd4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2afd8`](#insn-00b2afd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2afdc`](#insn-00b2afdc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2afe0`](#insn-00b2afe0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2aecc`](#insn-00b2aecc)

~~~json
{
  "source": "00b2aecc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aed0`](#insn-00b2aed0)

~~~json
{
  "source": "00b2aed0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aed4`](#insn-00b2aed4)

~~~json
{
  "source": "00b2aed4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aed8`](#insn-00b2aed8)

~~~json
{
  "source": "00b2aed8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aedc`](#insn-00b2aedc)

~~~json
{
  "source": "00b2aedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af00`](#insn-00b2af00)

~~~json
{
  "source": "00b2af00",
  "target": "00b2af98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af38`](#insn-00b2af38)

~~~json
{
  "source": "00b2af38",
  "target": "00b2af0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af3c`](#insn-00b2af3c)

~~~json
{
  "source": "00b2af3c",
  "target": "00b2af58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af48`](#insn-00b2af48)

~~~json
{
  "source": "00b2af48",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2af54`](#insn-00b2af54)

~~~json
{
  "source": "00b2af54",
  "target": "00b2af98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af5c`](#insn-00b2af5c)

~~~json
{
  "source": "00b2af5c",
  "target": "00b2af4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af6c`](#insn-00b2af6c)

~~~json
{
  "source": "00b2af6c",
  "target": "00b2af44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af74`](#insn-00b2af74)

~~~json
{
  "source": "00b2af74",
  "target": "00b2af84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af80`](#insn-00b2af80)

~~~json
{
  "source": "00b2af80",
  "target": "00b2af40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af88`](#insn-00b2af88)

~~~json
{
  "source": "00b2af88",
  "target": "00b2af78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2af90`](#insn-00b2af90)

~~~json
{
  "source": "00b2af90",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2af94`](#insn-00b2af94)

~~~json
{
  "source": "00b2af94",
  "target": "00b2af78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2afd0`](#insn-00b2afd0)

~~~json
{
  "source": "00b2afd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2afd4`](#insn-00b2afd4)

~~~json
{
  "source": "00b2afd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2afd8`](#insn-00b2afd8)

~~~json
{
  "source": "00b2afd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2afdc`](#insn-00b2afdc)

~~~json
{
  "source": "00b2afdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2afe0`](#insn-00b2afe0)

~~~json
{
  "source": "00b2afe0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
