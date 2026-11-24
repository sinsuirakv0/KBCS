# 00c4bddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4ade8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4ade8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0042.md#compare-e804ec03021290d2874bbdefc905901c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4bddc",
  "name": "FUN_00c4bddc",
  "size": 848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0a3edf36b0a9f72d1ebd9a73cfe212c5f7495b727e7a2434b2e119c8ae99119",
  "source_text_sha256": "e0a3edf36b0a9f72d1ebd9a73cfe212c5f7495b727e7a2434b2e119c8ae99119",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4bddc",
        "00c4c12b"
      ]
    ],
    "bytes_sha256": "763edff1a14f057764e654e5157eb8f0924512a8e45d5e2c84c3fb981eb7d2f7",
    "instruction_count": 212,
    "instruction_bytes": 848,
    "body_bytes": 848,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c461d4](../00c46/00c461d4.md)
- [00c5b140](../00c5b/00c5b140.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5514 bytes

~~~c

void FUN_00c4bddc(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  long lVar3;
  ulong uVar4;
  size_t sVar5;
  long lVar6;
  long *plVar7;
  undefined8 *puVar8;
  
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 8U) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 1000;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined8 *)((long)pvVar1 + lVar2) = 0x7365726975716572;
  lVar3 = param_2[1];
  lVar6 = *(long *)(param_1 + 0x18);
  lVar2 = lVar3 + 8;
  param_2[1] = lVar2;
  if (lVar6 != 0) {
    uVar4 = lVar3 + 9;
    pvVar1 = (void *)*param_2;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar3 + 0x3e9;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x28;
    FUN_00c461d4(param_1 + 0x10,param_2);
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    uVar4 = lVar2 + 1;
    *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
    if ((ulong)param_2[2] < uVar4) {
      sVar5 = param_2[2] * 2;
      uVar4 = lVar2 + 0x3e1;
      if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
        sVar5 = uVar4;
      }
      param_2[2] = sVar5;
      pvVar1 = realloc(pvVar1,sVar5);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
      uVar4 = lVar2 + 1;
    }
    param_2[1] = uVar4;
    *(undefined1 *)((long)pvVar1 + lVar2) = 0x29;
    lVar2 = param_2[1];
  }
  uVar4 = lVar2 + 1;
  pvVar1 = (void *)*param_2;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x7b;
  if (*(long *)(param_1 + 0x28) != 0) {
    puVar8 = *(undefined8 **)(param_1 + 0x20);
    lVar2 = *(long *)(param_1 + 0x28) << 3;
    do {
      plVar7 = (long *)*puVar8;
      (**(code **)(*plVar7 + 0x20))(plVar7,param_2);
      if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
        (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      }
      lVar2 = lVar2 + -8;
      puVar8 = puVar8 + 1;
    } while (lVar2 != 0);
  }
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x20;
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar4) {
    sVar5 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar5 < uVar4 || sVar5 - uVar4 == 0) {
      sVar5 = uVar4;
    }
    param_2[2] = sVar5;
    pvVar1 = realloc(pvVar1,sVar5);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x7d;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c4bddc"></a> `00c4bddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4bde0"></a> `00c4bde0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4bde4"></a> `00c4bde4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bde8"></a> `00c4bde8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bdec"></a> `00c4bdec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4bdf0"></a> `00c4bdf0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bdf4"></a> `00c4bdf4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4bdf8"></a> `00c4bdf8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00c4bdfc"></a> `00c4bdfc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4be00"></a> `00c4be00` | `2b 21 00 91` | add x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00c4be04"></a> `00c4be04` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00c4be08"></a> `00c4be08` | `89 01 00 54` | b.ls 0x00c4be38 | `CONDITIONAL_JUMP`
<a id="insn-00c4be0c"></a> `00c4be0c` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4be10"></a> `00c4be10` | `29 a1 0f 91` | add x9,x9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00c4be14"></a> `00c4be14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00c4be18"></a> `00c4be18` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c4be1c"></a> `00c4be1c` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00c4be20"></a> `00c4be20` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4be24"></a> `00c4be24` | `c7 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4be28"></a> `00c4be28` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4be2c"></a> `00c4be2c` | `00 17 00 b4` | cbz x0,0x00c4c10c | `CONDITIONAL_JUMP`
<a id="insn-00c4be30"></a> `00c4be30` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4be34"></a> `00c4be34` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00c4be38"></a> `00c4be38` | `4a ae 8c d2` | mov x10,#0x6572 | `FALL_THROUGH`
<a id="insn-00c4be3c"></a> `00c4be3c` | `2a ae ae f2` | movk x10,#0x7571, LSL #16 | `FALL_THROUGH`
<a id="insn-00c4be40"></a> `00c4be40` | `2a 4d ce f2` | movk x10,#0x7269, LSL #32 | `FALL_THROUGH`
<a id="insn-00c4be44"></a> `00c4be44` | `aa 6c ee f2` | movk x10,#0x7365, LSL #48 | `FALL_THROUGH`
<a id="insn-00c4be48"></a> `00c4be48` | `0a 69 29 f8` | str x10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00c4be4c"></a> `00c4be4c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4be50"></a> `00c4be50` | `8a 0e 40 f9` | ldr x10,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00c4be54"></a> `00c4be54` | `28 21 00 91` | add x8,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00c4be58"></a> `00c4be58` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4be5c"></a> `00c4be5c` | `2a 08 00 b4` | cbz x10,0x00c4bf60 | `CONDITIONAL_JUMP`
<a id="insn-00c4be60"></a> `00c4be60` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4be64"></a> `00c4be64` | `2a 25 00 91` | add x10,x9,#0x9 | `FALL_THROUGH`
<a id="insn-00c4be68"></a> `00c4be68` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4be6c"></a> `00c4be6c` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00c4be70"></a> `00c4be70` | `69 01 00 54` | b.ls 0x00c4be9c | `CONDITIONAL_JUMP`
<a id="insn-00c4be74"></a> `00c4be74` | `68 f9 7f d3` | lsl x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00c4be78"></a> `00c4be78` | `29 a5 0f 91` | add x9,x9,#0x3e9 | `FALL_THROUGH`
<a id="insn-00c4be7c"></a> `00c4be7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c4be80"></a> `00c4be80` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00c4be84"></a> `00c4be84` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4be88"></a> `00c4be88` | `ae 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4be8c"></a> `00c4be8c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4be90"></a> `00c4be90` | `80 14 00 b4` | cbz x0,0x00c4c120 | `CONDITIONAL_JUMP`
<a id="insn-00c4be94"></a> `00c4be94` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4be98"></a> `00c4be98` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4be9c"></a> `00c4be9c` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bea0"></a> `00c4bea0` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00c4bea4"></a> `00c4bea4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bea8"></a> `00c4bea8` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4beac"></a> `00c4beac` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4beb0"></a> `00c4beb0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4beb4"></a> `00c4beb4` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c4beb8"></a> `00c4beb8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bebc"></a> `00c4bebc` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bec0"></a> `00c4bec0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4bec4"></a> `00c4bec4` | `69 01 00 54` | b.ls 0x00c4bef0 | `CONDITIONAL_JUMP`
<a id="insn-00c4bec8"></a> `00c4bec8` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4becc"></a> `00c4becc` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4bed0"></a> `00c4bed0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4bed4"></a> `00c4bed4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4bed8"></a> `00c4bed8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bedc"></a> `00c4bedc` | `99 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bee0"></a> `00c4bee0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bee4"></a> `00c4bee4` | `00 12 00 b4` | cbz x0,0x00c4c124 | `CONDITIONAL_JUMP`
<a id="insn-00c4bee8"></a> `00c4bee8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4beec"></a> `00c4beec` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bef0"></a> `00c4bef0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bef4"></a> `00c4bef4` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00c4bef8"></a> `00c4bef8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4befc"></a> `00c4befc` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bf00"></a> `00c4bf00` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00c4bf04"></a> `00c4bf04` | `b4 e8 ff 97` | bl 0x00c461d4 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bf08"></a> `00c4bf08` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf0c"></a> `00c4bf0c` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bf10"></a> `00c4bf10` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bf14"></a> `00c4bf14` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf18"></a> `00c4bf18` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf1c"></a> `00c4bf1c` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bf20"></a> `00c4bf20` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4bf24"></a> `00c4bf24` | `69 01 00 54` | b.ls 0x00c4bf50 | `CONDITIONAL_JUMP`
<a id="insn-00c4bf28"></a> `00c4bf28` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf2c"></a> `00c4bf2c` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4bf30"></a> `00c4bf30` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4bf34"></a> `00c4bf34` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4bf38"></a> `00c4bf38` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf3c"></a> `00c4bf3c` | `81 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bf40"></a> `00c4bf40` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bf44"></a> `00c4bf44` | `20 0f 00 b4` | cbz x0,0x00c4c128 | `CONDITIONAL_JUMP`
<a id="insn-00c4bf48"></a> `00c4bf48` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf4c"></a> `00c4bf4c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf50"></a> `00c4bf50` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf54"></a> `00c4bf54` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00c4bf58"></a> `00c4bf58` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bf5c"></a> `00c4bf5c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf60"></a> `00c4bf60` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf64"></a> `00c4bf64` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf68"></a> `00c4bf68` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bf6c"></a> `00c4bf6c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4bf70"></a> `00c4bf70` | `69 01 00 54` | b.ls 0x00c4bf9c | `CONDITIONAL_JUMP`
<a id="insn-00c4bf74"></a> `00c4bf74` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf78"></a> `00c4bf78` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4bf7c"></a> `00c4bf7c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4bf80"></a> `00c4bf80` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4bf84"></a> `00c4bf84` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bf88"></a> `00c4bf88` | `6e 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bf8c"></a> `00c4bf8c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bf90"></a> `00c4bf90` | `00 0c 00 b4` | cbz x0,0x00c4c110 | `CONDITIONAL_JUMP`
<a id="insn-00c4bf94"></a> `00c4bf94` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bf98"></a> `00c4bf98` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bf9c"></a> `00c4bf9c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bfa0"></a> `00c4bfa0` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00c4bfa4"></a> `00c4bfa4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bfa8"></a> `00c4bfa8` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bfac"></a> `00c4bfac` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bfb0"></a> `00c4bfb0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bfb4"></a> `00c4bfb4` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bfb8"></a> `00c4bfb8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bfbc"></a> `00c4bfbc` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4bfc0"></a> `00c4bfc0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4bfc4"></a> `00c4bfc4` | `69 01 00 54` | b.ls 0x00c4bff0 | `CONDITIONAL_JUMP`
<a id="insn-00c4bfc8"></a> `00c4bfc8` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bfcc"></a> `00c4bfcc` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4bfd0"></a> `00c4bfd0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4bfd4"></a> `00c4bfd4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4bfd8"></a> `00c4bfd8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4bfdc"></a> `00c4bfdc` | `59 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4bfe0"></a> `00c4bfe0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4bfe4"></a> `00c4bfe4` | `80 09 00 b4` | cbz x0,0x00c4c114 | `CONDITIONAL_JUMP`
<a id="insn-00c4bfe8"></a> `00c4bfe8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bfec"></a> `00c4bfec` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4bff0"></a> `00c4bff0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4bff4"></a> `00c4bff4` | `69 0f 80 52` | mov w9,#0x7b | `FALL_THROUGH`
<a id="insn-00c4bff8"></a> `00c4bff8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4bffc"></a> `00c4bffc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00c4c000"></a> `00c4c000` | `e8 02 00 b4` | cbz x8,0x00c4c05c | `CONDITIONAL_JUMP`
<a id="insn-00c4c004"></a> `00c4c004` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00c4c008"></a> `00c4c008` | `16 f1 7d d3` | lsl x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00c4c00c"></a> `00c4c00c` | `04 00 00 14` | b 0x00c4c01c | `UNCONDITIONAL_JUMP`
<a id="insn-00c4c010"></a> `00c4c010` | `d6 22 00 f1` | subs x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00c4c014"></a> `00c4c014` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00c4c018"></a> `00c4c018` | `20 02 00 54` | b.eq 0x00c4c05c | `CONDITIONAL_JUMP`
<a id="insn-00c4c01c"></a> `00c4c01c` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00c4c020"></a> `00c4c020` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4c024"></a> `00c4c024` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c4c028"></a> `00c4c028` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4c02c"></a> `00c4c02c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c4c030"></a> `00c4c030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4c034"></a> `00c4c034` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4c038"></a> `00c4c038` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00c4c03c"></a> `00c4c03c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00c4c040"></a> `00c4c040` | `80 fe ff 54` | b.eq 0x00c4c010 | `CONDITIONAL_JUMP`
<a id="insn-00c4c044"></a> `00c4c044` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c4c048"></a> `00c4c048` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4c04c"></a> `00c4c04c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00c4c050"></a> `00c4c050` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c4c054"></a> `00c4c054` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c4c058"></a> `00c4c058` | `ee ff ff 17` | b 0x00c4c010 | `UNCONDITIONAL_JUMP`
<a id="insn-00c4c05c"></a> `00c4c05c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c060"></a> `00c4c060` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4c064"></a> `00c4c064` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c068"></a> `00c4c068` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4c06c"></a> `00c4c06c` | `69 01 00 54` | b.ls 0x00c4c098 | `CONDITIONAL_JUMP`
<a id="insn-00c4c070"></a> `00c4c070` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c074"></a> `00c4c074` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4c078"></a> `00c4c078` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4c07c"></a> `00c4c07c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4c080"></a> `00c4c080` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4c084"></a> `00c4c084` | `2f 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4c088"></a> `00c4c088` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4c08c"></a> `00c4c08c` | `60 04 00 b4` | cbz x0,0x00c4c118 | `CONDITIONAL_JUMP`
<a id="insn-00c4c090"></a> `00c4c090` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c094"></a> `00c4c094` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c098"></a> `00c4c098` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c09c"></a> `00c4c09c` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00c4c0a0"></a> `00c4c0a0` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4c0a4"></a> `00c4c0a4` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c0a8"></a> `00c4c0a8` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4c0ac"></a> `00c4c0ac` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4c0b0"></a> `00c4c0b0` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c0b4"></a> `00c4c0b4` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c0b8"></a> `00c4c0b8` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c4c0bc"></a> `00c4c0bc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00c4c0c0"></a> `00c4c0c0` | `69 01 00 54` | b.ls 0x00c4c0ec | `CONDITIONAL_JUMP`
<a id="insn-00c4c0c4"></a> `00c4c0c4` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c0c8"></a> `00c4c0c8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00c4c0cc"></a> `00c4c0cc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c4c0d0"></a> `00c4c0d0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00c4c0d4"></a> `00c4c0d4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c4c0d8"></a> `00c4c0d8` | `1a 3c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c4c0dc"></a> `00c4c0dc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00c4c0e0"></a> `00c4c0e0` | `e0 01 00 b4` | cbz x0,0x00c4c11c | `CONDITIONAL_JUMP`
<a id="insn-00c4c0e4"></a> `00c4c0e4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c0e8"></a> `00c4c0e8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c4c0ec"></a> `00c4c0ec` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c4c0f0"></a> `00c4c0f0` | `a9 0f 80 52` | mov w9,#0x7d | `FALL_THROUGH`
<a id="insn-00c4c0f4"></a> `00c4c0f4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00c4c0f8"></a> `00c4c0f8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4c0fc"></a> `00c4c0fc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4c100"></a> `00c4c100` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4c104"></a> `00c4c104` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4c108"></a> `00c4c108` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4c10c"></a> `00c4c10c` | `35 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c110"></a> `00c4c110` | `34 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c114"></a> `00c4c114` | `33 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c118"></a> `00c4c118` | `32 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c11c"></a> `00c4c11c` | `31 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c120"></a> `00c4c120` | `30 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c124"></a> `00c4c124` | `2f 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c4c128"></a> `00c4c128` | `2e 40 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4bddc`](#insn-00c4bddc) 範囲 `[['00c4bddc', '00c4be0b']]`
  - `CONDITIONAL_JUMP` [`00c4be08`](#insn-00c4be08) → [`00c4be38`](#insn-00c4be38)
  - `FALL_THROUGH` [`00c4be08`](#insn-00c4be08) → [`00c4be0c`](#insn-00c4be0c)
- ブロック [`00c4be0c`](#insn-00c4be0c) 範囲 `[['00c4be0c', '00c4be2f']]`
  - `CONDITIONAL_JUMP` [`00c4be2c`](#insn-00c4be2c) → [`00c4c10c`](#insn-00c4c10c)
  - `FALL_THROUGH` [`00c4be2c`](#insn-00c4be2c) → [`00c4be30`](#insn-00c4be30)
- ブロック [`00c4be30`](#insn-00c4be30) 範囲 `[['00c4be30', '00c4be37']]`
  - `FALL_THROUGH` [`00c4be34`](#insn-00c4be34) → [`00c4be38`](#insn-00c4be38)
- ブロック [`00c4be38`](#insn-00c4be38) 範囲 `[['00c4be38', '00c4be5f']]`
  - `CONDITIONAL_JUMP` [`00c4be5c`](#insn-00c4be5c) → [`00c4bf60`](#insn-00c4bf60)
  - `FALL_THROUGH` [`00c4be5c`](#insn-00c4be5c) → [`00c4be60`](#insn-00c4be60)
- ブロック [`00c4be60`](#insn-00c4be60) 範囲 `[['00c4be60', '00c4be73']]`
  - `CONDITIONAL_JUMP` [`00c4be70`](#insn-00c4be70) → [`00c4be9c`](#insn-00c4be9c)
  - `FALL_THROUGH` [`00c4be70`](#insn-00c4be70) → [`00c4be74`](#insn-00c4be74)
- ブロック [`00c4be74`](#insn-00c4be74) 範囲 `[['00c4be74', '00c4be93']]`
  - `CONDITIONAL_JUMP` [`00c4be90`](#insn-00c4be90) → [`00c4c120`](#insn-00c4c120)
  - `FALL_THROUGH` [`00c4be90`](#insn-00c4be90) → [`00c4be94`](#insn-00c4be94)
- ブロック [`00c4be94`](#insn-00c4be94) 範囲 `[['00c4be94', '00c4be9b']]`
  - `FALL_THROUGH` [`00c4be98`](#insn-00c4be98) → [`00c4be9c`](#insn-00c4be9c)
- ブロック [`00c4be9c`](#insn-00c4be9c) 範囲 `[['00c4be9c', '00c4bec7']]`
  - `CONDITIONAL_JUMP` [`00c4bec4`](#insn-00c4bec4) → [`00c4bef0`](#insn-00c4bef0)
  - `FALL_THROUGH` [`00c4bec4`](#insn-00c4bec4) → [`00c4bec8`](#insn-00c4bec8)
- ブロック [`00c4bec8`](#insn-00c4bec8) 範囲 `[['00c4bec8', '00c4bee7']]`
  - `CONDITIONAL_JUMP` [`00c4bee4`](#insn-00c4bee4) → [`00c4c124`](#insn-00c4c124)
  - `FALL_THROUGH` [`00c4bee4`](#insn-00c4bee4) → [`00c4bee8`](#insn-00c4bee8)
- ブロック [`00c4bee8`](#insn-00c4bee8) 範囲 `[['00c4bee8', '00c4beef']]`
  - `FALL_THROUGH` [`00c4beec`](#insn-00c4beec) → [`00c4bef0`](#insn-00c4bef0)
- ブロック [`00c4bef0`](#insn-00c4bef0) 範囲 `[['00c4bef0', '00c4bf27']]`
  - `CONDITIONAL_JUMP` [`00c4bf24`](#insn-00c4bf24) → [`00c4bf50`](#insn-00c4bf50)
  - `FALL_THROUGH` [`00c4bf24`](#insn-00c4bf24) → [`00c4bf28`](#insn-00c4bf28)
- ブロック [`00c4bf28`](#insn-00c4bf28) 範囲 `[['00c4bf28', '00c4bf47']]`
  - `CONDITIONAL_JUMP` [`00c4bf44`](#insn-00c4bf44) → [`00c4c128`](#insn-00c4c128)
  - `FALL_THROUGH` [`00c4bf44`](#insn-00c4bf44) → [`00c4bf48`](#insn-00c4bf48)
- ブロック [`00c4bf48`](#insn-00c4bf48) 範囲 `[['00c4bf48', '00c4bf4f']]`
  - `FALL_THROUGH` [`00c4bf4c`](#insn-00c4bf4c) → [`00c4bf50`](#insn-00c4bf50)
- ブロック [`00c4bf50`](#insn-00c4bf50) 範囲 `[['00c4bf50', '00c4bf5f']]`
  - `FALL_THROUGH` [`00c4bf5c`](#insn-00c4bf5c) → [`00c4bf60`](#insn-00c4bf60)
- ブロック [`00c4bf60`](#insn-00c4bf60) 範囲 `[['00c4bf60', '00c4bf73']]`
  - `CONDITIONAL_JUMP` [`00c4bf70`](#insn-00c4bf70) → [`00c4bf9c`](#insn-00c4bf9c)
  - `FALL_THROUGH` [`00c4bf70`](#insn-00c4bf70) → [`00c4bf74`](#insn-00c4bf74)
- ブロック [`00c4bf74`](#insn-00c4bf74) 範囲 `[['00c4bf74', '00c4bf93']]`
  - `CONDITIONAL_JUMP` [`00c4bf90`](#insn-00c4bf90) → [`00c4c110`](#insn-00c4c110)
  - `FALL_THROUGH` [`00c4bf90`](#insn-00c4bf90) → [`00c4bf94`](#insn-00c4bf94)
- ブロック [`00c4bf94`](#insn-00c4bf94) 範囲 `[['00c4bf94', '00c4bf9b']]`
  - `FALL_THROUGH` [`00c4bf98`](#insn-00c4bf98) → [`00c4bf9c`](#insn-00c4bf9c)
- ブロック [`00c4bf9c`](#insn-00c4bf9c) 範囲 `[['00c4bf9c', '00c4bfc7']]`
  - `CONDITIONAL_JUMP` [`00c4bfc4`](#insn-00c4bfc4) → [`00c4bff0`](#insn-00c4bff0)
  - `FALL_THROUGH` [`00c4bfc4`](#insn-00c4bfc4) → [`00c4bfc8`](#insn-00c4bfc8)
- ブロック [`00c4bfc8`](#insn-00c4bfc8) 範囲 `[['00c4bfc8', '00c4bfe7']]`
  - `CONDITIONAL_JUMP` [`00c4bfe4`](#insn-00c4bfe4) → [`00c4c114`](#insn-00c4c114)
  - `FALL_THROUGH` [`00c4bfe4`](#insn-00c4bfe4) → [`00c4bfe8`](#insn-00c4bfe8)
- ブロック [`00c4bfe8`](#insn-00c4bfe8) 範囲 `[['00c4bfe8', '00c4bfef']]`
  - `FALL_THROUGH` [`00c4bfec`](#insn-00c4bfec) → [`00c4bff0`](#insn-00c4bff0)
- ブロック [`00c4bff0`](#insn-00c4bff0) 範囲 `[['00c4bff0', '00c4c003']]`
  - `CONDITIONAL_JUMP` [`00c4c000`](#insn-00c4c000) → [`00c4c05c`](#insn-00c4c05c)
  - `FALL_THROUGH` [`00c4c000`](#insn-00c4c000) → [`00c4c004`](#insn-00c4c004)
- ブロック [`00c4c004`](#insn-00c4c004) 範囲 `[['00c4c004', '00c4c00f']]`
  - `UNCONDITIONAL_JUMP` [`00c4c00c`](#insn-00c4c00c) → [`00c4c01c`](#insn-00c4c01c)
- ブロック [`00c4c010`](#insn-00c4c010) 範囲 `[['00c4c010', '00c4c01b']]`
  - `CONDITIONAL_JUMP` [`00c4c018`](#insn-00c4c018) → [`00c4c05c`](#insn-00c4c05c)
  - `FALL_THROUGH` [`00c4c018`](#insn-00c4c018) → [`00c4c01c`](#insn-00c4c01c)
- ブロック [`00c4c01c`](#insn-00c4c01c) 範囲 `[['00c4c01c', '00c4c043']]`
  - `CONDITIONAL_JUMP` [`00c4c040`](#insn-00c4c040) → [`00c4c010`](#insn-00c4c010)
  - `FALL_THROUGH` [`00c4c040`](#insn-00c4c040) → [`00c4c044`](#insn-00c4c044)
- ブロック [`00c4c044`](#insn-00c4c044) 範囲 `[['00c4c044', '00c4c05b']]`
  - `UNCONDITIONAL_JUMP` [`00c4c058`](#insn-00c4c058) → [`00c4c010`](#insn-00c4c010)
- ブロック [`00c4c05c`](#insn-00c4c05c) 範囲 `[['00c4c05c', '00c4c06f']]`
  - `CONDITIONAL_JUMP` [`00c4c06c`](#insn-00c4c06c) → [`00c4c098`](#insn-00c4c098)
  - `FALL_THROUGH` [`00c4c06c`](#insn-00c4c06c) → [`00c4c070`](#insn-00c4c070)
- ブロック [`00c4c070`](#insn-00c4c070) 範囲 `[['00c4c070', '00c4c08f']]`
  - `CONDITIONAL_JUMP` [`00c4c08c`](#insn-00c4c08c) → [`00c4c118`](#insn-00c4c118)
  - `FALL_THROUGH` [`00c4c08c`](#insn-00c4c08c) → [`00c4c090`](#insn-00c4c090)
- ブロック [`00c4c090`](#insn-00c4c090) 範囲 `[['00c4c090', '00c4c097']]`
  - `FALL_THROUGH` [`00c4c094`](#insn-00c4c094) → [`00c4c098`](#insn-00c4c098)
- ブロック [`00c4c098`](#insn-00c4c098) 範囲 `[['00c4c098', '00c4c0c3']]`
  - `CONDITIONAL_JUMP` [`00c4c0c0`](#insn-00c4c0c0) → [`00c4c0ec`](#insn-00c4c0ec)
  - `FALL_THROUGH` [`00c4c0c0`](#insn-00c4c0c0) → [`00c4c0c4`](#insn-00c4c0c4)
- ブロック [`00c4c0c4`](#insn-00c4c0c4) 範囲 `[['00c4c0c4', '00c4c0e3']]`
  - `CONDITIONAL_JUMP` [`00c4c0e0`](#insn-00c4c0e0) → [`00c4c11c`](#insn-00c4c11c)
  - `FALL_THROUGH` [`00c4c0e0`](#insn-00c4c0e0) → [`00c4c0e4`](#insn-00c4c0e4)
- ブロック [`00c4c0e4`](#insn-00c4c0e4) 範囲 `[['00c4c0e4', '00c4c0eb']]`
  - `FALL_THROUGH` [`00c4c0e8`](#insn-00c4c0e8) → [`00c4c0ec`](#insn-00c4c0ec)
- ブロック [`00c4c0ec`](#insn-00c4c0ec) 範囲 `[['00c4c0ec', '00c4c10b']]`
- ブロック [`00c4c10c`](#insn-00c4c10c) 範囲 `[['00c4c10c', '00c4c10f']]`
- ブロック [`00c4c110`](#insn-00c4c110) 範囲 `[['00c4c110', '00c4c113']]`
- ブロック [`00c4c114`](#insn-00c4c114) 範囲 `[['00c4c114', '00c4c117']]`
- ブロック [`00c4c118`](#insn-00c4c118) 範囲 `[['00c4c118', '00c4c11b']]`
- ブロック [`00c4c11c`](#insn-00c4c11c) 範囲 `[['00c4c11c', '00c4c11f']]`
- ブロック [`00c4c120`](#insn-00c4c120) 範囲 `[['00c4c120', '00c4c123']]`
- ブロック [`00c4c124`](#insn-00c4c124) 範囲 `[['00c4c124', '00c4c127']]`
- ブロック [`00c4c128`](#insn-00c4c128) 範囲 `[['00c4c128', '00c4c12b']]`

## 命令位置別の参照

- [`00c4bde0`](#insn-00c4bde0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bde4`](#insn-00c4bde4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bde8`](#insn-00c4bde8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4be08`](#insn-00c4be08) → [`00c4be38`](#insn-00c4be38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4be24`](#insn-00c4be24) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4be2c`](#insn-00c4be2c) → [`00c4c10c`](#insn-00c4c10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4be5c`](#insn-00c4be5c) → [`00c4bf60`](#insn-00c4bf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4be70`](#insn-00c4be70) → [`00c4be9c`](#insn-00c4be9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4be88`](#insn-00c4be88) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4be90`](#insn-00c4be90) → [`00c4c120`](#insn-00c4c120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bec4`](#insn-00c4bec4) → [`00c4bef0`](#insn-00c4bef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bedc`](#insn-00c4bedc) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4bee4`](#insn-00c4bee4) → [`00c4c124`](#insn-00c4c124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf04`](#insn-00c4bf04) → [`00c461d4`](../00c46/00c461d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c461d4` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf24`](#insn-00c4bf24) → [`00c4bf50`](#insn-00c4bf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf3c`](#insn-00c4bf3c) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf44`](#insn-00c4bf44) → [`00c4c128`](#insn-00c4c128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf70`](#insn-00c4bf70) → [`00c4bf9c`](#insn-00c4bf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf88`](#insn-00c4bf88) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4bf90`](#insn-00c4bf90) → [`00c4c110`](#insn-00c4c110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bfc4`](#insn-00c4bfc4) → [`00c4bff0`](#insn-00c4bff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4bfdc`](#insn-00c4bfdc) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4bfe4`](#insn-00c4bfe4) → [`00c4c114`](#insn-00c4c114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c000`](#insn-00c4c000) → [`00c4c05c`](#insn-00c4c05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c00c`](#insn-00c4c00c) → [`00c4c01c`](#insn-00c4c01c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c018`](#insn-00c4c018) → [`00c4c05c`](#insn-00c4c05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c040`](#insn-00c4c040) → [`00c4c010`](#insn-00c4c010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c058`](#insn-00c4c058) → [`00c4c010`](#insn-00c4c010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c06c`](#insn-00c4c06c) → [`00c4c098`](#insn-00c4c098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c084`](#insn-00c4c084) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4c08c`](#insn-00c4c08c) → [`00c4c118`](#insn-00c4c118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c0c0`](#insn-00c4c0c0) → [`00c4c0ec`](#insn-00c4c0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c0d8`](#insn-00c4c0d8) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c4c0e0`](#insn-00c4c0e0) → [`00c4c11c`](#insn-00c4c11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c0f8`](#insn-00c4c0f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c0fc`](#insn-00c4c0fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c100`](#insn-00c4c100) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4c10c`](#insn-00c4c10c) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c110`](#insn-00c4c110) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c114`](#insn-00c4c114) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c118`](#insn-00c4c118) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c11c`](#insn-00c4c11c) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c120`](#insn-00c4c120) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c124`](#insn-00c4c124) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c4c128`](#insn-00c4c128) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4bde0`](#insn-00c4bde0)

~~~json
{
  "source": "00c4bde0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bde4`](#insn-00c4bde4)

~~~json
{
  "source": "00c4bde4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bde8`](#insn-00c4bde8)

~~~json
{
  "source": "00c4bde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4be08`](#insn-00c4be08)

~~~json
{
  "source": "00c4be08",
  "target": "00c4be38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4be24`](#insn-00c4be24)

~~~json
{
  "source": "00c4be24",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4be2c`](#insn-00c4be2c)

~~~json
{
  "source": "00c4be2c",
  "target": "00c4c10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4be5c`](#insn-00c4be5c)

~~~json
{
  "source": "00c4be5c",
  "target": "00c4bf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4be70`](#insn-00c4be70)

~~~json
{
  "source": "00c4be70",
  "target": "00c4be9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4be88`](#insn-00c4be88)

~~~json
{
  "source": "00c4be88",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4be90`](#insn-00c4be90)

~~~json
{
  "source": "00c4be90",
  "target": "00c4c120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bec4`](#insn-00c4bec4)

~~~json
{
  "source": "00c4bec4",
  "target": "00c4bef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bedc`](#insn-00c4bedc)

~~~json
{
  "source": "00c4bedc",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bee4`](#insn-00c4bee4)

~~~json
{
  "source": "00c4bee4",
  "target": "00c4c124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf04`](#insn-00c4bf04)

~~~json
{
  "source": "00c4bf04",
  "target": "00c461d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bf24`](#insn-00c4bf24)

~~~json
{
  "source": "00c4bf24",
  "target": "00c4bf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf3c`](#insn-00c4bf3c)

~~~json
{
  "source": "00c4bf3c",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bf44`](#insn-00c4bf44)

~~~json
{
  "source": "00c4bf44",
  "target": "00c4c128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf70`](#insn-00c4bf70)

~~~json
{
  "source": "00c4bf70",
  "target": "00c4bf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bf88`](#insn-00c4bf88)

~~~json
{
  "source": "00c4bf88",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bf90`](#insn-00c4bf90)

~~~json
{
  "source": "00c4bf90",
  "target": "00c4c110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bfc4`](#insn-00c4bfc4)

~~~json
{
  "source": "00c4bfc4",
  "target": "00c4bff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4bfdc`](#insn-00c4bfdc)

~~~json
{
  "source": "00c4bfdc",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4bfe4`](#insn-00c4bfe4)

~~~json
{
  "source": "00c4bfe4",
  "target": "00c4c114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c000`](#insn-00c4c000)

~~~json
{
  "source": "00c4c000",
  "target": "00c4c05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c00c`](#insn-00c4c00c)

~~~json
{
  "source": "00c4c00c",
  "target": "00c4c01c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c018`](#insn-00c4c018)

~~~json
{
  "source": "00c4c018",
  "target": "00c4c05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c040`](#insn-00c4c040)

~~~json
{
  "source": "00c4c040",
  "target": "00c4c010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c058`](#insn-00c4c058)

~~~json
{
  "source": "00c4c058",
  "target": "00c4c010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c06c`](#insn-00c4c06c)

~~~json
{
  "source": "00c4c06c",
  "target": "00c4c098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c084`](#insn-00c4c084)

~~~json
{
  "source": "00c4c084",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c08c`](#insn-00c4c08c)

~~~json
{
  "source": "00c4c08c",
  "target": "00c4c118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c0c0`](#insn-00c4c0c0)

~~~json
{
  "source": "00c4c0c0",
  "target": "00c4c0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c0d8`](#insn-00c4c0d8)

~~~json
{
  "source": "00c4c0d8",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c0e0`](#insn-00c4c0e0)

~~~json
{
  "source": "00c4c0e0",
  "target": "00c4c11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c0f8`](#insn-00c4c0f8)

~~~json
{
  "source": "00c4c0f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c0fc`](#insn-00c4c0fc)

~~~json
{
  "source": "00c4c0fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c100`](#insn-00c4c100)

~~~json
{
  "source": "00c4c100",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4c10c`](#insn-00c4c10c)

~~~json
{
  "source": "00c4c10c",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c110`](#insn-00c4c110)

~~~json
{
  "source": "00c4c110",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c114`](#insn-00c4c114)

~~~json
{
  "source": "00c4c114",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c118`](#insn-00c4c118)

~~~json
{
  "source": "00c4c118",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c11c`](#insn-00c4c11c)

~~~json
{
  "source": "00c4c11c",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c120`](#insn-00c4c120)

~~~json
{
  "source": "00c4c120",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c124`](#insn-00c4c124)

~~~json
{
  "source": "00c4c124",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4c128`](#insn-00c4c128)

~~~json
{
  "source": "00c4c128",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
