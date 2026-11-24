# 00c4ecfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd22b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd22b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-07610e540099060198bf07b68539aadf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c4f124`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0090.md#compare-491e2cfd4b1fe9fca823573613449432)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4ecfc",
  "name": "FUN_00c4ecfc",
  "size": 336,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef945cd85050117f7bb5e04a3934637a87461b35d27606641f07e5c9af385e42",
  "source_text_sha256": "ef945cd85050117f7bb5e04a3934637a87461b35d27606641f07e5c9af385e42",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4ecfc",
        "00c4ee4b"
      ]
    ],
    "bytes_sha256": "2317cc1ce2aa09e4fb0f31c17c9fbd9c3295198f2be0d61fbb8c391c4917b356",
    "instruction_count": 84,
    "instruction_bytes": 336,
    "body_bytes": 336,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3a8a4](../00c3a/00c3a8a4.md)

## 呼び出し先

- [00c3bde4](../00c3b/00c3bde4.md)
- [00c57c20](../00c57/00c57c20.md)
- [00c59c20](../00c59/00c59c20.md)

## 関連文字列（未確認候補）

~~~text
"enum"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1621 bytes

~~~c

undefined8 * FUN_00c4ecfc(long *param_1)

{
  short *psVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  long lVar5;
  char *pcVar6;
  undefined8 uVar7;
  void *pvVar8;
  
  psVar1 = (short *)*param_1;
  if ((ulong)(param_1[1] - (long)psVar1) < 2) {
LAB_00c4ed24:
    puVar2 = (undefined8 *)FUN_00c3bde4(param_1,0);
    return puVar2;
  }
  if (*psVar1 == 0x7354) {
    pcVar6 = "struct";
    uVar7 = 6;
  }
  else if (*psVar1 == 0x7554) {
    pcVar6 = "union";
    uVar7 = 5;
  }
  else {
    if (*psVar1 != 0x6554) goto LAB_00c4ed24;
    pcVar6 = "enum";
    uVar7 = 4;
  }
  *param_1 = (long)(psVar1 + 1);
  lVar3 = FUN_00c3bde4(param_1,0);
  puVar2 = (undefined8 *)0x0;
  if (lVar3 != 0) {
    pvVar8 = (void *)param_1[0x266];
    lVar5 = *(long *)((long)pvVar8 + 8);
    puVar4 = pvVar8;
    if (lVar5 - 0xfc0U < 0xfffffffffffff010) {
      puVar4 = malloc(0x1000);
      if (puVar4 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        _ZSt9terminatev();
      }
      lVar5 = 0;
      *puVar4 = pvVar8;
      puVar4[1] = 0;
      param_1[0x266] = (long)puVar4;
    }
    *(long *)((long)puVar4 + 8) = lVar5 + 0x30;
    puVar2 = (undefined8 *)((long)puVar4 + lVar5 + 0x10);
    *puVar2 = &PTR_FUN_00c99a70;
    *(undefined1 *)((long)puVar4 + lVar5 + 0x18) = 6;
    *(long *)((long)puVar4 + lVar5 + 0x30) = lVar3;
    *(char **)((long)puVar4 + lVar5 + 0x20) = pcVar6;
    *(undefined8 *)((long)puVar4 + lVar5 + 0x28) = uVar7;
    *(ushort *)((long)puVar4 + lVar5 + 0x19) =
         *(ushort *)((long)puVar4 + lVar5 + 0x19) & 0xf000 | 0x540;
  }
  return puVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4ecfc"></a> `00c4ecfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4ed00"></a> `00c4ed00` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00c4ed04"></a> `00c4ed04` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ed08"></a> `00c4ed08` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ed0c"></a> `00c4ed0c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c4ed10"></a> `00c4ed10` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4ed14"></a> `00c4ed14` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00c4ed18"></a> `00c4ed18` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-00c4ed1c"></a> `00c4ed1c` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00c4ed20"></a> `00c4ed20` | `02 01 00 54` | b.cs 0x00c4ed40 | `CONDITIONAL_JUMP`
<a id="insn-00c4ed24"></a> `00c4ed24` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00c4ed28"></a> `00c4ed28` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c4ed2c"></a> `00c4ed2c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ed30"></a> `00c4ed30` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ed34"></a> `00c4ed34` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00c4ed38"></a> `00c4ed38` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ed3c"></a> `00c4ed3c` | `2a b4 ff 17` | b 0x00c3bde4 | `CALL_TERMINATOR`
<a id="insn-00c4ed40"></a> `00c4ed40` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00c4ed44"></a> `00c4ed44` | `8a 6a 8e 52` | mov w10,#0x7354 | `FALL_THROUGH`
<a id="insn-00c4ed48"></a> `00c4ed48` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00c4ed4c"></a> `00c4ed4c` | `a0 01 00 54` | b.eq 0x00c4ed80 | `CONDITIONAL_JUMP`
<a id="insn-00c4ed50"></a> `00c4ed50` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00c4ed54"></a> `00c4ed54` | `8a aa 8e 52` | mov w10,#0x7554 | `FALL_THROUGH`
<a id="insn-00c4ed58"></a> `00c4ed58` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00c4ed5c"></a> `00c4ed5c` | `a0 01 00 54` | b.eq 0x00c4ed90 | `CONDITIONAL_JUMP`
<a id="insn-00c4ed60"></a> `00c4ed60` | `09 01 40 79` | ldrh w9,[x8] | `FALL_THROUGH`
<a id="insn-00c4ed64"></a> `00c4ed64` | `8a aa 8c 52` | mov w10,#0x6554 | `FALL_THROUGH`
<a id="insn-00c4ed68"></a> `00c4ed68` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00c4ed6c"></a> `00c4ed6c` | `c1 fd ff 54` | b.ne 0x00c4ed24 | `CONDITIONAL_JUMP`
<a id="insn-00c4ed70"></a> `00c4ed70` | `33 b3 ff b0` | adrp x19,0x2b3000 | `FALL_THROUGH`
<a id="insn-00c4ed74"></a> `00c4ed74` | `73 32 18 91` | add x19,x19,#0x60c | `FALL_THROUGH`
<a id="insn-00c4ed78"></a> `00c4ed78` | `94 00 80 52` | mov w20,#0x4 | `FALL_THROUGH`
<a id="insn-00c4ed7c"></a> `00c4ed7c` | `08 00 00 14` | b 0x00c4ed9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4ed80"></a> `00c4ed80` | `93 b3 ff f0` | adrp x19,0x2c1000 | `FALL_THROUGH`
<a id="insn-00c4ed84"></a> `00c4ed84` | `73 7a 2f 91` | add x19,x19,#0xbde | `FALL_THROUGH`
<a id="insn-00c4ed88"></a> `00c4ed88` | `d4 00 80 52` | mov w20,#0x6 | `FALL_THROUGH`
<a id="insn-00c4ed8c"></a> `00c4ed8c` | `04 00 00 14` | b 0x00c4ed9c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4ed90"></a> `00c4ed90` | `f3 b2 ff 90` | adrp x19,0x2aa000 | `FALL_THROUGH`
<a id="insn-00c4ed94"></a> `00c4ed94` | `73 ea 1d 91` | add x19,x19,#0x77a | `FALL_THROUGH`
<a id="insn-00c4ed98"></a> `00c4ed98` | `b4 00 80 52` | mov w20,#0x5 | `FALL_THROUGH`
<a id="insn-00c4ed9c"></a> `00c4ed9c` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c4eda0"></a> `00c4eda0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00c4eda4"></a> `00c4eda4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4eda8"></a> `00c4eda8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00c4edac"></a> `00c4edac` | `0e b4 ff 97` | bl 0x00c3bde4 | `UNCONDITIONAL_CALL`
<a id="insn-00c4edb0"></a> `00c4edb0` | `00 04 00 b4` | cbz x0,0x00c4ee30 | `CONDITIONAL_JUMP`
<a id="insn-00c4edb4"></a> `00c4edb4` | `b6 9a 49 f9` | ldr x22,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4edb8"></a> `00c4edb8` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00c4edbc"></a> `00c4edbc` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4edc0"></a> `00c4edc0` | `09 01 3f d1` | sub x9,x8,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c4edc4"></a> `00c4edc4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4edc8"></a> `00c4edc8` | `48 01 00 54` | b.hi 0x00c4edf0 | `CONDITIONAL_JUMP`
<a id="insn-00c4edcc"></a> `00c4edcc` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00c4edd0"></a> `00c4edd0` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4edd4"></a> `00c4edd4` | `93 2b 00 94` | bl 0x00c59c20 | `UNCONDITIONAL_CALL`
<a id="insn-00c4edd8"></a> `00c4edd8` | `80 03 00 b4` | cbz x0,0x00c4ee48 | `CONDITIONAL_JUMP`
<a id="insn-00c4eddc"></a> `00c4eddc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4ede0"></a> `00c4ede0` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4ede4"></a> `00c4ede4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c4ede8"></a> `00c4ede8` | `a0 9a 09 f9` | str x0,[x21, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4edec"></a> `00c4edec` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00c4edf0"></a> `00c4edf0` | `09 c1 00 91` | add x9,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00c4edf4"></a> `00c4edf4` | `c8 02 08 8b` | add x8,x22,x8 | `FALL_THROUGH`
<a id="insn-00c4edf8"></a> `00c4edf8` | `ca 00 80 52` | mov w10,#0x6 | `FALL_THROUGH`
<a id="insn-00c4edfc"></a> `00c4edfc` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee00"></a> `00c4ee00` | `49 02 00 f0` | adrp x9,0xc99000 | `FALL_THROUGH`
<a id="insn-00c4ee04"></a> `00c4ee04` | `29 c1 29 91` | add x9,x9,#0xa70 | `FALL_THROUGH`
<a id="insn-00c4ee08"></a> `00c4ee08` | `09 0d 01 f8` | str x9,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4ee0c"></a> `00c4ee0c` | `09 91 40 78` | ldurh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee10"></a> `00c4ee10` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00c4ee14"></a> `00c4ee14` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c4ee18"></a> `00c4ee18` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4ee1c"></a> `00c4ee1c` | `00 11 00 f9` | str x0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ee20"></a> `00c4ee20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c4ee24"></a> `00c4ee24` | `29 01 0a 2a` | orr w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00c4ee28"></a> `00c4ee28` | `13 51 01 a9` | stp x19,x20,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee2c"></a> `00c4ee2c` | `09 91 00 78` | sturh w9,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00c4ee30"></a> `00c4ee30` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c4ee34"></a> `00c4ee34` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4ee38"></a> `00c4ee38` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4ee3c"></a> `00c4ee3c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00c4ee40"></a> `00c4ee40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4ee44"></a> `00c4ee44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4ee48"></a> `00c4ee48` | `76 23 00 94` | bl 0x00c57c20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4ecfc`](#insn-00c4ecfc) 範囲 `[['00c4ecfc', '00c4ed23']]`
  - `CONDITIONAL_JUMP` [`00c4ed20`](#insn-00c4ed20) → [`00c4ed40`](#insn-00c4ed40)
  - `FALL_THROUGH` [`00c4ed20`](#insn-00c4ed20) → [`00c4ed24`](#insn-00c4ed24)
- ブロック [`00c4ed24`](#insn-00c4ed24) 範囲 `[['00c4ed24', '00c4ed3f']]`
- ブロック [`00c4ed40`](#insn-00c4ed40) 範囲 `[['00c4ed40', '00c4ed4f']]`
  - `CONDITIONAL_JUMP` [`00c4ed4c`](#insn-00c4ed4c) → [`00c4ed80`](#insn-00c4ed80)
  - `FALL_THROUGH` [`00c4ed4c`](#insn-00c4ed4c) → [`00c4ed50`](#insn-00c4ed50)
- ブロック [`00c4ed50`](#insn-00c4ed50) 範囲 `[['00c4ed50', '00c4ed5f']]`
  - `CONDITIONAL_JUMP` [`00c4ed5c`](#insn-00c4ed5c) → [`00c4ed90`](#insn-00c4ed90)
  - `FALL_THROUGH` [`00c4ed5c`](#insn-00c4ed5c) → [`00c4ed60`](#insn-00c4ed60)
- ブロック [`00c4ed60`](#insn-00c4ed60) 範囲 `[['00c4ed60', '00c4ed6f']]`
  - `CONDITIONAL_JUMP` [`00c4ed6c`](#insn-00c4ed6c) → [`00c4ed24`](#insn-00c4ed24)
  - `FALL_THROUGH` [`00c4ed6c`](#insn-00c4ed6c) → [`00c4ed70`](#insn-00c4ed70)
- ブロック [`00c4ed70`](#insn-00c4ed70) 範囲 `[['00c4ed70', '00c4ed7f']]`
  - `UNCONDITIONAL_JUMP` [`00c4ed7c`](#insn-00c4ed7c) → [`00c4ed9c`](#insn-00c4ed9c)
- ブロック [`00c4ed80`](#insn-00c4ed80) 範囲 `[['00c4ed80', '00c4ed8f']]`
  - `UNCONDITIONAL_JUMP` [`00c4ed8c`](#insn-00c4ed8c) → [`00c4ed9c`](#insn-00c4ed9c)
- ブロック [`00c4ed90`](#insn-00c4ed90) 範囲 `[['00c4ed90', '00c4ed9b']]`
  - `FALL_THROUGH` [`00c4ed98`](#insn-00c4ed98) → [`00c4ed9c`](#insn-00c4ed9c)
- ブロック [`00c4ed9c`](#insn-00c4ed9c) 範囲 `[['00c4ed9c', '00c4edb3']]`
  - `CONDITIONAL_JUMP` [`00c4edb0`](#insn-00c4edb0) → [`00c4ee30`](#insn-00c4ee30)
  - `FALL_THROUGH` [`00c4edb0`](#insn-00c4edb0) → [`00c4edb4`](#insn-00c4edb4)
- ブロック [`00c4edb4`](#insn-00c4edb4) 範囲 `[['00c4edb4', '00c4edcb']]`
  - `CONDITIONAL_JUMP` [`00c4edc8`](#insn-00c4edc8) → [`00c4edf0`](#insn-00c4edf0)
  - `FALL_THROUGH` [`00c4edc8`](#insn-00c4edc8) → [`00c4edcc`](#insn-00c4edcc)
- ブロック [`00c4edcc`](#insn-00c4edcc) 範囲 `[['00c4edcc', '00c4eddb']]`
  - `CONDITIONAL_JUMP` [`00c4edd8`](#insn-00c4edd8) → [`00c4ee48`](#insn-00c4ee48)
  - `FALL_THROUGH` [`00c4edd8`](#insn-00c4edd8) → [`00c4eddc`](#insn-00c4eddc)
- ブロック [`00c4eddc`](#insn-00c4eddc) 範囲 `[['00c4eddc', '00c4edef']]`
  - `FALL_THROUGH` [`00c4edec`](#insn-00c4edec) → [`00c4edf0`](#insn-00c4edf0)
- ブロック [`00c4edf0`](#insn-00c4edf0) 範囲 `[['00c4edf0', '00c4ee2f']]`
  - `FALL_THROUGH` [`00c4ee2c`](#insn-00c4ee2c) → [`00c4ee30`](#insn-00c4ee30)
- ブロック [`00c4ee30`](#insn-00c4ee30) 範囲 `[['00c4ee30', '00c4ee47']]`
- ブロック [`00c4ee48`](#insn-00c4ee48) 範囲 `[['00c4ee48', '00c4ee4b']]`

## 命令位置別の参照

- [`00c4ed00`](#insn-00c4ed00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed04`](#insn-00c4ed04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed08`](#insn-00c4ed08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed0c`](#insn-00c4ed0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed20`](#insn-00c4ed20) → [`00c4ed40`](#insn-00c4ed40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed28`](#insn-00c4ed28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed2c`](#insn-00c4ed2c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed30`](#insn-00c4ed30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed34`](#insn-00c4ed34) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed3c`](#insn-00c4ed3c) → [`00c3bde4`](../00c3b/00c3bde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3bde4` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed4c`](#insn-00c4ed4c) → [`00c4ed80`](#insn-00c4ed80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed5c`](#insn-00c4ed5c) → [`00c4ed90`](#insn-00c4ed90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed6c`](#insn-00c4ed6c) → [`00c4ed24`](#insn-00c4ed24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed7c`](#insn-00c4ed7c) → [`00c4ed9c`](#insn-00c4ed9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ed8c`](#insn-00c4ed8c) → [`00c4ed9c`](#insn-00c4ed9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edac`](#insn-00c4edac) → [`00c3bde4`](../00c3b/00c3bde4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c3bde4` · 推定シンボル `None` · 推定型 `None`
- [`00c4edb0`](#insn-00c4edb0) → [`00c4ee30`](#insn-00c4ee30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edc8`](#insn-00c4edc8) → [`00c4edf0`](#insn-00c4edf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4edd4`](#insn-00c4edd4) → [`00c59c20`](../00c59/00c59c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59c20` · 推定シンボル `None` · 推定型 `None`
- [`00c4edd8`](#insn-00c4edd8) → [`00c4ee48`](#insn-00c4ee48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee08`](#insn-00c4ee08) → `00c99a70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4ee28`](#insn-00c4ee28) → `002b360c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee30`](#insn-00c4ee30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee34`](#insn-00c4ee34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee38`](#insn-00c4ee38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee3c`](#insn-00c4ee3c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4ee48`](#insn-00c4ee48) → [`00c57c20`](../00c57/00c57c20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4ed00`](#insn-00c4ed00)

~~~json
{
  "source": "00c4ed00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed04`](#insn-00c4ed04)

~~~json
{
  "source": "00c4ed04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed08`](#insn-00c4ed08)

~~~json
{
  "source": "00c4ed08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed0c`](#insn-00c4ed0c)

~~~json
{
  "source": "00c4ed0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed20`](#insn-00c4ed20)

~~~json
{
  "source": "00c4ed20",
  "target": "00c4ed40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed28`](#insn-00c4ed28)

~~~json
{
  "source": "00c4ed28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed2c`](#insn-00c4ed2c)

~~~json
{
  "source": "00c4ed2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed30`](#insn-00c4ed30)

~~~json
{
  "source": "00c4ed30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed34`](#insn-00c4ed34)

~~~json
{
  "source": "00c4ed34",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed3c`](#insn-00c4ed3c)

~~~json
{
  "source": "00c4ed3c",
  "target": "00c3bde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4ed4c`](#insn-00c4ed4c)

~~~json
{
  "source": "00c4ed4c",
  "target": "00c4ed80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed5c`](#insn-00c4ed5c)

~~~json
{
  "source": "00c4ed5c",
  "target": "00c4ed90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed6c`](#insn-00c4ed6c)

~~~json
{
  "source": "00c4ed6c",
  "target": "00c4ed24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed7c`](#insn-00c4ed7c)

~~~json
{
  "source": "00c4ed7c",
  "target": "00c4ed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ed8c`](#insn-00c4ed8c)

~~~json
{
  "source": "00c4ed8c",
  "target": "00c4ed9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edac`](#insn-00c4edac)

~~~json
{
  "source": "00c4edac",
  "target": "00c3bde4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4edb0`](#insn-00c4edb0)

~~~json
{
  "source": "00c4edb0",
  "target": "00c4ee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edc8`](#insn-00c4edc8)

~~~json
{
  "source": "00c4edc8",
  "target": "00c4edf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4edd4`](#insn-00c4edd4)

~~~json
{
  "source": "00c4edd4",
  "target": "00c59c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4edd8`](#insn-00c4edd8)

~~~json
{
  "source": "00c4edd8",
  "target": "00c4ee48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee08`](#insn-00c4ee08)

~~~json
{
  "source": "00c4ee08",
  "target": "00c99a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c99a70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4ee28`](#insn-00c4ee28)

~~~json
{
  "source": "00c4ee28",
  "target": "002b360c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee30`](#insn-00c4ee30)

~~~json
{
  "source": "00c4ee30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee34`](#insn-00c4ee34)

~~~json
{
  "source": "00c4ee34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee38`](#insn-00c4ee38)

~~~json
{
  "source": "00c4ee38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee3c`](#insn-00c4ee3c)

~~~json
{
  "source": "00c4ee3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4ee48`](#insn-00c4ee48)

~~~json
{
  "source": "00c4ee48",
  "target": "00c57c20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
