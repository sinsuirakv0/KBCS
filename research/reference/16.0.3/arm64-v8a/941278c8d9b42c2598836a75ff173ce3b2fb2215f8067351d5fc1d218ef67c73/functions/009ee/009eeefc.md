# 009eeefc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `009edf50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0026.md#compare-c0b707acc49a5a30349ad7245475d8b0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009eeefc",
  "name": "FUN_009eeefc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51229530b9b277e18c6982bfa682b750421647200b8782d8e187049447722ea4",
  "source_text_sha256": "51229530b9b277e18c6982bfa682b750421647200b8782d8e187049447722ea4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009eeefc",
        "009ef107"
      ],
      [
        "009ef134",
        "009ef137"
      ]
    ],
    "bytes_sha256": "577cbae70715bc8279977a5524a4b6c4f2e965be0f401686a6ea4d9634aecc92",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009ef138](../009ef/009ef138.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [004413ec](../00441/004413ec.md)
- [009eeb3c](../009ee/009eeb3c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59100](../00c59/00c59100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3677 bytes

~~~c

void FUN_009eeefc(long *param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  bool bVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  long *plVar9;
  long lVar10;
  long *plVar11;
  long *plVar12;
  byte local_80 [16];
  void *local_70;
  long local_68;
  
                    /* try { // try from 009eeefc to 00aeef0b has its CatchHandler @ 009f0734 */
                    /* try { // try from 009eef0c to 00aeef17 has its CatchHandler @ 009f0714 */
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  local_80[0] = 0x10;
  local_80[9] = 0;
  local_80[1] = 0x42;
  local_80[2] = 0x6f;
  local_80[3] = 0x6e;
  local_80[4] = 0x75;
  local_80[5] = 0x73;
  local_80[6] = 0x4e;
  local_80[7] = 0x75;
  local_80[8] = 0x6d;
                    /* try { // try from 009eef58 to 00aeef5f has its CatchHandler @ 009f03dc */
  lVar4 = FUN_004413ec(param_2 + 0x10,local_80);
                    /* try { // try from 009eef60 to 00aeef6f has its CatchHandler @ 009f06d4 */
  if (param_2 + 0x18 == lVar4) {
    lVar4 = 0;
  }
  else {
    lVar4 = *(long *)(lVar4 + 0x38);
                    /* try { // try from 009eef70 to 00aeef7b has its CatchHandler @ 009f06b4 */
    if (*(int *)(lVar4 + 8) != 7) {
      lVar4 = 0;
    }
  }
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* try { // try from 009eef98 to 00aef103 has its CatchHandler @ 009ee1b8 */
  plVar11 = *(long **)(lVar4 + 0x10);
  if (plVar11 != (long *)(lVar4 + 0x18)) {
    do {
      iVar3 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (plVar11 + 4,0,10);
      lVar10 = plVar11[7];
      uVar5 = 0;
      if ((lVar10 == 0) || (*(int *)(lVar10 + 8) != 7)) goto LAB_009ef0d4;
      plVar9 = (long *)param_1[1];
      plVar8 = param_1 + 1;
      while (plVar12 = plVar8, plVar9 != (long *)0x0) {
        while (plVar6 = plVar9, plVar8 = plVar6, (int)plVar6[4] <= iVar3) {
          if (iVar3 <= (int)plVar6[4]) goto LAB_009ef084;
          plVar9 = (long *)plVar6[1];
          if ((long *)plVar6[1] == (long *)0x0) {
            plVar12 = plVar6 + 1;
            goto LAB_009ef02c;
          }
        }
        plVar9 = (long *)*plVar6;
      }
LAB_009ef02c:
      plVar6 = (long *)_Znwm(0x48);
      *plVar6 = 0;
      plVar6[1] = 0;
      plVar6[7] = 0;
      plVar6[8] = 0;
      plVar6[6] = 0;
      plVar6[2] = (long)plVar8;
      *plVar12 = (long)plVar6;
      plVar9 = (long *)*param_1;
      *(int *)(plVar6 + 4) = iVar3;
      *(undefined4 *)(plVar6 + 5) = 0;
      plVar8 = plVar6;
      if (*plVar9 != 0) {
        *param_1 = *plVar9;
        plVar8 = (long *)*plVar12;
      }
      FUN_0043bf04(param_1[1],plVar8);
      param_1[2] = param_1[2] + 1;
LAB_009ef084:
      uVar7 = FUN_009eeb3c(plVar6 + 5,lVar10,param_3);
      if ((uVar7 & 1) == 0) {
        uVar5 = 0;
        goto LAB_009ef0d4;
      }
      plVar8 = (long *)plVar11[1];
      plVar9 = plVar11;
      if ((long *)plVar11[1] == (long *)0x0) {
        do {
          plVar11 = (long *)plVar9[2];
          bVar2 = (long *)*plVar11 != plVar9;
          plVar9 = plVar11;
        } while (bVar2);
      }
      else {
        do {
          plVar11 = plVar8;
          plVar8 = (long *)*plVar11;
        } while ((long *)*plVar11 != (long *)0x0);
      }
    } while (plVar11 != (long *)(lVar4 + 0x18));
  }
  uVar5 = 1;
LAB_009ef0d4:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* try { // try from 009ef104 to 00aef10b has its CatchHandler @ 009f03d4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009eeefc"></a> `009eeefc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009eef00"></a> `009eef00` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009eef04"></a> `009eef04` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009eef08"></a> `009eef08` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009eef0c"></a> `009eef0c` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009eef10"></a> `009eef10` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009eef14"></a> `009eef14` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009eef18"></a> `009eef18` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009eef1c"></a> `009eef1c` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009eef20"></a> `009eef20` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-009eef24"></a> `009eef24` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-009eef28"></a> `009eef28` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009eef2c"></a> `009eef2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-009eef30"></a> `009eef30` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-009eef34"></a> `009eef34` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009eef38"></a> `009eef38` | `48 e8 8d d2` | mov x8,#0x6f42 | `FALL_THROUGH`
<a id="insn-009eef3c"></a> `009eef3c` | `c8 ad ae f2` | movk x8,#0x756e, LSL #16 | `FALL_THROUGH`
<a id="insn-009eef40"></a> `009eef40` | `e9 43 00 39` | strb w9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009eef44"></a> `009eef44` | `68 ce c9 f2` | movk x8,#0x4e73, LSL #32 | `FALL_THROUGH`
<a id="insn-009eef48"></a> `009eef48` | `ff 67 00 39` | strb wzr,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-009eef4c"></a> `009eef4c` | `a8 ae ed f2` | movk x8,#0x6d75, LSL #48 | `FALL_THROUGH`
<a id="insn-009eef50"></a> `009eef50` | `e8 13 01 f8` | stur x8,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-009eef54"></a> `009eef54` | `20 40 00 91` | add x0,x1,#0x10 | `FALL_THROUGH`
<a id="insn-009eef58"></a> `009eef58` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-009eef5c"></a> `009eef5c` | `24 49 e9 97` | bl 0x004413ec | `UNCONDITIONAL_CALL`
<a id="insn-009eef60"></a> `009eef60` | `a8 62 00 91` | add x8,x21,#0x18 | `FALL_THROUGH`
<a id="insn-009eef64"></a> `009eef64` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-009eef68"></a> `009eef68` | `c0 00 00 54` | b.eq 0x009eef80 | `CONDITIONAL_JUMP`
<a id="insn-009eef6c"></a> `009eef6c` | `08 1c 40 f9` | ldr x8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-009eef70"></a> `009eef70` | `09 09 40 b9` | ldr w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009eef74"></a> `009eef74` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-009eef78"></a> `009eef78` | `15 01 9f 9a` | csel x21,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-009eef7c"></a> `009eef7c` | `02 00 00 14` | b 0x009eef84 | `UNCONDITIONAL_JUMP`
<a id="insn-009eef80"></a> `009eef80` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-009eef84"></a> `009eef84` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009eef88"></a> `009eef88` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009eef8c"></a> `009eef8c` | `68 00 00 36` | tbz w8,#0x0,0x009eef98 | `CONDITIONAL_JUMP`
<a id="insn-009eef90"></a> `009eef90` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009eef94"></a> `009eef94` | `ef a7 09 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-009eef98"></a> `009eef98` | `bb 0a 40 f9` | ldr x27,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-009eef9c"></a> `009eef9c` | `b9 62 00 91` | add x25,x21,#0x18 | `FALL_THROUGH`
<a id="insn-009eefa0"></a> `009eefa0` | `7f 03 19 eb` | cmp x27,x25 | `FALL_THROUGH`
<a id="insn-009eefa4"></a> `009eefa4` | `20 09 00 54` | b.eq 0x009ef0c8 | `CONDITIONAL_JUMP`
<a id="insn-009eefa8"></a> `009eefa8` | `9a 22 00 91` | add x26,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009eefac"></a> `009eefac` | `04 00 00 14` | b 0x009eefbc | `UNCONDITIONAL_JUMP`
<a id="insn-009eefb0"></a> `009eefb0` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-009eefb4"></a> `009eefb4` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-009eefb8"></a> `009eefb8` | `80 08 00 54` | b.eq 0x009ef0c8 | `CONDITIONAL_JUMP`
<a id="insn-009eefbc"></a> `009eefbc` | `60 83 00 91` | add x0,x27,#0x20 | `FALL_THROUGH`
<a id="insn-009eefc0"></a> `009eefc0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-009eefc4"></a> `009eefc4` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-009eefc8"></a> `009eefc8` | `4e a8 09 94` | bl 0x00c59100 | `UNCONDITIONAL_CALL`
<a id="insn-009eefcc"></a> `009eefcc` | `75 1f 40 f9` | ldr x21,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-009eefd0"></a> `009eefd0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009eefd4"></a> `009eefd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009eefd8"></a> `009eefd8` | `f5 07 00 b4` | cbz x21,0x009ef0d4 | `CONDITIONAL_JUMP`
<a id="insn-009eefdc"></a> `009eefdc` | `a8 0a 40 b9` | ldr w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009eefe0"></a> `009eefe0` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-009eefe4"></a> `009eefe4` | `81 07 00 54` | b.ne 0x009ef0d4 | `CONDITIONAL_JUMP`
<a id="insn-009eefe8"></a> `009eefe8` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-009eefec"></a> `009eefec` | `fc 03 1a aa` | mov x28,x26 | `FALL_THROUGH`
<a id="insn-009eeff0"></a> `009eeff0` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-009eeff4"></a> `009eeff4` | `a8 00 00 b5` | cbnz x8,0x009ef008 | `CONDITIONAL_JUMP`
<a id="insn-009eeff8"></a> `009eeff8` | `0d 00 00 14` | b 0x009ef02c | `UNCONDITIONAL_JUMP`
<a id="insn-009eeffc"></a> `009eeffc` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-009ef000"></a> `009ef000` | `fc 03 16 aa` | mov x28,x22 | `FALL_THROUGH`
<a id="insn-009ef004"></a> `009ef004` | `48 01 00 b4` | cbz x8,0x009ef02c | `CONDITIONAL_JUMP`
<a id="insn-009ef008"></a> `009ef008` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-009ef00c"></a> `009ef00c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-009ef010"></a> `009ef010` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-009ef014"></a> `009ef014` | `4b ff ff 54` | b.lt 0x009eeffc | `CONDITIONAL_JUMP`
<a id="insn-009ef018"></a> `009ef018` | `1f 01 17 6b` | cmp w8,w23 | `FALL_THROUGH`
<a id="insn-009ef01c"></a> `009ef01c` | `4a 03 00 54` | b.ge 0x009ef084 | `CONDITIONAL_JUMP`
<a id="insn-009ef020"></a> `009ef020` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-009ef024"></a> `009ef024` | `28 ff ff b5` | cbnz x8,0x009ef008 | `CONDITIONAL_JUMP`
<a id="insn-009ef028"></a> `009ef028` | `dc 22 00 91` | add x28,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009ef02c"></a> `009ef02c` | `00 09 80 52` | mov w0,#0x48 | `FALL_THROUGH`
<a id="insn-009ef030"></a> `009ef030` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-009ef034"></a> `009ef034` | `bf a7 09 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-009ef038"></a> `009ef038` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-009ef03c"></a> `009ef03c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-009ef040"></a> `009ef040` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-009ef044"></a> `009ef044` | `1f fc 03 a9` | stp xzr,xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-009ef048"></a> `009ef048` | `1f 18 00 f9` | str xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-009ef04c"></a> `009ef04c` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-009ef050"></a> `009ef050` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-009ef054"></a> `009ef054` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009ef058"></a> `009ef058` | `17 20 00 b9` | str w23,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-009ef05c"></a> `009ef05c` | `1f 28 00 b9` | str wzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-009ef060"></a> `009ef060` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-009ef064"></a> `009ef064` | `68 00 00 b4` | cbz x8,0x009ef070 | `CONDITIONAL_JUMP`
<a id="insn-009ef068"></a> `009ef068` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-009ef06c"></a> `009ef06c` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-009ef070"></a> `009ef070` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-009ef074"></a> `009ef074` | `a4 33 e9 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-009ef078"></a> `009ef078` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-009ef07c"></a> `009ef07c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-009ef080"></a> `009ef080` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-009ef084"></a> `009ef084` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-009ef088"></a> `009ef088` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009ef08c"></a> `009ef08c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009ef090"></a> `009ef090` | `ab fe ff 97` | bl 0x009eeb3c | `UNCONDITIONAL_CALL`
<a id="insn-009ef094"></a> `009ef094` | `e0 01 00 36` | tbz w0,#0x0,0x009ef0d0 | `CONDITIONAL_JUMP`
<a id="insn-009ef098"></a> `009ef098` | `69 07 40 f9` | ldr x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-009ef09c"></a> `009ef09c` | `a9 00 00 b4` | cbz x9,0x009ef0b0 | `CONDITIONAL_JUMP`
<a id="insn-009ef0a0"></a> `009ef0a0` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-009ef0a4"></a> `009ef0a4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-009ef0a8"></a> `009ef0a8` | `c9 ff ff b5` | cbnz x9,0x009ef0a0 | `CONDITIONAL_JUMP`
<a id="insn-009ef0ac"></a> `009ef0ac` | `c1 ff ff 17` | b 0x009eefb0 | `UNCONDITIONAL_JUMP`
<a id="insn-009ef0b0"></a> `009ef0b0` | `68 0b 40 f9` | ldr x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-009ef0b4"></a> `009ef0b4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009ef0b8"></a> `009ef0b8` | `3f 01 1b eb` | cmp x9,x27 | `FALL_THROUGH`
<a id="insn-009ef0bc"></a> `009ef0bc` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-009ef0c0"></a> `009ef0c0` | `81 ff ff 54` | b.ne 0x009ef0b0 | `CONDITIONAL_JUMP`
<a id="insn-009ef0c4"></a> `009ef0c4` | `bb ff ff 17` | b 0x009eefb0 | `UNCONDITIONAL_JUMP`
<a id="insn-009ef0c8"></a> `009ef0c8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ef0cc"></a> `009ef0cc` | `02 00 00 14` | b 0x009ef0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ef0d0"></a> `009ef0d0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009ef0d4"></a> `009ef0d4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ef0d8"></a> `009ef0d8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ef0dc"></a> `009ef0dc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ef0e0"></a> `009ef0e0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ef0e4"></a> `009ef0e4` | `81 02 00 54` | b.ne 0x009ef134 | `CONDITIONAL_JUMP`
<a id="insn-009ef0e8"></a> `009ef0e8` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009ef0ec"></a> `009ef0ec` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009ef0f0"></a> `009ef0f0` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009ef0f4"></a> `009ef0f4` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009ef0f8"></a> `009ef0f8` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009ef0fc"></a> `009ef0fc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ef100"></a> `009ef100` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009ef104"></a> `009ef104` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ef134"></a> `009ef134` | `93 a7 09 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009eeefc`](#insn-009eeefc) 範囲 `[['009eeefc', '009eef0b']]`
  - `FALL_THROUGH` [`009eef08`](#insn-009eef08) → [`009eef0c`](#insn-009eef0c)
- ブロック [`009eef0c`](#insn-009eef0c) 範囲 `[['009eef0c', '009eef57']]`
  - `FALL_THROUGH` [`009eef54`](#insn-009eef54) → [`009eef58`](#insn-009eef58)
- ブロック [`009eef58`](#insn-009eef58) 範囲 `[['009eef58', '009eef5f']]`
  - `FALL_THROUGH` [`009eef5c`](#insn-009eef5c) → [`009eef60`](#insn-009eef60)
- ブロック [`009eef60`](#insn-009eef60) 範囲 `[['009eef60', '009eef6b']]`
  - `CONDITIONAL_JUMP` [`009eef68`](#insn-009eef68) → [`009eef80`](#insn-009eef80)
  - `FALL_THROUGH` [`009eef68`](#insn-009eef68) → [`009eef6c`](#insn-009eef6c)
- ブロック [`009eef6c`](#insn-009eef6c) 範囲 `[['009eef6c', '009eef6f']]`
  - `FALL_THROUGH` [`009eef6c`](#insn-009eef6c) → [`009eef70`](#insn-009eef70)
- ブロック [`009eef70`](#insn-009eef70) 範囲 `[['009eef70', '009eef7b']]`
  - `FALL_THROUGH` [`009eef78`](#insn-009eef78) → [`009eef7c`](#insn-009eef7c)
- ブロック [`009eef7c`](#insn-009eef7c) 範囲 `[['009eef7c', '009eef7f']]`
  - `UNCONDITIONAL_JUMP` [`009eef7c`](#insn-009eef7c) → [`009eef84`](#insn-009eef84)
- ブロック [`009eef80`](#insn-009eef80) 範囲 `[['009eef80', '009eef83']]`
  - `FALL_THROUGH` [`009eef80`](#insn-009eef80) → [`009eef84`](#insn-009eef84)
- ブロック [`009eef84`](#insn-009eef84) 範囲 `[['009eef84', '009eef8f']]`
  - `CONDITIONAL_JUMP` [`009eef8c`](#insn-009eef8c) → [`009eef98`](#insn-009eef98)
  - `FALL_THROUGH` [`009eef8c`](#insn-009eef8c) → [`009eef90`](#insn-009eef90)
- ブロック [`009eef90`](#insn-009eef90) 範囲 `[['009eef90', '009eef97']]`
  - `FALL_THROUGH` [`009eef94`](#insn-009eef94) → [`009eef98`](#insn-009eef98)
- ブロック [`009eef98`](#insn-009eef98) 範囲 `[['009eef98', '009eefa7']]`
  - `CONDITIONAL_JUMP` [`009eefa4`](#insn-009eefa4) → [`009ef0c8`](#insn-009ef0c8)
  - `FALL_THROUGH` [`009eefa4`](#insn-009eefa4) → [`009eefa8`](#insn-009eefa8)
- ブロック [`009eefa8`](#insn-009eefa8) 範囲 `[['009eefa8', '009eefaf']]`
  - `UNCONDITIONAL_JUMP` [`009eefac`](#insn-009eefac) → [`009eefbc`](#insn-009eefbc)
- ブロック [`009eefb0`](#insn-009eefb0) 範囲 `[['009eefb0', '009eefbb']]`
  - `CONDITIONAL_JUMP` [`009eefb8`](#insn-009eefb8) → [`009ef0c8`](#insn-009ef0c8)
  - `FALL_THROUGH` [`009eefb8`](#insn-009eefb8) → [`009eefbc`](#insn-009eefbc)
- ブロック [`009eefbc`](#insn-009eefbc) 範囲 `[['009eefbc', '009eefdb']]`
  - `CONDITIONAL_JUMP` [`009eefd8`](#insn-009eefd8) → [`009ef0d4`](#insn-009ef0d4)
  - `FALL_THROUGH` [`009eefd8`](#insn-009eefd8) → [`009eefdc`](#insn-009eefdc)
- ブロック [`009eefdc`](#insn-009eefdc) 範囲 `[['009eefdc', '009eefe7']]`
  - `CONDITIONAL_JUMP` [`009eefe4`](#insn-009eefe4) → [`009ef0d4`](#insn-009ef0d4)
  - `FALL_THROUGH` [`009eefe4`](#insn-009eefe4) → [`009eefe8`](#insn-009eefe8)
- ブロック [`009eefe8`](#insn-009eefe8) 範囲 `[['009eefe8', '009eeff7']]`
  - `CONDITIONAL_JUMP` [`009eeff4`](#insn-009eeff4) → [`009ef008`](#insn-009ef008)
  - `FALL_THROUGH` [`009eeff4`](#insn-009eeff4) → [`009eeff8`](#insn-009eeff8)
- ブロック [`009eeff8`](#insn-009eeff8) 範囲 `[['009eeff8', '009eeffb']]`
  - `UNCONDITIONAL_JUMP` [`009eeff8`](#insn-009eeff8) → [`009ef02c`](#insn-009ef02c)
- ブロック [`009eeffc`](#insn-009eeffc) 範囲 `[['009eeffc', '009ef007']]`
  - `CONDITIONAL_JUMP` [`009ef004`](#insn-009ef004) → [`009ef02c`](#insn-009ef02c)
  - `FALL_THROUGH` [`009ef004`](#insn-009ef004) → [`009ef008`](#insn-009ef008)
- ブロック [`009ef008`](#insn-009ef008) 範囲 `[['009ef008', '009ef017']]`
  - `CONDITIONAL_JUMP` [`009ef014`](#insn-009ef014) → [`009eeffc`](#insn-009eeffc)
  - `FALL_THROUGH` [`009ef014`](#insn-009ef014) → [`009ef018`](#insn-009ef018)
- ブロック [`009ef018`](#insn-009ef018) 範囲 `[['009ef018', '009ef01f']]`
  - `CONDITIONAL_JUMP` [`009ef01c`](#insn-009ef01c) → [`009ef084`](#insn-009ef084)
  - `FALL_THROUGH` [`009ef01c`](#insn-009ef01c) → [`009ef020`](#insn-009ef020)
- ブロック [`009ef020`](#insn-009ef020) 範囲 `[['009ef020', '009ef027']]`
  - `CONDITIONAL_JUMP` [`009ef024`](#insn-009ef024) → [`009ef008`](#insn-009ef008)
  - `FALL_THROUGH` [`009ef024`](#insn-009ef024) → [`009ef028`](#insn-009ef028)
- ブロック [`009ef028`](#insn-009ef028) 範囲 `[['009ef028', '009ef02b']]`
  - `FALL_THROUGH` [`009ef028`](#insn-009ef028) → [`009ef02c`](#insn-009ef02c)
- ブロック [`009ef02c`](#insn-009ef02c) 範囲 `[['009ef02c', '009ef067']]`
  - `CONDITIONAL_JUMP` [`009ef064`](#insn-009ef064) → [`009ef070`](#insn-009ef070)
  - `FALL_THROUGH` [`009ef064`](#insn-009ef064) → [`009ef068`](#insn-009ef068)
- ブロック [`009ef068`](#insn-009ef068) 範囲 `[['009ef068', '009ef06f']]`
  - `FALL_THROUGH` [`009ef06c`](#insn-009ef06c) → [`009ef070`](#insn-009ef070)
- ブロック [`009ef070`](#insn-009ef070) 範囲 `[['009ef070', '009ef083']]`
  - `FALL_THROUGH` [`009ef080`](#insn-009ef080) → [`009ef084`](#insn-009ef084)
- ブロック [`009ef084`](#insn-009ef084) 範囲 `[['009ef084', '009ef097']]`
  - `CONDITIONAL_JUMP` [`009ef094`](#insn-009ef094) → [`009ef0d0`](#insn-009ef0d0)
  - `FALL_THROUGH` [`009ef094`](#insn-009ef094) → [`009ef098`](#insn-009ef098)
- ブロック [`009ef098`](#insn-009ef098) 範囲 `[['009ef098', '009ef09f']]`
  - `CONDITIONAL_JUMP` [`009ef09c`](#insn-009ef09c) → [`009ef0b0`](#insn-009ef0b0)
  - `FALL_THROUGH` [`009ef09c`](#insn-009ef09c) → [`009ef0a0`](#insn-009ef0a0)
- ブロック [`009ef0a0`](#insn-009ef0a0) 範囲 `[['009ef0a0', '009ef0ab']]`
  - `CONDITIONAL_JUMP` [`009ef0a8`](#insn-009ef0a8) → [`009ef0a0`](#insn-009ef0a0)
  - `FALL_THROUGH` [`009ef0a8`](#insn-009ef0a8) → [`009ef0ac`](#insn-009ef0ac)
- ブロック [`009ef0ac`](#insn-009ef0ac) 範囲 `[['009ef0ac', '009ef0af']]`
  - `UNCONDITIONAL_JUMP` [`009ef0ac`](#insn-009ef0ac) → [`009eefb0`](#insn-009eefb0)
- ブロック [`009ef0b0`](#insn-009ef0b0) 範囲 `[['009ef0b0', '009ef0c3']]`
  - `CONDITIONAL_JUMP` [`009ef0c0`](#insn-009ef0c0) → [`009ef0b0`](#insn-009ef0b0)
  - `FALL_THROUGH` [`009ef0c0`](#insn-009ef0c0) → [`009ef0c4`](#insn-009ef0c4)
- ブロック [`009ef0c4`](#insn-009ef0c4) 範囲 `[['009ef0c4', '009ef0c7']]`
  - `UNCONDITIONAL_JUMP` [`009ef0c4`](#insn-009ef0c4) → [`009eefb0`](#insn-009eefb0)
- ブロック [`009ef0c8`](#insn-009ef0c8) 範囲 `[['009ef0c8', '009ef0cf']]`
  - `UNCONDITIONAL_JUMP` [`009ef0cc`](#insn-009ef0cc) → [`009ef0d4`](#insn-009ef0d4)
- ブロック [`009ef0d0`](#insn-009ef0d0) 範囲 `[['009ef0d0', '009ef0d3']]`
  - `FALL_THROUGH` [`009ef0d0`](#insn-009ef0d0) → [`009ef0d4`](#insn-009ef0d4)
- ブロック [`009ef0d4`](#insn-009ef0d4) 範囲 `[['009ef0d4', '009ef0e7']]`
  - `CONDITIONAL_JUMP` [`009ef0e4`](#insn-009ef0e4) → [`009ef134`](#insn-009ef134)
  - `FALL_THROUGH` [`009ef0e4`](#insn-009ef0e4) → [`009ef0e8`](#insn-009ef0e8)
- ブロック [`009ef0e8`](#insn-009ef0e8) 範囲 `[['009ef0e8', '009ef103']]`
  - `FALL_THROUGH` [`009ef100`](#insn-009ef100) → [`009ef104`](#insn-009ef104)
- ブロック [`009ef104`](#insn-009ef104) 範囲 `[['009ef104', '009ef107']]`
- ブロック [`009ef134`](#insn-009ef134) 範囲 `[['009ef134', '009ef137']]`

## 命令位置別の参照

- [`009eef00`](#insn-009eef00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef04`](#insn-009eef04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef08`](#insn-009eef08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef0c`](#insn-009eef0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef10`](#insn-009eef10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef14`](#insn-009eef14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef34`](#insn-009eef34) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef40`](#insn-009eef40) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef48`](#insn-009eef48) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef50`](#insn-009eef50) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef5c`](#insn-009eef5c) → [`004413ec`](../00441/004413ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004413ec` · 推定シンボル `None` · 推定型 `None`
- [`009eef68`](#insn-009eef68) → [`009eef80`](#insn-009eef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef7c`](#insn-009eef7c) → [`009eef84`](#insn-009eef84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef84`](#insn-009eef84) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef88`](#insn-009eef88) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef8c`](#insn-009eef8c) → [`009eef98`](#insn-009eef98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef90`](#insn-009eef90) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eef94`](#insn-009eef94) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`009eefa4`](#insn-009eefa4) → [`009ef0c8`](#insn-009ef0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eefac`](#insn-009eefac) → [`009eefbc`](#insn-009eefbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eefb8`](#insn-009eefb8) → [`009ef0c8`](#insn-009ef0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eefc8`](#insn-009eefc8) → [`00c59100`](../00c59/00c59100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59100` · 推定シンボル `None` · 推定型 `None`
- [`009eefd8`](#insn-009eefd8) → [`009ef0d4`](#insn-009ef0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eefe4`](#insn-009eefe4) → [`009ef0d4`](#insn-009ef0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eeff4`](#insn-009eeff4) → [`009ef008`](#insn-009ef008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009eeff8`](#insn-009eeff8) → [`009ef02c`](#insn-009ef02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef004`](#insn-009ef004) → [`009ef02c`](#insn-009ef02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef014`](#insn-009ef014) → [`009eeffc`](#insn-009eeffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef01c`](#insn-009ef01c) → [`009ef084`](#insn-009ef084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef024`](#insn-009ef024) → [`009ef008`](#insn-009ef008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef034`](#insn-009ef034) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`009ef064`](#insn-009ef064) → [`009ef070`](#insn-009ef070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef074`](#insn-009ef074) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`009ef090`](#insn-009ef090) → [`009eeb3c`](009eeb3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009eeb3c` · 推定シンボル `None` · 推定型 `None`
- [`009ef094`](#insn-009ef094) → [`009ef0d0`](#insn-009ef0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef09c`](#insn-009ef09c) → [`009ef0b0`](#insn-009ef0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0a8`](#insn-009ef0a8) → [`009ef0a0`](#insn-009ef0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0ac`](#insn-009ef0ac) → [`009eefb0`](#insn-009eefb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0c0`](#insn-009ef0c0) → [`009ef0b0`](#insn-009ef0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0c4`](#insn-009ef0c4) → [`009eefb0`](#insn-009eefb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0cc`](#insn-009ef0cc) → [`009ef0d4`](#insn-009ef0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0d4`](#insn-009ef0d4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0dc`](#insn-009ef0dc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0e4`](#insn-009ef0e4) → [`009ef134`](#insn-009ef134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0e8`](#insn-009ef0e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0ec`](#insn-009ef0ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0f0`](#insn-009ef0f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0f4`](#insn-009ef0f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0f8`](#insn-009ef0f8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef0fc`](#insn-009ef0fc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ef134`](#insn-009ef134) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009eef00`](#insn-009eef00)

~~~json
{
  "source": "009eef00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef04`](#insn-009eef04)

~~~json
{
  "source": "009eef04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef08`](#insn-009eef08)

~~~json
{
  "source": "009eef08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef0c`](#insn-009eef0c)

~~~json
{
  "source": "009eef0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef10`](#insn-009eef10)

~~~json
{
  "source": "009eef10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef14`](#insn-009eef14)

~~~json
{
  "source": "009eef14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef34`](#insn-009eef34)

~~~json
{
  "source": "009eef34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef40`](#insn-009eef40)

~~~json
{
  "source": "009eef40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef48`](#insn-009eef48)

~~~json
{
  "source": "009eef48",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef50`](#insn-009eef50)

~~~json
{
  "source": "009eef50",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef5c`](#insn-009eef5c)

~~~json
{
  "source": "009eef5c",
  "target": "004413ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009eef68`](#insn-009eef68)

~~~json
{
  "source": "009eef68",
  "target": "009eef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef7c`](#insn-009eef7c)

~~~json
{
  "source": "009eef7c",
  "target": "009eef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef84`](#insn-009eef84)

~~~json
{
  "source": "009eef84",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef88`](#insn-009eef88)

~~~json
{
  "source": "009eef88",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef8c`](#insn-009eef8c)

~~~json
{
  "source": "009eef8c",
  "target": "009eef98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef90`](#insn-009eef90)

~~~json
{
  "source": "009eef90",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eef94`](#insn-009eef94)

~~~json
{
  "source": "009eef94",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009eefa4`](#insn-009eefa4)

~~~json
{
  "source": "009eefa4",
  "target": "009ef0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eefac`](#insn-009eefac)

~~~json
{
  "source": "009eefac",
  "target": "009eefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eefb8`](#insn-009eefb8)

~~~json
{
  "source": "009eefb8",
  "target": "009ef0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eefc8`](#insn-009eefc8)

~~~json
{
  "source": "009eefc8",
  "target": "00c59100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009eefd8`](#insn-009eefd8)

~~~json
{
  "source": "009eefd8",
  "target": "009ef0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eefe4`](#insn-009eefe4)

~~~json
{
  "source": "009eefe4",
  "target": "009ef0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eeff4`](#insn-009eeff4)

~~~json
{
  "source": "009eeff4",
  "target": "009ef008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009eeff8`](#insn-009eeff8)

~~~json
{
  "source": "009eeff8",
  "target": "009ef02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef004`](#insn-009ef004)

~~~json
{
  "source": "009ef004",
  "target": "009ef02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef014`](#insn-009ef014)

~~~json
{
  "source": "009ef014",
  "target": "009eeffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef01c`](#insn-009ef01c)

~~~json
{
  "source": "009ef01c",
  "target": "009ef084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef024`](#insn-009ef024)

~~~json
{
  "source": "009ef024",
  "target": "009ef008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef034`](#insn-009ef034)

~~~json
{
  "source": "009ef034",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ef064`](#insn-009ef064)

~~~json
{
  "source": "009ef064",
  "target": "009ef070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef074`](#insn-009ef074)

~~~json
{
  "source": "009ef074",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ef090`](#insn-009ef090)

~~~json
{
  "source": "009ef090",
  "target": "009eeb3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ef094`](#insn-009ef094)

~~~json
{
  "source": "009ef094",
  "target": "009ef0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef09c`](#insn-009ef09c)

~~~json
{
  "source": "009ef09c",
  "target": "009ef0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0a8`](#insn-009ef0a8)

~~~json
{
  "source": "009ef0a8",
  "target": "009ef0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0ac`](#insn-009ef0ac)

~~~json
{
  "source": "009ef0ac",
  "target": "009eefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0c0`](#insn-009ef0c0)

~~~json
{
  "source": "009ef0c0",
  "target": "009ef0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0c4`](#insn-009ef0c4)

~~~json
{
  "source": "009ef0c4",
  "target": "009eefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0cc`](#insn-009ef0cc)

~~~json
{
  "source": "009ef0cc",
  "target": "009ef0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0d4`](#insn-009ef0d4)

~~~json
{
  "source": "009ef0d4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0dc`](#insn-009ef0dc)

~~~json
{
  "source": "009ef0dc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0e4`](#insn-009ef0e4)

~~~json
{
  "source": "009ef0e4",
  "target": "009ef134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0e8`](#insn-009ef0e8)

~~~json
{
  "source": "009ef0e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0ec`](#insn-009ef0ec)

~~~json
{
  "source": "009ef0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0f0`](#insn-009ef0f0)

~~~json
{
  "source": "009ef0f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0f4`](#insn-009ef0f4)

~~~json
{
  "source": "009ef0f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0f8`](#insn-009ef0f8)

~~~json
{
  "source": "009ef0f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef0fc`](#insn-009ef0fc)

~~~json
{
  "source": "009ef0fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ef134`](#insn-009ef134)

~~~json
{
  "source": "009ef134",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
