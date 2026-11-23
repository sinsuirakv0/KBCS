# 00bcddd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcde98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcde98.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-48128768252a0ea1a713c93e4380ac2e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcddd0",
  "name": "FUN_00bcddd0",
  "size": 848,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b28510dc99e292136b1e2bf717891c9db0c39fb66cdfacd38ccf1fed4cb352b",
  "source_text_sha256": "0b28510dc99e292136b1e2bf717891c9db0c39fb66cdfacd38ccf1fed4cb352b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcddd0",
        "00bce11f"
      ]
    ],
    "bytes_sha256": "230bd902f9fe992d73380a0b6edb467ef684f0e3f09cf5548fc893dbc1770fa6",
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

- [00bc81c8](../00bc8/00bc81c8.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6096 bytes

~~~c

void FUN_00bcddd0(long param_1,undefined8 *param_2)

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
                    /* try { // try from 00bcde34 to 00ccde4f has its CatchHandler @ 00bce47c */
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
                    /* try { // try from 00bcdebc to 00ccded7 has its CatchHandler @ 00bce478 */
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
    FUN_00bc81c8(param_1 + 0x10,param_2);
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
                    /* try { // try from 00bcdf44 to 00ccdf5f has its CatchHandler @ 00bce474 */
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
                    /* try { // try from 00bcdfbc to 00ccdfd7 has its CatchHandler @ 00bce48c */
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
                    /* try { // try from 00bce034 to 00cce04f has its CatchHandler @ 00bce488 */
      if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
        (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
      }
      lVar2 = lVar2 + -8;
      puVar8 = puVar8 + 1;
    } while (lVar2 != 0);
  }
                    /* try { // try from 00bce050 to 00cce12b has its CatchHandler @ 00bcdcf4 */
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
<a id="insn-00bcddd0"></a> `00bcddd0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcddd4"></a> `00bcddd4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdddc"></a> `00bcdddc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdde0"></a> `00bcdde0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcdde4"></a> `00bcdde4` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdde8"></a> `00bcdde8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcddf0"></a> `00bcddf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcddf4"></a> `00bcddf4` | `2b 21 00 91` | add x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcddf8"></a> `00bcddf8` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcddfc"></a> `00bcddfc` | `89 01 00 54` | b.ls 0x00bcde2c | `CONDITIONAL_JUMP`
<a id="insn-00bcde00"></a> `00bcde00` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde04"></a> `00bcde04` | `29 a1 0f 91` | add x9,x9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00bcde08"></a> `00bcde08` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcde0c"></a> `00bcde0c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcde10"></a> `00bcde10` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcde14"></a> `00bcde14` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcde18"></a> `00bcde18` | `ce 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde1c"></a> `00bcde1c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcde20"></a> `00bcde20` | `00 17 00 b4` | cbz x0,0x00bce100 | `CONDITIONAL_JUMP`
<a id="insn-00bcde24"></a> `00bcde24` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde28"></a> `00bcde28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcde2c"></a> `00bcde2c` | `4a ae 8c d2` | mov x10,#0x6572 | `FALL_THROUGH`
<a id="insn-00bcde30"></a> `00bcde30` | `2a ae ae f2` | movk x10,#0x7571, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcde34"></a> `00bcde34` | `2a 4d ce f2` | movk x10,#0x7269, LSL #32 | `FALL_THROUGH`
<a id="insn-00bcde38"></a> `00bcde38` | `aa 6c ee f2` | movk x10,#0x7365, LSL #48 | `FALL_THROUGH`
<a id="insn-00bcde3c"></a> `00bcde3c` | `0a 69 29 f8` | str x10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcde40"></a> `00bcde40` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde44"></a> `00bcde44` | `8a 0e 40 f9` | ldr x10,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde48"></a> `00bcde48` | `28 21 00 91` | add x8,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcde4c"></a> `00bcde4c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde50"></a> `00bcde50` | `2a 08 00 b4` | cbz x10,0x00bcdf54 | `CONDITIONAL_JUMP`
<a id="insn-00bcde54"></a> `00bcde54` | `6b 0a 40 f9` | ldr x11,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcde58"></a> `00bcde58` | `2a 25 00 91` | add x10,x9,#0x9 | `FALL_THROUGH`
<a id="insn-00bcde5c"></a> `00bcde5c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcde60"></a> `00bcde60` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcde64"></a> `00bcde64` | `69 01 00 54` | b.ls 0x00bcde90 | `CONDITIONAL_JUMP`
<a id="insn-00bcde68"></a> `00bcde68` | `68 f9 7f d3` | lsl x8,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde6c"></a> `00bcde6c` | `29 a5 0f 91` | add x9,x9,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcde70"></a> `00bcde70` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcde74"></a> `00bcde74` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcde78"></a> `00bcde78` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcde7c"></a> `00bcde7c` | `b5 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde80"></a> `00bcde80` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcde84"></a> `00bcde84` | `80 14 00 b4` | cbz x0,0x00bce114 | `CONDITIONAL_JUMP`
<a id="insn-00bcde88"></a> `00bcde88` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde8c"></a> `00bcde8c` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde90"></a> `00bcde90` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcde94"></a> `00bcde94` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcde98"></a> `00bcde98` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcde9c"></a> `00bcde9c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdea0"></a> `00bcdea0` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdea4"></a> `00bcdea4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdea8"></a> `00bcdea8` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdeac"></a> `00bcdeac` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdeb0"></a> `00bcdeb0` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdeb4"></a> `00bcdeb4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdeb8"></a> `00bcdeb8` | `69 01 00 54` | b.ls 0x00bcdee4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdebc"></a> `00bcdebc` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdec0"></a> `00bcdec0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdec4"></a> `00bcdec4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdec8"></a> `00bcdec8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdecc"></a> `00bcdecc` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcded0"></a> `00bcded0` | `a0 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcded4"></a> `00bcded4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcded8"></a> `00bcded8` | `00 12 00 b4` | cbz x0,0x00bce118 | `CONDITIONAL_JUMP`
<a id="insn-00bcdedc"></a> `00bcdedc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdee0"></a> `00bcdee0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdee4"></a> `00bcdee4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdee8"></a> `00bcdee8` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bcdeec"></a> `00bcdeec` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcdef0"></a> `00bcdef0` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdef4"></a> `00bcdef4` | `80 42 00 91` | add x0,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdef8"></a> `00bcdef8` | `b4 e8 ff 97` | bl 0x00bc81c8 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdefc"></a> `00bcdefc` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf00"></a> `00bcdf00` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdf04"></a> `00bcdf04` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf08"></a> `00bcdf08` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf0c"></a> `00bcdf0c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf10"></a> `00bcdf10` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdf14"></a> `00bcdf14` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdf18"></a> `00bcdf18` | `69 01 00 54` | b.ls 0x00bcdf44 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf1c"></a> `00bcdf1c` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf20"></a> `00bcdf20` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdf24"></a> `00bcdf24` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdf28"></a> `00bcdf28` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdf2c"></a> `00bcdf2c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf30"></a> `00bcdf30` | `88 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf34"></a> `00bcdf34` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf38"></a> `00bcdf38` | `20 0f 00 b4` | cbz x0,0x00bce11c | `CONDITIONAL_JUMP`
<a id="insn-00bcdf3c"></a> `00bcdf3c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf40"></a> `00bcdf40` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf44"></a> `00bcdf44` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf48"></a> `00bcdf48` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bcdf4c"></a> `00bcdf4c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdf50"></a> `00bcdf50` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf54"></a> `00bcdf54` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf58"></a> `00bcdf58` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf5c"></a> `00bcdf5c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf60"></a> `00bcdf60` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdf64"></a> `00bcdf64` | `69 01 00 54` | b.ls 0x00bcdf90 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf68"></a> `00bcdf68` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf6c"></a> `00bcdf6c` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdf70"></a> `00bcdf70` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdf74"></a> `00bcdf74` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdf78"></a> `00bcdf78` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdf7c"></a> `00bcdf7c` | `75 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf80"></a> `00bcdf80` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf84"></a> `00bcdf84` | `00 0c 00 b4` | cbz x0,0x00bce104 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf88"></a> `00bcdf88` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf8c"></a> `00bcdf8c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf90"></a> `00bcdf90` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdf94"></a> `00bcdf94` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdf98"></a> `00bcdf98` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdf9c"></a> `00bcdf9c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfa0"></a> `00bcdfa0` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdfa4"></a> `00bcdfa4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdfa8"></a> `00bcdfa8` | `6b 05 00 11` | add w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfac"></a> `00bcdfac` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfb0"></a> `00bcdfb0` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdfb4"></a> `00bcdfb4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdfb8"></a> `00bcdfb8` | `69 01 00 54` | b.ls 0x00bcdfe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfbc"></a> `00bcdfbc` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfc0"></a> `00bcdfc0` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdfc4"></a> `00bcdfc4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdfc8"></a> `00bcdfc8` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdfcc"></a> `00bcdfcc` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdfd0"></a> `00bcdfd0` | `60 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdfd4"></a> `00bcdfd4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdfd8"></a> `00bcdfd8` | `80 09 00 b4` | cbz x0,0x00bce108 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfdc"></a> `00bcdfdc` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfe0"></a> `00bcdfe0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfe4"></a> `00bcdfe4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfe8"></a> `00bcdfe8` | `69 0f 80 52` | mov w9,#0x7b | `FALL_THROUGH`
<a id="insn-00bcdfec"></a> `00bcdfec` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcdff0"></a> `00bcdff0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdff4"></a> `00bcdff4` | `e8 02 00 b4` | cbz x8,0x00bce050 | `CONDITIONAL_JUMP`
<a id="insn-00bcdff8"></a> `00bcdff8` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdffc"></a> `00bcdffc` | `16 f1 7d d3` | lsl x22,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bce000"></a> `00bce000` | `04 00 00 14` | b 0x00bce010 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce004"></a> `00bce004` | `d6 22 00 f1` | subs x22,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bce008"></a> `00bce008` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bce00c"></a> `00bce00c` | `20 02 00 54` | b.eq 0x00bce050 | `CONDITIONAL_JUMP`
<a id="insn-00bce010"></a> `00bce010` | `b4 02 40 f9` | ldr x20,[x21] | `FALL_THROUGH`
<a id="insn-00bce014"></a> `00bce014` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce018"></a> `00bce018` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce01c"></a> `00bce01c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce020"></a> `00bce020` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bce024"></a> `00bce024` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce028"></a> `00bce028` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bce02c"></a> `00bce02c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bce030"></a> `00bce030` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bce034"></a> `00bce034` | `80 fe ff 54` | b.eq 0x00bce004 | `CONDITIONAL_JUMP`
<a id="insn-00bce038"></a> `00bce038` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce03c"></a> `00bce03c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce040"></a> `00bce040` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce044"></a> `00bce044` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bce048"></a> `00bce048` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce04c"></a> `00bce04c` | `ee ff ff 17` | b 0x00bce004 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce050"></a> `00bce050` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce054"></a> `00bce054` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce058"></a> `00bce058` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce05c"></a> `00bce05c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce060"></a> `00bce060` | `69 01 00 54` | b.ls 0x00bce08c | `CONDITIONAL_JUMP`
<a id="insn-00bce064"></a> `00bce064` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce068"></a> `00bce068` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce06c"></a> `00bce06c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce070"></a> `00bce070` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce074"></a> `00bce074` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce078"></a> `00bce078` | `36 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bce07c"></a> `00bce07c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce080"></a> `00bce080` | `60 04 00 b4` | cbz x0,0x00bce10c | `CONDITIONAL_JUMP`
<a id="insn-00bce084"></a> `00bce084` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce088"></a> `00bce088` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce08c"></a> `00bce08c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce090"></a> `00bce090` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bce094"></a> `00bce094` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce098"></a> `00bce098` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce09c"></a> `00bce09c` | `6b 22 40 b9` | ldr w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0a0"></a> `00bce0a0` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce0a4"></a> `00bce0a4` | `6b 05 00 51` | sub w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0a8"></a> `00bce0a8` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0ac"></a> `00bce0ac` | `6b 22 00 b9` | str w11,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0b0"></a> `00bce0b0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bce0b4"></a> `00bce0b4` | `69 01 00 54` | b.ls 0x00bce0e0 | `CONDITIONAL_JUMP`
<a id="insn-00bce0b8"></a> `00bce0b8` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0bc"></a> `00bce0bc` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bce0c0"></a> `00bce0c0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bce0c4"></a> `00bce0c4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bce0c8"></a> `00bce0c8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce0cc"></a> `00bce0cc` | `21 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bce0d0"></a> `00bce0d0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce0d4"></a> `00bce0d4` | `e0 01 00 b4` | cbz x0,0x00bce110 | `CONDITIONAL_JUMP`
<a id="insn-00bce0d8"></a> `00bce0d8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0dc"></a> `00bce0dc` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce0e0"></a> `00bce0e0` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce0e4"></a> `00bce0e4` | `a9 0f 80 52` | mov w9,#0x7d | `FALL_THROUGH`
<a id="insn-00bce0e8"></a> `00bce0e8` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bce0ec"></a> `00bce0ec` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0f0"></a> `00bce0f0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce0f4"></a> `00bce0f4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bce0f8"></a> `00bce0f8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce0fc"></a> `00bce0fc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce100"></a> `00bce100` | `30 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce104"></a> `00bce104` | `2f 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce108"></a> `00bce108` | `2e 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce10c"></a> `00bce10c` | `2d 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce110"></a> `00bce110` | `2c 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce114"></a> `00bce114` | `2b 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce118"></a> `00bce118` | `2a 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bce11c"></a> `00bce11c` | `29 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcddd0`](#insn-00bcddd0) 範囲 `[['00bcddd0', '00bcddff']]`
  - `CONDITIONAL_JUMP` [`00bcddfc`](#insn-00bcddfc) → [`00bcde2c`](#insn-00bcde2c)
  - `FALL_THROUGH` [`00bcddfc`](#insn-00bcddfc) → [`00bcde00`](#insn-00bcde00)
- ブロック [`00bcde00`](#insn-00bcde00) 範囲 `[['00bcde00', '00bcde23']]`
  - `CONDITIONAL_JUMP` [`00bcde20`](#insn-00bcde20) → [`00bce100`](#insn-00bce100)
  - `FALL_THROUGH` [`00bcde20`](#insn-00bcde20) → [`00bcde24`](#insn-00bcde24)
- ブロック [`00bcde24`](#insn-00bcde24) 範囲 `[['00bcde24', '00bcde2b']]`
  - `FALL_THROUGH` [`00bcde28`](#insn-00bcde28) → [`00bcde2c`](#insn-00bcde2c)
- ブロック [`00bcde2c`](#insn-00bcde2c) 範囲 `[['00bcde2c', '00bcde33']]`
  - `FALL_THROUGH` [`00bcde30`](#insn-00bcde30) → [`00bcde34`](#insn-00bcde34)
- ブロック [`00bcde34`](#insn-00bcde34) 範囲 `[['00bcde34', '00bcde53']]`
  - `CONDITIONAL_JUMP` [`00bcde50`](#insn-00bcde50) → [`00bcdf54`](#insn-00bcdf54)
  - `FALL_THROUGH` [`00bcde50`](#insn-00bcde50) → [`00bcde54`](#insn-00bcde54)
- ブロック [`00bcde54`](#insn-00bcde54) 範囲 `[['00bcde54', '00bcde67']]`
  - `CONDITIONAL_JUMP` [`00bcde64`](#insn-00bcde64) → [`00bcde90`](#insn-00bcde90)
  - `FALL_THROUGH` [`00bcde64`](#insn-00bcde64) → [`00bcde68`](#insn-00bcde68)
- ブロック [`00bcde68`](#insn-00bcde68) 範囲 `[['00bcde68', '00bcde87']]`
  - `CONDITIONAL_JUMP` [`00bcde84`](#insn-00bcde84) → [`00bce114`](#insn-00bce114)
  - `FALL_THROUGH` [`00bcde84`](#insn-00bcde84) → [`00bcde88`](#insn-00bcde88)
- ブロック [`00bcde88`](#insn-00bcde88) 範囲 `[['00bcde88', '00bcde8f']]`
  - `FALL_THROUGH` [`00bcde8c`](#insn-00bcde8c) → [`00bcde90`](#insn-00bcde90)
- ブロック [`00bcde90`](#insn-00bcde90) 範囲 `[['00bcde90', '00bcdebb']]`
  - `CONDITIONAL_JUMP` [`00bcdeb8`](#insn-00bcdeb8) → [`00bcdee4`](#insn-00bcdee4)
  - `FALL_THROUGH` [`00bcdeb8`](#insn-00bcdeb8) → [`00bcdebc`](#insn-00bcdebc)
- ブロック [`00bcdebc`](#insn-00bcdebc) 範囲 `[['00bcdebc', '00bcdedb']]`
  - `CONDITIONAL_JUMP` [`00bcded8`](#insn-00bcded8) → [`00bce118`](#insn-00bce118)
  - `FALL_THROUGH` [`00bcded8`](#insn-00bcded8) → [`00bcdedc`](#insn-00bcdedc)
- ブロック [`00bcdedc`](#insn-00bcdedc) 範囲 `[['00bcdedc', '00bcdee3']]`
  - `FALL_THROUGH` [`00bcdee0`](#insn-00bcdee0) → [`00bcdee4`](#insn-00bcdee4)
- ブロック [`00bcdee4`](#insn-00bcdee4) 範囲 `[['00bcdee4', '00bcdf1b']]`
  - `CONDITIONAL_JUMP` [`00bcdf18`](#insn-00bcdf18) → [`00bcdf44`](#insn-00bcdf44)
  - `FALL_THROUGH` [`00bcdf18`](#insn-00bcdf18) → [`00bcdf1c`](#insn-00bcdf1c)
- ブロック [`00bcdf1c`](#insn-00bcdf1c) 範囲 `[['00bcdf1c', '00bcdf3b']]`
  - `CONDITIONAL_JUMP` [`00bcdf38`](#insn-00bcdf38) → [`00bce11c`](#insn-00bce11c)
  - `FALL_THROUGH` [`00bcdf38`](#insn-00bcdf38) → [`00bcdf3c`](#insn-00bcdf3c)
- ブロック [`00bcdf3c`](#insn-00bcdf3c) 範囲 `[['00bcdf3c', '00bcdf43']]`
  - `FALL_THROUGH` [`00bcdf40`](#insn-00bcdf40) → [`00bcdf44`](#insn-00bcdf44)
- ブロック [`00bcdf44`](#insn-00bcdf44) 範囲 `[['00bcdf44', '00bcdf53']]`
  - `FALL_THROUGH` [`00bcdf50`](#insn-00bcdf50) → [`00bcdf54`](#insn-00bcdf54)
- ブロック [`00bcdf54`](#insn-00bcdf54) 範囲 `[['00bcdf54', '00bcdf67']]`
  - `CONDITIONAL_JUMP` [`00bcdf64`](#insn-00bcdf64) → [`00bcdf90`](#insn-00bcdf90)
  - `FALL_THROUGH` [`00bcdf64`](#insn-00bcdf64) → [`00bcdf68`](#insn-00bcdf68)
- ブロック [`00bcdf68`](#insn-00bcdf68) 範囲 `[['00bcdf68', '00bcdf87']]`
  - `CONDITIONAL_JUMP` [`00bcdf84`](#insn-00bcdf84) → [`00bce104`](#insn-00bce104)
  - `FALL_THROUGH` [`00bcdf84`](#insn-00bcdf84) → [`00bcdf88`](#insn-00bcdf88)
- ブロック [`00bcdf88`](#insn-00bcdf88) 範囲 `[['00bcdf88', '00bcdf8f']]`
  - `FALL_THROUGH` [`00bcdf8c`](#insn-00bcdf8c) → [`00bcdf90`](#insn-00bcdf90)
- ブロック [`00bcdf90`](#insn-00bcdf90) 範囲 `[['00bcdf90', '00bcdfbb']]`
  - `CONDITIONAL_JUMP` [`00bcdfb8`](#insn-00bcdfb8) → [`00bcdfe4`](#insn-00bcdfe4)
  - `FALL_THROUGH` [`00bcdfb8`](#insn-00bcdfb8) → [`00bcdfbc`](#insn-00bcdfbc)
- ブロック [`00bcdfbc`](#insn-00bcdfbc) 範囲 `[['00bcdfbc', '00bcdfdb']]`
  - `CONDITIONAL_JUMP` [`00bcdfd8`](#insn-00bcdfd8) → [`00bce108`](#insn-00bce108)
  - `FALL_THROUGH` [`00bcdfd8`](#insn-00bcdfd8) → [`00bcdfdc`](#insn-00bcdfdc)
- ブロック [`00bcdfdc`](#insn-00bcdfdc) 範囲 `[['00bcdfdc', '00bcdfe3']]`
  - `FALL_THROUGH` [`00bcdfe0`](#insn-00bcdfe0) → [`00bcdfe4`](#insn-00bcdfe4)
- ブロック [`00bcdfe4`](#insn-00bcdfe4) 範囲 `[['00bcdfe4', '00bcdff7']]`
  - `CONDITIONAL_JUMP` [`00bcdff4`](#insn-00bcdff4) → [`00bce050`](#insn-00bce050)
  - `FALL_THROUGH` [`00bcdff4`](#insn-00bcdff4) → [`00bcdff8`](#insn-00bcdff8)
- ブロック [`00bcdff8`](#insn-00bcdff8) 範囲 `[['00bcdff8', '00bce003']]`
  - `UNCONDITIONAL_JUMP` [`00bce000`](#insn-00bce000) → [`00bce010`](#insn-00bce010)
- ブロック [`00bce004`](#insn-00bce004) 範囲 `[['00bce004', '00bce00f']]`
  - `CONDITIONAL_JUMP` [`00bce00c`](#insn-00bce00c) → [`00bce050`](#insn-00bce050)
  - `FALL_THROUGH` [`00bce00c`](#insn-00bce00c) → [`00bce010`](#insn-00bce010)
- ブロック [`00bce010`](#insn-00bce010) 範囲 `[['00bce010', '00bce033']]`
  - `FALL_THROUGH` [`00bce030`](#insn-00bce030) → [`00bce034`](#insn-00bce034)
- ブロック [`00bce034`](#insn-00bce034) 範囲 `[['00bce034', '00bce037']]`
  - `CONDITIONAL_JUMP` [`00bce034`](#insn-00bce034) → [`00bce004`](#insn-00bce004)
  - `FALL_THROUGH` [`00bce034`](#insn-00bce034) → [`00bce038`](#insn-00bce038)
- ブロック [`00bce038`](#insn-00bce038) 範囲 `[['00bce038', '00bce04f']]`
  - `UNCONDITIONAL_JUMP` [`00bce04c`](#insn-00bce04c) → [`00bce004`](#insn-00bce004)
- ブロック [`00bce050`](#insn-00bce050) 範囲 `[['00bce050', '00bce063']]`
  - `CONDITIONAL_JUMP` [`00bce060`](#insn-00bce060) → [`00bce08c`](#insn-00bce08c)
  - `FALL_THROUGH` [`00bce060`](#insn-00bce060) → [`00bce064`](#insn-00bce064)
- ブロック [`00bce064`](#insn-00bce064) 範囲 `[['00bce064', '00bce083']]`
  - `CONDITIONAL_JUMP` [`00bce080`](#insn-00bce080) → [`00bce10c`](#insn-00bce10c)
  - `FALL_THROUGH` [`00bce080`](#insn-00bce080) → [`00bce084`](#insn-00bce084)
- ブロック [`00bce084`](#insn-00bce084) 範囲 `[['00bce084', '00bce08b']]`
  - `FALL_THROUGH` [`00bce088`](#insn-00bce088) → [`00bce08c`](#insn-00bce08c)
- ブロック [`00bce08c`](#insn-00bce08c) 範囲 `[['00bce08c', '00bce0b7']]`
  - `CONDITIONAL_JUMP` [`00bce0b4`](#insn-00bce0b4) → [`00bce0e0`](#insn-00bce0e0)
  - `FALL_THROUGH` [`00bce0b4`](#insn-00bce0b4) → [`00bce0b8`](#insn-00bce0b8)
- ブロック [`00bce0b8`](#insn-00bce0b8) 範囲 `[['00bce0b8', '00bce0d7']]`
  - `CONDITIONAL_JUMP` [`00bce0d4`](#insn-00bce0d4) → [`00bce110`](#insn-00bce110)
  - `FALL_THROUGH` [`00bce0d4`](#insn-00bce0d4) → [`00bce0d8`](#insn-00bce0d8)
- ブロック [`00bce0d8`](#insn-00bce0d8) 範囲 `[['00bce0d8', '00bce0df']]`
  - `FALL_THROUGH` [`00bce0dc`](#insn-00bce0dc) → [`00bce0e0`](#insn-00bce0e0)
- ブロック [`00bce0e0`](#insn-00bce0e0) 範囲 `[['00bce0e0', '00bce0ff']]`
- ブロック [`00bce100`](#insn-00bce100) 範囲 `[['00bce100', '00bce103']]`
- ブロック [`00bce104`](#insn-00bce104) 範囲 `[['00bce104', '00bce107']]`
- ブロック [`00bce108`](#insn-00bce108) 範囲 `[['00bce108', '00bce10b']]`
- ブロック [`00bce10c`](#insn-00bce10c) 範囲 `[['00bce10c', '00bce10f']]`
- ブロック [`00bce110`](#insn-00bce110) 範囲 `[['00bce110', '00bce113']]`
- ブロック [`00bce114`](#insn-00bce114) 範囲 `[['00bce114', '00bce117']]`
- ブロック [`00bce118`](#insn-00bce118) 範囲 `[['00bce118', '00bce11b']]`
- ブロック [`00bce11c`](#insn-00bce11c) 範囲 `[['00bce11c', '00bce11f']]`

## 命令位置別の参照

- [`00bcddd4`](#insn-00bcddd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd8`](#insn-00bcddd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdddc`](#insn-00bcdddc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddfc`](#insn-00bcddfc) → [`00bcde2c`](#insn-00bcde2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde18`](#insn-00bcde18) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcde20`](#insn-00bcde20) → [`00bce100`](#insn-00bce100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde50`](#insn-00bcde50) → [`00bcdf54`](#insn-00bcdf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde64`](#insn-00bcde64) → [`00bcde90`](#insn-00bcde90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde7c`](#insn-00bcde7c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcde84`](#insn-00bcde84) → [`00bce114`](#insn-00bce114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdeb8`](#insn-00bcdeb8) → [`00bcdee4`](#insn-00bcdee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcded0`](#insn-00bcded0) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcded8`](#insn-00bcded8) → [`00bce118`](#insn-00bce118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdef8`](#insn-00bcdef8) → [`00bc81c8`](../00bc8/00bc81c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc81c8` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf18`](#insn-00bcdf18) → [`00bcdf44`](#insn-00bcdf44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf30`](#insn-00bcdf30) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf38`](#insn-00bcdf38) → [`00bce11c`](#insn-00bce11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf64`](#insn-00bcdf64) → [`00bcdf90`](#insn-00bcdf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf7c`](#insn-00bcdf7c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf84`](#insn-00bcdf84) → [`00bce104`](#insn-00bce104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfb8`](#insn-00bcdfb8) → [`00bcdfe4`](#insn-00bcdfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd0`](#insn-00bcdfd0) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd8`](#insn-00bcdfd8) → [`00bce108`](#insn-00bce108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdff4`](#insn-00bcdff4) → [`00bce050`](#insn-00bce050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce000`](#insn-00bce000) → [`00bce010`](#insn-00bce010) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce00c`](#insn-00bce00c) → [`00bce050`](#insn-00bce050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce034`](#insn-00bce034) → [`00bce004`](#insn-00bce004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce04c`](#insn-00bce04c) → [`00bce004`](#insn-00bce004) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce060`](#insn-00bce060) → [`00bce08c`](#insn-00bce08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce078`](#insn-00bce078) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bce080`](#insn-00bce080) → [`00bce10c`](#insn-00bce10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0b4`](#insn-00bce0b4) → [`00bce0e0`](#insn-00bce0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0cc`](#insn-00bce0cc) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bce0d4`](#insn-00bce0d4) → [`00bce110`](#insn-00bce110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0ec`](#insn-00bce0ec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0f0`](#insn-00bce0f0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0f4`](#insn-00bce0f4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce100`](#insn-00bce100) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce104`](#insn-00bce104) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce108`](#insn-00bce108) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce10c`](#insn-00bce10c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce110`](#insn-00bce110) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce114`](#insn-00bce114) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce118`](#insn-00bce118) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce11c`](#insn-00bce11c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcddd4`](#insn-00bcddd4)

~~~json
{
  "source": "00bcddd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddd8`](#insn-00bcddd8)

~~~json
{
  "source": "00bcddd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdddc`](#insn-00bcdddc)

~~~json
{
  "source": "00bcdddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddfc`](#insn-00bcddfc)

~~~json
{
  "source": "00bcddfc",
  "target": "00bcde2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde18`](#insn-00bcde18)

~~~json
{
  "source": "00bcde18",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde20`](#insn-00bcde20)

~~~json
{
  "source": "00bcde20",
  "target": "00bce100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde50`](#insn-00bcde50)

~~~json
{
  "source": "00bcde50",
  "target": "00bcdf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde64`](#insn-00bcde64)

~~~json
{
  "source": "00bcde64",
  "target": "00bcde90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde7c`](#insn-00bcde7c)

~~~json
{
  "source": "00bcde7c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde84`](#insn-00bcde84)

~~~json
{
  "source": "00bcde84",
  "target": "00bce114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdeb8`](#insn-00bcdeb8)

~~~json
{
  "source": "00bcdeb8",
  "target": "00bcdee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcded0`](#insn-00bcded0)

~~~json
{
  "source": "00bcded0",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcded8`](#insn-00bcded8)

~~~json
{
  "source": "00bcded8",
  "target": "00bce118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdef8`](#insn-00bcdef8)

~~~json
{
  "source": "00bcdef8",
  "target": "00bc81c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf18`](#insn-00bcdf18)

~~~json
{
  "source": "00bcdf18",
  "target": "00bcdf44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf30`](#insn-00bcdf30)

~~~json
{
  "source": "00bcdf30",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf38`](#insn-00bcdf38)

~~~json
{
  "source": "00bcdf38",
  "target": "00bce11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf64`](#insn-00bcdf64)

~~~json
{
  "source": "00bcdf64",
  "target": "00bcdf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf7c`](#insn-00bcdf7c)

~~~json
{
  "source": "00bcdf7c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf84`](#insn-00bcdf84)

~~~json
{
  "source": "00bcdf84",
  "target": "00bce104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfb8`](#insn-00bcdfb8)

~~~json
{
  "source": "00bcdfb8",
  "target": "00bcdfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfd0`](#insn-00bcdfd0)

~~~json
{
  "source": "00bcdfd0",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdfd8`](#insn-00bcdfd8)

~~~json
{
  "source": "00bcdfd8",
  "target": "00bce108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdff4`](#insn-00bcdff4)

~~~json
{
  "source": "00bcdff4",
  "target": "00bce050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce000`](#insn-00bce000)

~~~json
{
  "source": "00bce000",
  "target": "00bce010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce00c`](#insn-00bce00c)

~~~json
{
  "source": "00bce00c",
  "target": "00bce050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce034`](#insn-00bce034)

~~~json
{
  "source": "00bce034",
  "target": "00bce004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce04c`](#insn-00bce04c)

~~~json
{
  "source": "00bce04c",
  "target": "00bce004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce060`](#insn-00bce060)

~~~json
{
  "source": "00bce060",
  "target": "00bce08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce078`](#insn-00bce078)

~~~json
{
  "source": "00bce078",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce080`](#insn-00bce080)

~~~json
{
  "source": "00bce080",
  "target": "00bce10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0b4`](#insn-00bce0b4)

~~~json
{
  "source": "00bce0b4",
  "target": "00bce0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0cc`](#insn-00bce0cc)

~~~json
{
  "source": "00bce0cc",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce0d4`](#insn-00bce0d4)

~~~json
{
  "source": "00bce0d4",
  "target": "00bce110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0ec`](#insn-00bce0ec)

~~~json
{
  "source": "00bce0ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0f0`](#insn-00bce0f0)

~~~json
{
  "source": "00bce0f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0f4`](#insn-00bce0f4)

~~~json
{
  "source": "00bce0f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce100`](#insn-00bce100)

~~~json
{
  "source": "00bce100",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce104`](#insn-00bce104)

~~~json
{
  "source": "00bce104",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce108`](#insn-00bce108)

~~~json
{
  "source": "00bce108",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce10c`](#insn-00bce10c)

~~~json
{
  "source": "00bce10c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce110`](#insn-00bce110)

~~~json
{
  "source": "00bce110",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce114`](#insn-00bce114)

~~~json
{
  "source": "00bce114",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce118`](#insn-00bce118)

~~~json
{
  "source": "00bce118",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce11c`](#insn-00bce11c)

~~~json
{
  "source": "00bce11c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
