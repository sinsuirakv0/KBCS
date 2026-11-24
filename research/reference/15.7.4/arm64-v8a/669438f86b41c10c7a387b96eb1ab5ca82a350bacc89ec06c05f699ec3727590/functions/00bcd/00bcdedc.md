# 00bcdedc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcde98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-4cc919f41ad79050c9ea8e55e6e16a8a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4a924`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a924.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-e92b88742f43f8479cf24b77e68a728a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdedc",
  "name": "FUN_00bcdedc",
  "size": 848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d83a6f8459b23917cf3412cbd2396f933e0c9ccf10c735314896dc757d8ff22",
  "source_text_sha256": "9d83a6f8459b23917cf3412cbd2396f933e0c9ccf10c735314896dc757d8ff22",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdedc",
        "00bce22b"
      ]
    ],
    "bytes_sha256": "7b387480cd26c662540d88b3f5e8cbc414d53d24b6cb680d7a8676a333c82d88",
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

- [00bc82d4](../00bc8/00bc82d4.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6096 bytes

~~~c

void FUN_00bcdedc(long param_1,undefined8 *param_2)

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
                    /* try { // try from 00bcdf40 to 00ccdf5b has its CatchHandler @ 00bce588 */
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
                    /* try { // try from 00bcdfc8 to 00ccdfe3 has its CatchHandler @ 00bce584 */
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
    FUN_00bc82d4(param_1 + 0x10,param_2);
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
                    /* try { // try from 00bce050 to 00cce06b has its CatchHandler @ 00bce580 */
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
                    /* try { // try from 00bce0c8 to 00cce0e3 has its CatchHandler @ 00bce598 */
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
                    /* try { // try from 00bce140 to 00cce15b has its CatchHandler @ 00bce594 */
      if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
        (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      }
      lVar2 = lVar2 + -8;
      puVar8 = puVar8 + 1;
    } while (lVar2 != 0);
  }
                    /* try { // try from 00bce15c to 00cce237 has its CatchHandler @ 00bcde00 */
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
<a id="insn-00bcdedc"></a> `00bcdedc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcdee0"></a> `00bcdee0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcdee4"></a> `00bcdee4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdee8"></a> `00bcdee8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdeec"></a> `00bcdeec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcdef0"></a> `00bcdef0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdef4"></a> `00bcdef4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcdef8"></a> `00bcdef8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcdefc"></a> `00bcdefc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcdf00"></a> `00bcdf00` | `2b 21 00 91` | add x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdf04"></a> `00bcdf04` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcdf08"></a> `00bcdf08` | `89 01 00 54` | b.ls 0x00bcdf38 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf0c"></a> `00bcdf0c` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf10"></a> `00bcdf10` | `29 a1 0f 91` | add x9,x9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00bcdf14"></a> `00bcdf14` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdf18"></a> `00bcdf18` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcdf1c"></a> `00bcdf1c` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcdf20"></a> `00bcdf20` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf24"></a> `00bcdf24` | `cb 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf28"></a> `00bcdf28` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf2c"></a> `00bcdf2c` | `00 17 00 b4` | cbz x0,0x00bce20c | `CONDITIONAL_JUMP`
<a id="insn-00bcdf30"></a> `00bcdf30` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf34"></a> `00bcdf34` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcdf38"></a> `00bcdf38` | `4a ae 8c d2` | mov x10,#0x6572 | `FALL_THROUGH`
<a id="insn-00bcdf3c"></a> `00bcdf3c` | `2a ae ae f2` | movk x10,#0x7571, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcdf40"></a> `00bcdf40` | `2a 4d ce f2` | movk x10,#0x7269, LSL #32 | `FALL_THROUGH`
<a id="insn-00bcdf44"></a> `00bcdf44` | `aa 6c ee f2` | movk x10,#0x7365, LSL #48 | `FALL_THROUGH`
<a id="insn-00bcdf48"></a> `00bcdf48` | `0a 69 29 f8` | str x10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcdf4c"></a> `00bcdf4c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf50"></a> `00bcdf50` | `8a 0e 40 f9` | ldr x10,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdf54"></a> `00bcdf54` | `28 21 00 91` | add x8,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdf58"></a> `00bcdf58` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf5c"></a> `00bcdf5c` | `2a 08 00 b4` | cbz x10,0x00bce060 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf60"></a> `00bcdf60` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf64"></a> `00bcdf64` | `2a 25 00 91` | add x10,x9,#0x9 | `FALL_THROUGH`
<a id="insn-00bcdf68"></a> `00bcdf68` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf6c"></a> `00bcdf6c` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcdf70"></a> `00bcdf70` | `69 01 00 54` | b.ls 0x00bcdf9c | `CONDITIONAL_JUMP`
<a id="insn-00bcdf74"></a> `00bcdf74` | `68 f9 7f d3` | lsl x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf78"></a> `00bcdf78` | `29 a5 0f 91` | add x9,x9,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcdf7c"></a> `00bcdf7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdf80"></a> `00bcdf80` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcdf84"></a> `00bcdf84` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf88"></a> `00bcdf88` | `b2 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf8c"></a> `00bcdf8c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf90"></a> `00bcdf90` | `80 14 00 b4` | cbz x0,0x00bce220 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf94"></a> `00bcdf94` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf98"></a> `00bcdf98` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf9c"></a> `00bcdf9c` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfa0"></a> `00bcdfa0` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdfa4"></a> `00bcdfa4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdfa8"></a> `00bcdfa8` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfac"></a> `00bcdfac` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdfb0"></a> `00bcdfb0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdfb4"></a> `00bcdfb4` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfb8"></a> `00bcdfb8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfbc"></a> `00bcdfbc` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdfc0"></a> `00bcdfc0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdfc4"></a> `00bcdfc4` | `69 01 00 54` | b.ls 0x00bcdff0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfc8"></a> `00bcdfc8` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfcc"></a> `00bcdfcc` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdfd0"></a> `00bcdfd0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdfd4"></a> `00bcdfd4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdfd8"></a> `00bcdfd8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdfdc"></a> `00bcdfdc` | `9d 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdfe0"></a> `00bcdfe0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdfe4"></a> `00bcdfe4` | `00 12 00 b4` | cbz x0,0x00bce224 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfe8"></a> `00bcdfe8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfec"></a> `00bcdfec` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdff0"></a> `00bcdff0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdff4"></a> `00bcdff4` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdff8"></a> `00bcdff8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcdffc"></a> `00bcdffc` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce000"></a> `00bce000` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bce004"></a> `00bce004` | `b4 e8 ff 97` | bl 0x00bc82d4 | `UNCONDITIONAL_CALL`
<a id="insn-00bce008"></a> `00bce008` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce00c"></a> `00bce00c` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce010"></a> `00bce010` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce014"></a> `00bce014` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bce018"></a> `00bce018` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce01c"></a> `00bce01c` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce020"></a> `00bce020` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce024"></a> `00bce024` | `69 01 00 54` | b.ls 0x00bce050 | `CONDITIONAL_JUMP`
<a id="insn-00bce028"></a> `00bce028` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce02c"></a> `00bce02c` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce030"></a> `00bce030` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce034"></a> `00bce034` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce038"></a> `00bce038` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce03c"></a> `00bce03c` | `85 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bce040"></a> `00bce040` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce044"></a> `00bce044` | `20 0f 00 b4` | cbz x0,0x00bce228 | `CONDITIONAL_JUMP`
<a id="insn-00bce048"></a> `00bce048` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce04c"></a> `00bce04c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce050"></a> `00bce050` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce054"></a> `00bce054` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bce058"></a> `00bce058` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce05c"></a> `00bce05c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce060"></a> `00bce060` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce064"></a> `00bce064` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce068"></a> `00bce068` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce06c"></a> `00bce06c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce070"></a> `00bce070` | `69 01 00 54` | b.ls 0x00bce09c | `CONDITIONAL_JUMP`
<a id="insn-00bce074"></a> `00bce074` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce078"></a> `00bce078` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce07c"></a> `00bce07c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce080"></a> `00bce080` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce084"></a> `00bce084` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce088"></a> `00bce088` | `72 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bce08c"></a> `00bce08c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce090"></a> `00bce090` | `00 0c 00 b4` | cbz x0,0x00bce210 | `CONDITIONAL_JUMP`
<a id="insn-00bce094"></a> `00bce094` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce098"></a> `00bce098` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce09c"></a> `00bce09c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0a0"></a> `00bce0a0` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bce0a4"></a> `00bce0a4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce0a8"></a> `00bce0a8` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0ac"></a> `00bce0ac` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0b0"></a> `00bce0b0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce0b4"></a> `00bce0b4` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0b8"></a> `00bce0b8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0bc"></a> `00bce0bc` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0c0"></a> `00bce0c0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce0c4"></a> `00bce0c4` | `69 01 00 54` | b.ls 0x00bce0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bce0c8"></a> `00bce0c8` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0cc"></a> `00bce0cc` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce0d0"></a> `00bce0d0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce0d4"></a> `00bce0d4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce0d8"></a> `00bce0d8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce0dc"></a> `00bce0dc` | `5d 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bce0e0"></a> `00bce0e0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce0e4"></a> `00bce0e4` | `80 09 00 b4` | cbz x0,0x00bce214 | `CONDITIONAL_JUMP`
<a id="insn-00bce0e8"></a> `00bce0e8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0ec"></a> `00bce0ec` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0f0"></a> `00bce0f0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0f4"></a> `00bce0f4` | `69 0f 80 52` | mov w9,#0x7b | `FALL_THROUGH`
<a id="insn-00bce0f8"></a> `00bce0f8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce0fc"></a> `00bce0fc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bce100"></a> `00bce100` | `e8 02 00 b4` | cbz x8,0x00bce15c | `CONDITIONAL_JUMP`
<a id="insn-00bce104"></a> `00bce104` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bce108"></a> `00bce108` | `16 f1 7d d3` | lsl x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bce10c"></a> `00bce10c` | `04 00 00 14` | b 0x00bce11c | `UNCONDITIONAL_JUMP`
<a id="insn-00bce110"></a> `00bce110` | `d6 22 00 f1` | subs x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bce114"></a> `00bce114` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bce118"></a> `00bce118` | `20 02 00 54` | b.eq 0x00bce15c | `CONDITIONAL_JUMP`
<a id="insn-00bce11c"></a> `00bce11c` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00bce120"></a> `00bce120` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce124"></a> `00bce124` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce128"></a> `00bce128` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce12c"></a> `00bce12c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bce130"></a> `00bce130` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce134"></a> `00bce134` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bce138"></a> `00bce138` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bce13c"></a> `00bce13c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bce140"></a> `00bce140` | `80 fe ff 54` | b.eq 0x00bce110 | `CONDITIONAL_JUMP`
<a id="insn-00bce144"></a> `00bce144` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce148"></a> `00bce148` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce14c"></a> `00bce14c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce150"></a> `00bce150` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bce154"></a> `00bce154` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce158"></a> `00bce158` | `ee ff ff 17` | b 0x00bce110 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce15c"></a> `00bce15c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce160"></a> `00bce160` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce164"></a> `00bce164` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce168"></a> `00bce168` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce16c"></a> `00bce16c` | `69 01 00 54` | b.ls 0x00bce198 | `CONDITIONAL_JUMP`
<a id="insn-00bce170"></a> `00bce170` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce174"></a> `00bce174` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce178"></a> `00bce178` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce17c"></a> `00bce17c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce180"></a> `00bce180` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce184"></a> `00bce184` | `33 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bce188"></a> `00bce188` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce18c"></a> `00bce18c` | `60 04 00 b4` | cbz x0,0x00bce218 | `CONDITIONAL_JUMP`
<a id="insn-00bce190"></a> `00bce190` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce194"></a> `00bce194` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce198"></a> `00bce198` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce19c"></a> `00bce19c` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bce1a0"></a> `00bce1a0` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce1a4"></a> `00bce1a4` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce1a8"></a> `00bce1a8` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce1ac"></a> `00bce1ac` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce1b0"></a> `00bce1b0` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bce1b4"></a> `00bce1b4` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce1b8"></a> `00bce1b8` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce1bc"></a> `00bce1bc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce1c0"></a> `00bce1c0` | `69 01 00 54` | b.ls 0x00bce1ec | `CONDITIONAL_JUMP`
<a id="insn-00bce1c4"></a> `00bce1c4` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce1c8"></a> `00bce1c8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce1cc"></a> `00bce1cc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce1d0"></a> `00bce1d0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce1d4"></a> `00bce1d4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce1d8"></a> `00bce1d8` | `1e 3c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bce1dc"></a> `00bce1dc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce1e0"></a> `00bce1e0` | `e0 01 00 b4` | cbz x0,0x00bce21c | `CONDITIONAL_JUMP`
<a id="insn-00bce1e4"></a> `00bce1e4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce1e8"></a> `00bce1e8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce1ec"></a> `00bce1ec` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce1f0"></a> `00bce1f0` | `a9 0f 80 52` | mov w9,#0x7d | `FALL_THROUGH`
<a id="insn-00bce1f4"></a> `00bce1f4` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce1f8"></a> `00bce1f8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce1fc"></a> `00bce1fc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce200"></a> `00bce200` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bce204"></a> `00bce204` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce208"></a> `00bce208` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce20c"></a> `00bce20c` | `2d 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce210"></a> `00bce210` | `2c 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce214"></a> `00bce214` | `2b 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce218"></a> `00bce218` | `2a 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce21c"></a> `00bce21c` | `29 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce220"></a> `00bce220` | `28 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce224"></a> `00bce224` | `27 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bce228"></a> `00bce228` | `26 40 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdedc`](#insn-00bcdedc) 範囲 `[['00bcdedc', '00bcdf0b']]`
  - `CONDITIONAL_JUMP` [`00bcdf08`](#insn-00bcdf08) → [`00bcdf38`](#insn-00bcdf38)
  - `FALL_THROUGH` [`00bcdf08`](#insn-00bcdf08) → [`00bcdf0c`](#insn-00bcdf0c)
- ブロック [`00bcdf0c`](#insn-00bcdf0c) 範囲 `[['00bcdf0c', '00bcdf2f']]`
  - `CONDITIONAL_JUMP` [`00bcdf2c`](#insn-00bcdf2c) → [`00bce20c`](#insn-00bce20c)
  - `FALL_THROUGH` [`00bcdf2c`](#insn-00bcdf2c) → [`00bcdf30`](#insn-00bcdf30)
- ブロック [`00bcdf30`](#insn-00bcdf30) 範囲 `[['00bcdf30', '00bcdf37']]`
  - `FALL_THROUGH` [`00bcdf34`](#insn-00bcdf34) → [`00bcdf38`](#insn-00bcdf38)
- ブロック [`00bcdf38`](#insn-00bcdf38) 範囲 `[['00bcdf38', '00bcdf3f']]`
  - `FALL_THROUGH` [`00bcdf3c`](#insn-00bcdf3c) → [`00bcdf40`](#insn-00bcdf40)
- ブロック [`00bcdf40`](#insn-00bcdf40) 範囲 `[['00bcdf40', '00bcdf5f']]`
  - `CONDITIONAL_JUMP` [`00bcdf5c`](#insn-00bcdf5c) → [`00bce060`](#insn-00bce060)
  - `FALL_THROUGH` [`00bcdf5c`](#insn-00bcdf5c) → [`00bcdf60`](#insn-00bcdf60)
- ブロック [`00bcdf60`](#insn-00bcdf60) 範囲 `[['00bcdf60', '00bcdf73']]`
  - `CONDITIONAL_JUMP` [`00bcdf70`](#insn-00bcdf70) → [`00bcdf9c`](#insn-00bcdf9c)
  - `FALL_THROUGH` [`00bcdf70`](#insn-00bcdf70) → [`00bcdf74`](#insn-00bcdf74)
- ブロック [`00bcdf74`](#insn-00bcdf74) 範囲 `[['00bcdf74', '00bcdf93']]`
  - `CONDITIONAL_JUMP` [`00bcdf90`](#insn-00bcdf90) → [`00bce220`](#insn-00bce220)
  - `FALL_THROUGH` [`00bcdf90`](#insn-00bcdf90) → [`00bcdf94`](#insn-00bcdf94)
- ブロック [`00bcdf94`](#insn-00bcdf94) 範囲 `[['00bcdf94', '00bcdf9b']]`
  - `FALL_THROUGH` [`00bcdf98`](#insn-00bcdf98) → [`00bcdf9c`](#insn-00bcdf9c)
- ブロック [`00bcdf9c`](#insn-00bcdf9c) 範囲 `[['00bcdf9c', '00bcdfc7']]`
  - `CONDITIONAL_JUMP` [`00bcdfc4`](#insn-00bcdfc4) → [`00bcdff0`](#insn-00bcdff0)
  - `FALL_THROUGH` [`00bcdfc4`](#insn-00bcdfc4) → [`00bcdfc8`](#insn-00bcdfc8)
- ブロック [`00bcdfc8`](#insn-00bcdfc8) 範囲 `[['00bcdfc8', '00bcdfe7']]`
  - `CONDITIONAL_JUMP` [`00bcdfe4`](#insn-00bcdfe4) → [`00bce224`](#insn-00bce224)
  - `FALL_THROUGH` [`00bcdfe4`](#insn-00bcdfe4) → [`00bcdfe8`](#insn-00bcdfe8)
- ブロック [`00bcdfe8`](#insn-00bcdfe8) 範囲 `[['00bcdfe8', '00bcdfef']]`
  - `FALL_THROUGH` [`00bcdfec`](#insn-00bcdfec) → [`00bcdff0`](#insn-00bcdff0)
- ブロック [`00bcdff0`](#insn-00bcdff0) 範囲 `[['00bcdff0', '00bce027']]`
  - `CONDITIONAL_JUMP` [`00bce024`](#insn-00bce024) → [`00bce050`](#insn-00bce050)
  - `FALL_THROUGH` [`00bce024`](#insn-00bce024) → [`00bce028`](#insn-00bce028)
- ブロック [`00bce028`](#insn-00bce028) 範囲 `[['00bce028', '00bce047']]`
  - `CONDITIONAL_JUMP` [`00bce044`](#insn-00bce044) → [`00bce228`](#insn-00bce228)
  - `FALL_THROUGH` [`00bce044`](#insn-00bce044) → [`00bce048`](#insn-00bce048)
- ブロック [`00bce048`](#insn-00bce048) 範囲 `[['00bce048', '00bce04f']]`
  - `FALL_THROUGH` [`00bce04c`](#insn-00bce04c) → [`00bce050`](#insn-00bce050)
- ブロック [`00bce050`](#insn-00bce050) 範囲 `[['00bce050', '00bce05f']]`
  - `FALL_THROUGH` [`00bce05c`](#insn-00bce05c) → [`00bce060`](#insn-00bce060)
- ブロック [`00bce060`](#insn-00bce060) 範囲 `[['00bce060', '00bce073']]`
  - `CONDITIONAL_JUMP` [`00bce070`](#insn-00bce070) → [`00bce09c`](#insn-00bce09c)
  - `FALL_THROUGH` [`00bce070`](#insn-00bce070) → [`00bce074`](#insn-00bce074)
- ブロック [`00bce074`](#insn-00bce074) 範囲 `[['00bce074', '00bce093']]`
  - `CONDITIONAL_JUMP` [`00bce090`](#insn-00bce090) → [`00bce210`](#insn-00bce210)
  - `FALL_THROUGH` [`00bce090`](#insn-00bce090) → [`00bce094`](#insn-00bce094)
- ブロック [`00bce094`](#insn-00bce094) 範囲 `[['00bce094', '00bce09b']]`
  - `FALL_THROUGH` [`00bce098`](#insn-00bce098) → [`00bce09c`](#insn-00bce09c)
- ブロック [`00bce09c`](#insn-00bce09c) 範囲 `[['00bce09c', '00bce0c7']]`
  - `CONDITIONAL_JUMP` [`00bce0c4`](#insn-00bce0c4) → [`00bce0f0`](#insn-00bce0f0)
  - `FALL_THROUGH` [`00bce0c4`](#insn-00bce0c4) → [`00bce0c8`](#insn-00bce0c8)
- ブロック [`00bce0c8`](#insn-00bce0c8) 範囲 `[['00bce0c8', '00bce0e7']]`
  - `CONDITIONAL_JUMP` [`00bce0e4`](#insn-00bce0e4) → [`00bce214`](#insn-00bce214)
  - `FALL_THROUGH` [`00bce0e4`](#insn-00bce0e4) → [`00bce0e8`](#insn-00bce0e8)
- ブロック [`00bce0e8`](#insn-00bce0e8) 範囲 `[['00bce0e8', '00bce0ef']]`
  - `FALL_THROUGH` [`00bce0ec`](#insn-00bce0ec) → [`00bce0f0`](#insn-00bce0f0)
- ブロック [`00bce0f0`](#insn-00bce0f0) 範囲 `[['00bce0f0', '00bce103']]`
  - `CONDITIONAL_JUMP` [`00bce100`](#insn-00bce100) → [`00bce15c`](#insn-00bce15c)
  - `FALL_THROUGH` [`00bce100`](#insn-00bce100) → [`00bce104`](#insn-00bce104)
- ブロック [`00bce104`](#insn-00bce104) 範囲 `[['00bce104', '00bce10f']]`
  - `UNCONDITIONAL_JUMP` [`00bce10c`](#insn-00bce10c) → [`00bce11c`](#insn-00bce11c)
- ブロック [`00bce110`](#insn-00bce110) 範囲 `[['00bce110', '00bce11b']]`
  - `CONDITIONAL_JUMP` [`00bce118`](#insn-00bce118) → [`00bce15c`](#insn-00bce15c)
  - `FALL_THROUGH` [`00bce118`](#insn-00bce118) → [`00bce11c`](#insn-00bce11c)
- ブロック [`00bce11c`](#insn-00bce11c) 範囲 `[['00bce11c', '00bce13f']]`
  - `FALL_THROUGH` [`00bce13c`](#insn-00bce13c) → [`00bce140`](#insn-00bce140)
- ブロック [`00bce140`](#insn-00bce140) 範囲 `[['00bce140', '00bce143']]`
  - `CONDITIONAL_JUMP` [`00bce140`](#insn-00bce140) → [`00bce110`](#insn-00bce110)
  - `FALL_THROUGH` [`00bce140`](#insn-00bce140) → [`00bce144`](#insn-00bce144)
- ブロック [`00bce144`](#insn-00bce144) 範囲 `[['00bce144', '00bce15b']]`
  - `UNCONDITIONAL_JUMP` [`00bce158`](#insn-00bce158) → [`00bce110`](#insn-00bce110)
- ブロック [`00bce15c`](#insn-00bce15c) 範囲 `[['00bce15c', '00bce16f']]`
  - `CONDITIONAL_JUMP` [`00bce16c`](#insn-00bce16c) → [`00bce198`](#insn-00bce198)
  - `FALL_THROUGH` [`00bce16c`](#insn-00bce16c) → [`00bce170`](#insn-00bce170)
- ブロック [`00bce170`](#insn-00bce170) 範囲 `[['00bce170', '00bce18f']]`
  - `CONDITIONAL_JUMP` [`00bce18c`](#insn-00bce18c) → [`00bce218`](#insn-00bce218)
  - `FALL_THROUGH` [`00bce18c`](#insn-00bce18c) → [`00bce190`](#insn-00bce190)
- ブロック [`00bce190`](#insn-00bce190) 範囲 `[['00bce190', '00bce197']]`
  - `FALL_THROUGH` [`00bce194`](#insn-00bce194) → [`00bce198`](#insn-00bce198)
- ブロック [`00bce198`](#insn-00bce198) 範囲 `[['00bce198', '00bce1c3']]`
  - `CONDITIONAL_JUMP` [`00bce1c0`](#insn-00bce1c0) → [`00bce1ec`](#insn-00bce1ec)
  - `FALL_THROUGH` [`00bce1c0`](#insn-00bce1c0) → [`00bce1c4`](#insn-00bce1c4)
- ブロック [`00bce1c4`](#insn-00bce1c4) 範囲 `[['00bce1c4', '00bce1e3']]`
  - `CONDITIONAL_JUMP` [`00bce1e0`](#insn-00bce1e0) → [`00bce21c`](#insn-00bce21c)
  - `FALL_THROUGH` [`00bce1e0`](#insn-00bce1e0) → [`00bce1e4`](#insn-00bce1e4)
- ブロック [`00bce1e4`](#insn-00bce1e4) 範囲 `[['00bce1e4', '00bce1eb']]`
  - `FALL_THROUGH` [`00bce1e8`](#insn-00bce1e8) → [`00bce1ec`](#insn-00bce1ec)
- ブロック [`00bce1ec`](#insn-00bce1ec) 範囲 `[['00bce1ec', '00bce20b']]`
- ブロック [`00bce20c`](#insn-00bce20c) 範囲 `[['00bce20c', '00bce20f']]`
- ブロック [`00bce210`](#insn-00bce210) 範囲 `[['00bce210', '00bce213']]`
- ブロック [`00bce214`](#insn-00bce214) 範囲 `[['00bce214', '00bce217']]`
- ブロック [`00bce218`](#insn-00bce218) 範囲 `[['00bce218', '00bce21b']]`
- ブロック [`00bce21c`](#insn-00bce21c) 範囲 `[['00bce21c', '00bce21f']]`
- ブロック [`00bce220`](#insn-00bce220) 範囲 `[['00bce220', '00bce223']]`
- ブロック [`00bce224`](#insn-00bce224) 範囲 `[['00bce224', '00bce227']]`
- ブロック [`00bce228`](#insn-00bce228) 範囲 `[['00bce228', '00bce22b']]`

## 命令位置別の参照

- [`00bcdee0`](#insn-00bcdee0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdee4`](#insn-00bcdee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdee8`](#insn-00bcdee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf08`](#insn-00bcdf08) → [`00bcdf38`](#insn-00bcdf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf24`](#insn-00bcdf24) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf2c`](#insn-00bcdf2c) → [`00bce20c`](#insn-00bce20c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf5c`](#insn-00bcdf5c) → [`00bce060`](#insn-00bce060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf70`](#insn-00bcdf70) → [`00bcdf9c`](#insn-00bcdf9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf88`](#insn-00bcdf88) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf90`](#insn-00bcdf90) → [`00bce220`](#insn-00bce220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfc4`](#insn-00bcdfc4) → [`00bcdff0`](#insn-00bcdff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfdc`](#insn-00bcdfdc) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfe4`](#insn-00bcdfe4) → [`00bce224`](#insn-00bce224) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce004`](#insn-00bce004) → [`00bc82d4`](../00bc8/00bc82d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc82d4` · 推定シンボル `None` · 推定型 `None`
- [`00bce024`](#insn-00bce024) → [`00bce050`](#insn-00bce050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce03c`](#insn-00bce03c) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bce044`](#insn-00bce044) → [`00bce228`](#insn-00bce228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce070`](#insn-00bce070) → [`00bce09c`](#insn-00bce09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce088`](#insn-00bce088) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bce090`](#insn-00bce090) → [`00bce210`](#insn-00bce210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0c4`](#insn-00bce0c4) → [`00bce0f0`](#insn-00bce0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0dc`](#insn-00bce0dc) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bce0e4`](#insn-00bce0e4) → [`00bce214`](#insn-00bce214) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce100`](#insn-00bce100) → [`00bce15c`](#insn-00bce15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce10c`](#insn-00bce10c) → [`00bce11c`](#insn-00bce11c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce118`](#insn-00bce118) → [`00bce15c`](#insn-00bce15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce140`](#insn-00bce140) → [`00bce110`](#insn-00bce110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce158`](#insn-00bce158) → [`00bce110`](#insn-00bce110) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce16c`](#insn-00bce16c) → [`00bce198`](#insn-00bce198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce184`](#insn-00bce184) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bce18c`](#insn-00bce18c) → [`00bce218`](#insn-00bce218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1c0`](#insn-00bce1c0) → [`00bce1ec`](#insn-00bce1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1d8`](#insn-00bce1d8) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bce1e0`](#insn-00bce1e0) → [`00bce21c`](#insn-00bce21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1f8`](#insn-00bce1f8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1fc`](#insn-00bce1fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce200`](#insn-00bce200) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce20c`](#insn-00bce20c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce210`](#insn-00bce210) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce214`](#insn-00bce214) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce218`](#insn-00bce218) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce21c`](#insn-00bce21c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce220`](#insn-00bce220) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce224`](#insn-00bce224) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce228`](#insn-00bce228) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdee0`](#insn-00bcdee0)

~~~json
{
  "source": "00bcdee0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdee4`](#insn-00bcdee4)

~~~json
{
  "source": "00bcdee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdee8`](#insn-00bcdee8)

~~~json
{
  "source": "00bcdee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf08`](#insn-00bcdf08)

~~~json
{
  "source": "00bcdf08",
  "target": "00bcdf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf24`](#insn-00bcdf24)

~~~json
{
  "source": "00bcdf24",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf2c`](#insn-00bcdf2c)

~~~json
{
  "source": "00bcdf2c",
  "target": "00bce20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf5c`](#insn-00bcdf5c)

~~~json
{
  "source": "00bcdf5c",
  "target": "00bce060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf70`](#insn-00bcdf70)

~~~json
{
  "source": "00bcdf70",
  "target": "00bcdf9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf88`](#insn-00bcdf88)

~~~json
{
  "source": "00bcdf88",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf90`](#insn-00bcdf90)

~~~json
{
  "source": "00bcdf90",
  "target": "00bce220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfc4`](#insn-00bcdfc4)

~~~json
{
  "source": "00bcdfc4",
  "target": "00bcdff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfdc`](#insn-00bcdfdc)

~~~json
{
  "source": "00bcdfdc",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdfe4`](#insn-00bcdfe4)

~~~json
{
  "source": "00bcdfe4",
  "target": "00bce224",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce004`](#insn-00bce004)

~~~json
{
  "source": "00bce004",
  "target": "00bc82d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce024`](#insn-00bce024)

~~~json
{
  "source": "00bce024",
  "target": "00bce050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce03c`](#insn-00bce03c)

~~~json
{
  "source": "00bce03c",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce044`](#insn-00bce044)

~~~json
{
  "source": "00bce044",
  "target": "00bce228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce070`](#insn-00bce070)

~~~json
{
  "source": "00bce070",
  "target": "00bce09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce088`](#insn-00bce088)

~~~json
{
  "source": "00bce088",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce090`](#insn-00bce090)

~~~json
{
  "source": "00bce090",
  "target": "00bce210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0c4`](#insn-00bce0c4)

~~~json
{
  "source": "00bce0c4",
  "target": "00bce0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0dc`](#insn-00bce0dc)

~~~json
{
  "source": "00bce0dc",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce0e4`](#insn-00bce0e4)

~~~json
{
  "source": "00bce0e4",
  "target": "00bce214",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce100`](#insn-00bce100)

~~~json
{
  "source": "00bce100",
  "target": "00bce15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce10c`](#insn-00bce10c)

~~~json
{
  "source": "00bce10c",
  "target": "00bce11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce118`](#insn-00bce118)

~~~json
{
  "source": "00bce118",
  "target": "00bce15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce140`](#insn-00bce140)

~~~json
{
  "source": "00bce140",
  "target": "00bce110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce158`](#insn-00bce158)

~~~json
{
  "source": "00bce158",
  "target": "00bce110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce16c`](#insn-00bce16c)

~~~json
{
  "source": "00bce16c",
  "target": "00bce198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce184`](#insn-00bce184)

~~~json
{
  "source": "00bce184",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce18c`](#insn-00bce18c)

~~~json
{
  "source": "00bce18c",
  "target": "00bce218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1c0`](#insn-00bce1c0)

~~~json
{
  "source": "00bce1c0",
  "target": "00bce1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1d8`](#insn-00bce1d8)

~~~json
{
  "source": "00bce1d8",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce1e0`](#insn-00bce1e0)

~~~json
{
  "source": "00bce1e0",
  "target": "00bce21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1f8`](#insn-00bce1f8)

~~~json
{
  "source": "00bce1f8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1fc`](#insn-00bce1fc)

~~~json
{
  "source": "00bce1fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce200`](#insn-00bce200)

~~~json
{
  "source": "00bce200",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce20c`](#insn-00bce20c)

~~~json
{
  "source": "00bce20c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce210`](#insn-00bce210)

~~~json
{
  "source": "00bce210",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce214`](#insn-00bce214)

~~~json
{
  "source": "00bce214",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce218`](#insn-00bce218)

~~~json
{
  "source": "00bce218",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce21c`](#insn-00bce21c)

~~~json
{
  "source": "00bce21c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce220`](#insn-00bce220)

~~~json
{
  "source": "00bce220",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce224`](#insn-00bce224)

~~~json
{
  "source": "00bce224",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce228`](#insn-00bce228)

~~~json
{
  "source": "00bce228",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
