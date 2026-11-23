# 00ad4cec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad4db4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4db4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-11bf6b7db45870b385e186c149b44753)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad4cec",
  "name": "FUN_00ad4cec",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "acdd189ea8a4bb98ff703b45a57ad3fa025af359354c7f1ecc51eb9559c2f9cc",
  "source_text_sha256": "acdd189ea8a4bb98ff703b45a57ad3fa025af359354c7f1ecc51eb9559c2f9cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad4cec",
        "00ad4ebf"
      ],
      [
        "00ad4ee4",
        "00ad4ee7"
      ]
    ],
    "bytes_sha256": "2c2dee23d090850768fe1163ed7a5ac28fc986da0cf2882237424e0805f62f94",
    "instruction_count": 118,
    "instruction_bytes": 472,
    "body_bytes": 472,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad4424](../00ad4/00ad4424.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [0041e380](../0041e/0041e380.md)
- [0041e41c](../0041e/0041e41c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2682 bytes

~~~c

ulong * FUN_00ad4cec(long *param_1,char *param_2)

{
  ulong uVar1;
  long lVar2;
  size_t sVar3;
  void *__ptr;
  long lVar4;
  long lVar5;
  long lVar6;
  undefined1 *puVar7;
  ulong *puVar8;
  undefined1 *puVar9;
  void *__dest;
  
  lVar2 = tpidr_el0;
  lVar4 = *(long *)(lVar2 + 0x28);
  lVar5 = param_1[1] - *param_1 >> 3;
  puVar8 = (ulong *)(lVar5 * -0x5555555555555555);
  puVar9 = (undefined1 *)((long)puVar8 + 1);
  if (puVar9 < (undefined1 *)0xaaaaaaaaaaaaaab) {
    lVar6 = param_1[2] - *param_1 >> 3;
    puVar7 = (undefined1 *)(lVar6 * 0x5555555555555556);
    if (puVar7 < puVar9 || (long)puVar7 - (long)puVar9 == 0) {
      puVar7 = puVar9;
    }
    if (0x555555555555554 < (ulong)(lVar6 * -0x5555555555555555)) {
      puVar7 = (undefined1 *)0xaaaaaaaaaaaaaaa;
    }
    if (puVar7 == (undefined1 *)0x0) {
      lVar6 = 0;
    }
    else {
      if ((undefined1 *)0xaaaaaaaaaaaaaaa < puVar7) {
        if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
          FUN_0041e380();
        }
        goto LAB_00ad4ee4;
      }
      lVar6 = _Znwm((long)puVar7 * 0x18);
    }
    puVar8 = (ulong *)(lVar6 + lVar5 * 8);
    sVar3 = strlen(param_2);
    if (sVar3 < 0xfffffffffffffff8) {
      if (sVar3 < 0x17) {
        puVar9 = (undefined1 *)((long)puVar8 + 1);
        *(char *)puVar8 = (char)((int)sVar3 << 1);
        if (sVar3 != 0) goto LAB_00ad4e08;
      }
      else {
        uVar1 = (sVar3 & 0xfffffffffffffff8) + 8;
        if ((sVar3 | 7) != 0x17) {
          uVar1 = sVar3 | 7;
        }
        puVar9 = (undefined1 *)_Znwm(uVar1 + 1);
        puVar8[1] = sVar3;
        puVar8[2] = (ulong)puVar9;
        *puVar8 = uVar1 + 1 | 1;
LAB_00ad4e08:
        memmove(puVar9,param_2,sVar3);
      }
      puVar9[sVar3] = 0;
      sVar3 = param_1[1] - *param_1;
      __dest = (void *)((long)puVar8 - sVar3);
      memcpy(__dest,(void *)*param_1,sVar3);
      __ptr = (void *)*param_1;
      *param_1 = (long)__dest;
      param_1[1] = (long)(puVar8 + 3);
      param_1[2] = lVar6 + (long)puVar7 * 0x18;
      if (__ptr != (void *)0x0) {
        _ZdlPv(__ptr);
      }
      if (*(long *)(lVar2 + 0x28) == lVar4) {
        return puVar8 + 3;
      }
      goto LAB_00ad4ee4;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != lVar4) goto LAB_00ad4ee4;
    FUN_0041e41c(param_1);
  }
                    /* catch() { ... } // from try @ 00ad5078 with catch @ 00ad4e9c */
  if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(puVar8);
  }
LAB_00ad4ee4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad4cec"></a> `00ad4cec` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ad4cf0"></a> `00ad4cf0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad4cf4"></a> `00ad4cf4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad4cf8"></a> `00ad4cf8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad4cfc"></a> `00ad4cfc` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad4d00"></a> `00ad4d00` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad4d04"></a> `00ad4d04` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad4d08"></a> `00ad4d08` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ad4d0c"></a> `00ad4d0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad4d10"></a> `00ad4d10` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4d14"></a> `00ad4d14` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00ad4d18"></a> `00ad4d18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4d1c"></a> `00ad4d1c` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad4d20"></a> `00ad4d20` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00ad4d24"></a> `00ad4d24` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4d28"></a> `00ad4d28` | `15 7d 0b 9b` | mul x21,x8,x11 | `FALL_THROUGH`
<a id="insn-00ad4d2c"></a> `00ad4d2c` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ad4d30"></a> `00ad4d30` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00ad4d34"></a> `00ad4d34` | `a9 06 00 91` | add x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4d38"></a> `00ad4d38` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00ad4d3c"></a> `00ad4d3c` | `08 0a 00 54` | b.hi 0x00ad4e7c | `CONDITIONAL_JUMP`
<a id="insn-00ad4d40"></a> `00ad4d40` | `6c 42 00 91` | add x12,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00ad4d44"></a> `00ad4d44` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ad4d48"></a> `00ad4d48` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00ad4d4c"></a> `00ad4d4c` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad4d50"></a> `00ad4d50` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-00ad4d54"></a> `00ad4d54` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00ad4d58"></a> `00ad4d58` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4d5c"></a> `00ad4d5c` | `ad aa e0 f2` | movk x13,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00ad4d60"></a> `00ad4d60` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00ad4d64"></a> `00ad4d64` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4d68"></a> `00ad4d68` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00ad4d6c"></a> `00ad4d6c` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00ad4d70"></a> `00ad4d70` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00ad4d74"></a> `00ad4d74` | `36 31 88 9a` | csel x22,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00ad4d78"></a> `00ad4d78` | `f6 00 00 b4` | cbz x22,0x00ad4d94 | `CONDITIONAL_JUMP`
<a id="insn-00ad4d7c"></a> `00ad4d7c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00ad4d80"></a> `00ad4d80` | `68 09 00 54` | b.hi 0x00ad4eac | `CONDITIONAL_JUMP`
<a id="insn-00ad4d84"></a> `00ad4d84` | `c8 06 16 8b` | add x8,x22,x22, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ad4d88"></a> `00ad4d88` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4d8c"></a> `00ad4d8c` | `6d 18 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4d90"></a> `00ad4d90` | `02 00 00 14` | b 0x00ad4d98 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad4d94"></a> `00ad4d94` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00ad4d98"></a> `00ad4d98` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00ad4d9c"></a> `00ad4d9c` | `b5 02 08 9b` | madd x21,x21,x8,x0 | `FALL_THROUGH`
<a id="insn-00ad4da0"></a> `00ad4da0` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00ad4da4"></a> `00ad4da4` | `e0 57 00 a9` | stp x0,x21,[sp] | `FALL_THROUGH`
<a id="insn-00ad4da8"></a> `00ad4da8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad4dac"></a> `00ad4dac` | `f5 23 01 a9` | stp x21,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad4db0"></a> `00ad4db0` | `b8 18 04 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4db4"></a> `00ad4db4` | `1f 20 00 b1` | cmn x0,#0x8 | `FALL_THROUGH`
<a id="insn-00ad4db8"></a> `00ad4db8` | `e2 06 00 54` | b.cs 0x00ad4e94 | `CONDITIONAL_JUMP`
<a id="insn-00ad4dbc"></a> `00ad4dbc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ad4dc0"></a> `00ad4dc0` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-00ad4dc4"></a> `00ad4dc4` | `a2 00 00 54` | b.cs 0x00ad4dd8 | `CONDITIONAL_JUMP`
<a id="insn-00ad4dc8"></a> `00ad4dc8` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4dcc"></a> `00ad4dcc` | `a8 16 00 38` | strb w8,[x21], #0x1 | `FALL_THROUGH`
<a id="insn-00ad4dd0"></a> `00ad4dd0` | `d6 01 00 b5` | cbnz x22,0x00ad4e08 | `CONDITIONAL_JUMP`
<a id="insn-00ad4dd4"></a> `00ad4dd4` | `11 00 00 14` | b 0x00ad4e18 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad4dd8"></a> `00ad4dd8` | `c8 f2 7d 92` | and x8,x22,#-0x8 | `FALL_THROUGH`
<a id="insn-00ad4ddc"></a> `00ad4ddc` | `c9 0a 40 b2` | orr x9,x22,#0x7 | `FALL_THROUGH`
<a id="insn-00ad4de0"></a> `00ad4de0` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00ad4de4"></a> `00ad4de4` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-00ad4de8"></a> `00ad4de8` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00ad4dec"></a> `00ad4dec` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4df0"></a> `00ad4df0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad4df4"></a> `00ad4df4` | `53 18 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4df8"></a> `00ad4df8` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4dfc"></a> `00ad4dfc` | `b6 82 00 a9` | stp x22,x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ad4e00"></a> `00ad4e00` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00ad4e04"></a> `00ad4e04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ad4e08"></a> `00ad4e08` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4e0c"></a> `00ad4e0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad4e10"></a> `00ad4e10` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ad4e14"></a> `00ad4e14` | `77 18 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4e18"></a> `00ad4e18` | `bf 6a 36 38` | strb wzr,[x21, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00ad4e1c"></a> `00ad4e1c` | `61 22 40 a9` | ldp x1,x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad4e20"></a> `00ad4e20` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad4e24"></a> `00ad4e24` | `02 01 01 cb` | sub x2,x8,x1 | `FALL_THROUGH`
<a id="insn-00ad4e28"></a> `00ad4e28` | `55 01 02 cb` | sub x21,x10,x2 | `FALL_THROUGH`
<a id="insn-00ad4e2c"></a> `00ad4e2c` | `34 61 00 91` | add x20,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00ad4e30"></a> `00ad4e30` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4e34"></a> `00ad4e34` | `9f 18 04 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4e38"></a> `00ad4e38` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00ad4e3c"></a> `00ad4e3c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad4e40"></a> `00ad4e40` | `75 52 00 a9` | stp x21,x20,[x19] | `FALL_THROUGH`
<a id="insn-00ad4e44"></a> `00ad4e44` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ad4e48"></a> `00ad4e48` | `40 00 00 b4` | cbz x0,0x00ad4e50 | `CONDITIONAL_JUMP`
<a id="insn-00ad4e4c"></a> `00ad4e4c` | `45 18 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4e50"></a> `00ad4e50` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4e54"></a> `00ad4e54` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4e58"></a> `00ad4e58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4e5c"></a> `00ad4e5c` | `41 04 00 54` | b.ne 0x00ad4ee4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4e60"></a> `00ad4e60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad4e64"></a> `00ad4e64` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad4e68"></a> `00ad4e68` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad4e6c"></a> `00ad4e6c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad4e70"></a> `00ad4e70` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad4e74"></a> `00ad4e74` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ad4e78"></a> `00ad4e78` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad4e7c"></a> `00ad4e7c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4e80"></a> `00ad4e80` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4e84"></a> `00ad4e84` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4e88"></a> `00ad4e88` | `e1 02 00 54` | b.ne 0x00ad4ee4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4e8c"></a> `00ad4e8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad4e90"></a> `00ad4e90` | `63 25 e5 97` | bl 0x0041e41c | `UNCONDITIONAL_CALL`
<a id="insn-00ad4e94"></a> `00ad4e94` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4e98"></a> `00ad4e98` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4e9c"></a> `00ad4e9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4ea0"></a> `00ad4ea0` | `21 02 00 54` | b.ne 0x00ad4ee4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4ea4"></a> `00ad4ea4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4ea8"></a> `00ad4ea8` | `5f 0f e5 97` | bl 0x00418c24 | `CALL_TERMINATOR`
<a id="insn-00ad4eac"></a> `00ad4eac` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4eb0"></a> `00ad4eb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4eb4"></a> `00ad4eb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4eb8"></a> `00ad4eb8` | `61 01 00 54` | b.ne 0x00ad4ee4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4ebc"></a> `00ad4ebc` | `31 25 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00ad4ee4"></a> `00ad4ee4` | `2b 18 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad4cec`](#insn-00ad4cec) 範囲 `[['00ad4cec', '00ad4d3f']]`
  - `CONDITIONAL_JUMP` [`00ad4d3c`](#insn-00ad4d3c) → [`00ad4e7c`](#insn-00ad4e7c)
  - `FALL_THROUGH` [`00ad4d3c`](#insn-00ad4d3c) → [`00ad4d40`](#insn-00ad4d40)
- ブロック [`00ad4d40`](#insn-00ad4d40) 範囲 `[['00ad4d40', '00ad4d7b']]`
  - `CONDITIONAL_JUMP` [`00ad4d78`](#insn-00ad4d78) → [`00ad4d94`](#insn-00ad4d94)
  - `FALL_THROUGH` [`00ad4d78`](#insn-00ad4d78) → [`00ad4d7c`](#insn-00ad4d7c)
- ブロック [`00ad4d7c`](#insn-00ad4d7c) 範囲 `[['00ad4d7c', '00ad4d83']]`
  - `CONDITIONAL_JUMP` [`00ad4d80`](#insn-00ad4d80) → [`00ad4eac`](#insn-00ad4eac)
  - `FALL_THROUGH` [`00ad4d80`](#insn-00ad4d80) → [`00ad4d84`](#insn-00ad4d84)
- ブロック [`00ad4d84`](#insn-00ad4d84) 範囲 `[['00ad4d84', '00ad4d93']]`
  - `UNCONDITIONAL_JUMP` [`00ad4d90`](#insn-00ad4d90) → [`00ad4d98`](#insn-00ad4d98)
- ブロック [`00ad4d94`](#insn-00ad4d94) 範囲 `[['00ad4d94', '00ad4d97']]`
  - `FALL_THROUGH` [`00ad4d94`](#insn-00ad4d94) → [`00ad4d98`](#insn-00ad4d98)
- ブロック [`00ad4d98`](#insn-00ad4d98) 範囲 `[['00ad4d98', '00ad4dbb']]`
  - `CONDITIONAL_JUMP` [`00ad4db8`](#insn-00ad4db8) → [`00ad4e94`](#insn-00ad4e94)
  - `FALL_THROUGH` [`00ad4db8`](#insn-00ad4db8) → [`00ad4dbc`](#insn-00ad4dbc)
- ブロック [`00ad4dbc`](#insn-00ad4dbc) 範囲 `[['00ad4dbc', '00ad4dc7']]`
  - `CONDITIONAL_JUMP` [`00ad4dc4`](#insn-00ad4dc4) → [`00ad4dd8`](#insn-00ad4dd8)
  - `FALL_THROUGH` [`00ad4dc4`](#insn-00ad4dc4) → [`00ad4dc8`](#insn-00ad4dc8)
- ブロック [`00ad4dc8`](#insn-00ad4dc8) 範囲 `[['00ad4dc8', '00ad4dd3']]`
  - `CONDITIONAL_JUMP` [`00ad4dd0`](#insn-00ad4dd0) → [`00ad4e08`](#insn-00ad4e08)
  - `FALL_THROUGH` [`00ad4dd0`](#insn-00ad4dd0) → [`00ad4dd4`](#insn-00ad4dd4)
- ブロック [`00ad4dd4`](#insn-00ad4dd4) 範囲 `[['00ad4dd4', '00ad4dd7']]`
  - `UNCONDITIONAL_JUMP` [`00ad4dd4`](#insn-00ad4dd4) → [`00ad4e18`](#insn-00ad4e18)
- ブロック [`00ad4dd8`](#insn-00ad4dd8) 範囲 `[['00ad4dd8', '00ad4e07']]`
  - `FALL_THROUGH` [`00ad4e04`](#insn-00ad4e04) → [`00ad4e08`](#insn-00ad4e08)
- ブロック [`00ad4e08`](#insn-00ad4e08) 範囲 `[['00ad4e08', '00ad4e17']]`
  - `FALL_THROUGH` [`00ad4e14`](#insn-00ad4e14) → [`00ad4e18`](#insn-00ad4e18)
- ブロック [`00ad4e18`](#insn-00ad4e18) 範囲 `[['00ad4e18', '00ad4e4b']]`
  - `CONDITIONAL_JUMP` [`00ad4e48`](#insn-00ad4e48) → [`00ad4e50`](#insn-00ad4e50)
  - `FALL_THROUGH` [`00ad4e48`](#insn-00ad4e48) → [`00ad4e4c`](#insn-00ad4e4c)
- ブロック [`00ad4e4c`](#insn-00ad4e4c) 範囲 `[['00ad4e4c', '00ad4e4f']]`
  - `FALL_THROUGH` [`00ad4e4c`](#insn-00ad4e4c) → [`00ad4e50`](#insn-00ad4e50)
- ブロック [`00ad4e50`](#insn-00ad4e50) 範囲 `[['00ad4e50', '00ad4e5f']]`
  - `CONDITIONAL_JUMP` [`00ad4e5c`](#insn-00ad4e5c) → [`00ad4ee4`](#insn-00ad4ee4)
  - `FALL_THROUGH` [`00ad4e5c`](#insn-00ad4e5c) → [`00ad4e60`](#insn-00ad4e60)
- ブロック [`00ad4e60`](#insn-00ad4e60) 範囲 `[['00ad4e60', '00ad4e7b']]`
- ブロック [`00ad4e7c`](#insn-00ad4e7c) 範囲 `[['00ad4e7c', '00ad4e8b']]`
  - `CONDITIONAL_JUMP` [`00ad4e88`](#insn-00ad4e88) → [`00ad4ee4`](#insn-00ad4ee4)
  - `FALL_THROUGH` [`00ad4e88`](#insn-00ad4e88) → [`00ad4e8c`](#insn-00ad4e8c)
- ブロック [`00ad4e8c`](#insn-00ad4e8c) 範囲 `[['00ad4e8c', '00ad4e93']]`
  - `FALL_THROUGH` [`00ad4e90`](#insn-00ad4e90) → [`00ad4e94`](#insn-00ad4e94)
- ブロック [`00ad4e94`](#insn-00ad4e94) 範囲 `[['00ad4e94', '00ad4e9b']]`
  - `FALL_THROUGH` [`00ad4e98`](#insn-00ad4e98) → [`00ad4e9c`](#insn-00ad4e9c)
- ブロック [`00ad4e9c`](#insn-00ad4e9c) 範囲 `[['00ad4e9c', '00ad4ea3']]`
  - `CONDITIONAL_JUMP` [`00ad4ea0`](#insn-00ad4ea0) → [`00ad4ee4`](#insn-00ad4ee4)
  - `FALL_THROUGH` [`00ad4ea0`](#insn-00ad4ea0) → [`00ad4ea4`](#insn-00ad4ea4)
- ブロック [`00ad4ea4`](#insn-00ad4ea4) 範囲 `[['00ad4ea4', '00ad4eab']]`
- ブロック [`00ad4eac`](#insn-00ad4eac) 範囲 `[['00ad4eac', '00ad4ebb']]`
  - `CONDITIONAL_JUMP` [`00ad4eb8`](#insn-00ad4eb8) → [`00ad4ee4`](#insn-00ad4ee4)
  - `FALL_THROUGH` [`00ad4eb8`](#insn-00ad4eb8) → [`00ad4ebc`](#insn-00ad4ebc)
- ブロック [`00ad4ebc`](#insn-00ad4ebc) 範囲 `[['00ad4ebc', '00ad4ebf']]`
- ブロック [`00ad4ee4`](#insn-00ad4ee4) 範囲 `[['00ad4ee4', '00ad4ee7']]`

## 命令位置別の参照

- [`00ad4cf0`](#insn-00ad4cf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cf4`](#insn-00ad4cf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cf8`](#insn-00ad4cf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cfc`](#insn-00ad4cfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d18`](#insn-00ad4d18) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d3c`](#insn-00ad4d3c) → [`00ad4e7c`](#insn-00ad4e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d4c`](#insn-00ad4d4c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d78`](#insn-00ad4d78) → [`00ad4d94`](#insn-00ad4d94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d80`](#insn-00ad4d80) → [`00ad4eac`](#insn-00ad4eac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d8c`](#insn-00ad4d8c) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d90`](#insn-00ad4d90) → [`00ad4d98`](#insn-00ad4d98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4da4`](#insn-00ad4da4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dac`](#insn-00ad4dac) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4db0`](#insn-00ad4db0) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00ad4db8`](#insn-00ad4db8) → [`00ad4e94`](#insn-00ad4e94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dc4`](#insn-00ad4dc4) → [`00ad4dd8`](#insn-00ad4dd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dd0`](#insn-00ad4dd0) → [`00ad4e08`](#insn-00ad4e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dd4`](#insn-00ad4dd4) → [`00ad4e18`](#insn-00ad4e18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4df4`](#insn-00ad4df4) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e14`](#insn-00ad4e14) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e20`](#insn-00ad4e20) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e34`](#insn-00ad4e34) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e3c`](#insn-00ad4e3c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e48`](#insn-00ad4e48) → [`00ad4e50`](#insn-00ad4e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e4c`](#insn-00ad4e4c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e54`](#insn-00ad4e54) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e5c`](#insn-00ad4e5c) → [`00ad4ee4`](#insn-00ad4ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e64`](#insn-00ad4e64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e68`](#insn-00ad4e68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e6c`](#insn-00ad4e6c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e70`](#insn-00ad4e70) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e80`](#insn-00ad4e80) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e88`](#insn-00ad4e88) → [`00ad4ee4`](#insn-00ad4ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e90`](#insn-00ad4e90) → [`0041e41c`](../0041e/0041e41c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e41c` · 推定シンボル `None` · 推定型 `None`
- [`00ad4e98`](#insn-00ad4e98) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ea0`](#insn-00ad4ea0) → [`00ad4ee4`](#insn-00ad4ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ea8`](#insn-00ad4ea8) → [`00418c24`](../00418/00418c24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c24` · 推定シンボル `None` · 推定型 `None`
- [`00ad4eb0`](#insn-00ad4eb0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4eb8`](#insn-00ad4eb8) → [`00ad4ee4`](#insn-00ad4ee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ebc`](#insn-00ad4ebc) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ee4`](#insn-00ad4ee4) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad4cf0`](#insn-00ad4cf0)

~~~json
{
  "source": "00ad4cf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cf4`](#insn-00ad4cf4)

~~~json
{
  "source": "00ad4cf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cf8`](#insn-00ad4cf8)

~~~json
{
  "source": "00ad4cf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cfc`](#insn-00ad4cfc)

~~~json
{
  "source": "00ad4cfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d18`](#insn-00ad4d18)

~~~json
{
  "source": "00ad4d18",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d3c`](#insn-00ad4d3c)

~~~json
{
  "source": "00ad4d3c",
  "target": "00ad4e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d4c`](#insn-00ad4d4c)

~~~json
{
  "source": "00ad4d4c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d78`](#insn-00ad4d78)

~~~json
{
  "source": "00ad4d78",
  "target": "00ad4d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d80`](#insn-00ad4d80)

~~~json
{
  "source": "00ad4d80",
  "target": "00ad4eac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d8c`](#insn-00ad4d8c)

~~~json
{
  "source": "00ad4d8c",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4d90`](#insn-00ad4d90)

~~~json
{
  "source": "00ad4d90",
  "target": "00ad4d98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4da4`](#insn-00ad4da4)

~~~json
{
  "source": "00ad4da4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dac`](#insn-00ad4dac)

~~~json
{
  "source": "00ad4dac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4db0`](#insn-00ad4db0)

~~~json
{
  "source": "00ad4db0",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4db8`](#insn-00ad4db8)

~~~json
{
  "source": "00ad4db8",
  "target": "00ad4e94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dc4`](#insn-00ad4dc4)

~~~json
{
  "source": "00ad4dc4",
  "target": "00ad4dd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dd0`](#insn-00ad4dd0)

~~~json
{
  "source": "00ad4dd0",
  "target": "00ad4e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dd4`](#insn-00ad4dd4)

~~~json
{
  "source": "00ad4dd4",
  "target": "00ad4e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4df4`](#insn-00ad4df4)

~~~json
{
  "source": "00ad4df4",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4e14`](#insn-00ad4e14)

~~~json
{
  "source": "00ad4e14",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4e20`](#insn-00ad4e20)

~~~json
{
  "source": "00ad4e20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e34`](#insn-00ad4e34)

~~~json
{
  "source": "00ad4e34",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4e3c`](#insn-00ad4e3c)

~~~json
{
  "source": "00ad4e3c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e48`](#insn-00ad4e48)

~~~json
{
  "source": "00ad4e48",
  "target": "00ad4e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e4c`](#insn-00ad4e4c)

~~~json
{
  "source": "00ad4e4c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4e54`](#insn-00ad4e54)

~~~json
{
  "source": "00ad4e54",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e5c`](#insn-00ad4e5c)

~~~json
{
  "source": "00ad4e5c",
  "target": "00ad4ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e64`](#insn-00ad4e64)

~~~json
{
  "source": "00ad4e64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e68`](#insn-00ad4e68)

~~~json
{
  "source": "00ad4e68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e6c`](#insn-00ad4e6c)

~~~json
{
  "source": "00ad4e6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e70`](#insn-00ad4e70)

~~~json
{
  "source": "00ad4e70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e80`](#insn-00ad4e80)

~~~json
{
  "source": "00ad4e80",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e88`](#insn-00ad4e88)

~~~json
{
  "source": "00ad4e88",
  "target": "00ad4ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4e90`](#insn-00ad4e90)

~~~json
{
  "source": "00ad4e90",
  "target": "0041e41c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4e98`](#insn-00ad4e98)

~~~json
{
  "source": "00ad4e98",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4ea0`](#insn-00ad4ea0)

~~~json
{
  "source": "00ad4ea0",
  "target": "00ad4ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4ea8`](#insn-00ad4ea8)

~~~json
{
  "source": "00ad4ea8",
  "target": "00418c24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4eb0`](#insn-00ad4eb0)

~~~json
{
  "source": "00ad4eb0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4eb8`](#insn-00ad4eb8)

~~~json
{
  "source": "00ad4eb8",
  "target": "00ad4ee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4ebc`](#insn-00ad4ebc)

~~~json
{
  "source": "00ad4ebc",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4ee4`](#insn-00ad4ee4)

~~~json
{
  "source": "00ad4ee4",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
