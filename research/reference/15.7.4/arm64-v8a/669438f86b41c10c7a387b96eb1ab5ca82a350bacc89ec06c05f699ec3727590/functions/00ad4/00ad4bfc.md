# 00ad4bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad4bb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4bb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-0ff70ef6473c77feab2338940a092be7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b34640`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b34/00b34640.md) · 移動量 `+0x5fa44`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0018.md#compare-5bffd83f57d54d40a4c21482ca95e0ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad4bfc",
  "name": "FUN_00ad4bfc",
  "size": 472,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23eb56be9696d36e081c3578986f27b2c6129ef858b53af6d8040bb57409ea7c",
  "source_text_sha256": "23eb56be9696d36e081c3578986f27b2c6129ef858b53af6d8040bb57409ea7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad4bfc",
        "00ad4dcf"
      ],
      [
        "00ad4df4",
        "00ad4df7"
      ]
    ],
    "bytes_sha256": "f2e54d9ff1f93304295a5a1167951d40eea30d2440a16e2da362b4b6cd82d254",
    "instruction_count": 118,
    "instruction_bytes": 472,
    "body_bytes": 472,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ad4530](../00ad4/00ad4530.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [0041e380](../0041e/0041e380.md)
- [0041e41c](../0041e/0041e41c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2595 bytes

~~~c

ulong * FUN_00ad4bfc(long *param_1,char *param_2)

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
        goto LAB_00ad4df4;
      }
      lVar6 = _Znwm((long)puVar7 * 0x18);
    }
    puVar8 = (ulong *)(lVar6 + lVar5 * 8);
    sVar3 = strlen(param_2);
    if (sVar3 < 0xfffffffffffffff8) {
      if (sVar3 < 0x17) {
        puVar9 = (undefined1 *)((long)puVar8 + 1);
        *(char *)puVar8 = (char)((int)sVar3 << 1);
        if (sVar3 != 0) goto LAB_00ad4d18;
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
LAB_00ad4d18:
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
      goto LAB_00ad4df4;
    }
  }
  else {
    if (*(long *)(lVar2 + 0x28) != lVar4) goto LAB_00ad4df4;
    FUN_0041e41c(param_1);
  }
  if (*(long *)(lVar2 + 0x28) == lVar4) {
                    /* WARNING: Subroutine does not return */
    FUN_00418c24(puVar8);
  }
LAB_00ad4df4:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad4bfc"></a> `00ad4bfc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ad4c00"></a> `00ad4c00` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad4c04"></a> `00ad4c04` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad4c08"></a> `00ad4c08` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad4c0c"></a> `00ad4c0c` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad4c10"></a> `00ad4c10` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad4c14"></a> `00ad4c14` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad4c18"></a> `00ad4c18` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ad4c1c"></a> `00ad4c1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad4c20"></a> `00ad4c20` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4c24"></a> `00ad4c24` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00ad4c28"></a> `00ad4c28` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4c2c"></a> `00ad4c2c` | `0a 20 40 a9` | ldp x10,x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad4c30"></a> `00ad4c30` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00ad4c34"></a> `00ad4c34` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4c38"></a> `00ad4c38` | `15 7d 0b 9b` | mul x21,x8,x11 | `FALL_THROUGH`
<a id="insn-00ad4c3c"></a> `00ad4c3c` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00ad4c40"></a> `00ad4c40` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00ad4c44"></a> `00ad4c44` | `a9 06 00 91` | add x9,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4c48"></a> `00ad4c48` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00ad4c4c"></a> `00ad4c4c` | `08 0a 00 54` | b.hi 0x00ad4d8c | `CONDITIONAL_JUMP`
<a id="insn-00ad4c50"></a> `00ad4c50` | `6c 42 00 91` | add x12,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00ad4c54"></a> `00ad4c54` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00ad4c58"></a> `00ad4c58` | `8d 01 40 f9` | ldr x13,[x12] | `FALL_THROUGH`
<a id="insn-00ad4c5c"></a> `00ad4c5c` | `ec 13 00 f9` | str x12,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad4c60"></a> `00ad4c60` | `aa 01 0a cb` | sub x10,x13,x10 | `FALL_THROUGH`
<a id="insn-00ad4c64"></a> `00ad4c64` | `ed f3 00 b2` | orr x13,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00ad4c68"></a> `00ad4c68` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4c6c"></a> `00ad4c6c` | `ad aa e0 f2` | movk x13,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00ad4c70"></a> `00ad4c70` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00ad4c74"></a> `00ad4c74` | `4b f9 7f d3` | lsl x11,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4c78"></a> `00ad4c78` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00ad4c7c"></a> `00ad4c7c` | `69 81 89 9a` | csel x9,x11,x9,hi | `FALL_THROUGH`
<a id="insn-00ad4c80"></a> `00ad4c80` | `5f 01 0d eb` | cmp x10,x13 | `FALL_THROUGH`
<a id="insn-00ad4c84"></a> `00ad4c84` | `36 31 88 9a` | csel x22,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00ad4c88"></a> `00ad4c88` | `f6 00 00 b4` | cbz x22,0x00ad4ca4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4c8c"></a> `00ad4c8c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00ad4c90"></a> `00ad4c90` | `68 09 00 54` | b.hi 0x00ad4dbc | `CONDITIONAL_JUMP`
<a id="insn-00ad4c94"></a> `00ad4c94` | `c8 06 16 8b` | add x8,x22,x22, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00ad4c98"></a> `00ad4c98` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ad4c9c"></a> `00ad4c9c` | `e9 18 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4ca0"></a> `00ad4ca0` | `02 00 00 14` | b 0x00ad4ca8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad4ca4"></a> `00ad4ca4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00ad4ca8"></a> `00ad4ca8` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00ad4cac"></a> `00ad4cac` | `b5 02 08 9b` | madd x21,x21,x8,x0 | `FALL_THROUGH`
<a id="insn-00ad4cb0"></a> `00ad4cb0` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00ad4cb4"></a> `00ad4cb4` | `e0 57 00 a9` | stp x0,x21,[sp] | `FALL_THROUGH`
<a id="insn-00ad4cb8"></a> `00ad4cb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad4cbc"></a> `00ad4cbc` | `f5 23 01 a9` | stp x21,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad4cc0"></a> `00ad4cc0` | `34 19 04 94` | bl 0x00bdb190 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4cc4"></a> `00ad4cc4` | `1f 20 00 b1` | cmn x0,#0x8 | `FALL_THROUGH`
<a id="insn-00ad4cc8"></a> `00ad4cc8` | `e2 06 00 54` | b.cs 0x00ad4da4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4ccc"></a> `00ad4ccc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ad4cd0"></a> `00ad4cd0` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-00ad4cd4"></a> `00ad4cd4` | `a2 00 00 54` | b.cs 0x00ad4ce8 | `CONDITIONAL_JUMP`
<a id="insn-00ad4cd8"></a> `00ad4cd8` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4cdc"></a> `00ad4cdc` | `a8 16 00 38` | strb w8,[x21], #0x1 | `FALL_THROUGH`
<a id="insn-00ad4ce0"></a> `00ad4ce0` | `d6 01 00 b5` | cbnz x22,0x00ad4d18 | `CONDITIONAL_JUMP`
<a id="insn-00ad4ce4"></a> `00ad4ce4` | `11 00 00 14` | b 0x00ad4d28 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad4ce8"></a> `00ad4ce8` | `c8 f2 7d 92` | and x8,x22,#-0x8 | `FALL_THROUGH`
<a id="insn-00ad4cec"></a> `00ad4cec` | `c9 0a 40 b2` | orr x9,x22,#0x7 | `FALL_THROUGH`
<a id="insn-00ad4cf0"></a> `00ad4cf0` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00ad4cf4"></a> `00ad4cf4` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-00ad4cf8"></a> `00ad4cf8` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00ad4cfc"></a> `00ad4cfc` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4d00"></a> `00ad4d00` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad4d04"></a> `00ad4d04` | `cf 18 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4d08"></a> `00ad4d08` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00ad4d0c"></a> `00ad4d0c` | `b6 82 00 a9` | stp x22,x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ad4d10"></a> `00ad4d10` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00ad4d14"></a> `00ad4d14` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ad4d18"></a> `00ad4d18` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4d1c"></a> `00ad4d1c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad4d20"></a> `00ad4d20` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ad4d24"></a> `00ad4d24` | `f3 18 04 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4d28"></a> `00ad4d28` | `bf 6a 36 38` | strb wzr,[x21, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00ad4d2c"></a> `00ad4d2c` | `61 22 40 a9` | ldp x1,x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad4d30"></a> `00ad4d30` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad4d34"></a> `00ad4d34` | `02 01 01 cb` | sub x2,x8,x1 | `FALL_THROUGH`
<a id="insn-00ad4d38"></a> `00ad4d38` | `55 01 02 cb` | sub x21,x10,x2 | `FALL_THROUGH`
<a id="insn-00ad4d3c"></a> `00ad4d3c` | `34 61 00 91` | add x20,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00ad4d40"></a> `00ad4d40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4d44"></a> `00ad4d44` | `1b 19 04 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4d48"></a> `00ad4d48` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00ad4d4c"></a> `00ad4d4c` | `e8 0f 40 f9` | ldr x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad4d50"></a> `00ad4d50` | `75 52 00 a9` | stp x21,x20,[x19] | `FALL_THROUGH`
<a id="insn-00ad4d54"></a> `00ad4d54` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ad4d58"></a> `00ad4d58` | `40 00 00 b4` | cbz x0,0x00ad4d60 | `CONDITIONAL_JUMP`
<a id="insn-00ad4d5c"></a> `00ad4d5c` | `c1 18 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00ad4d60"></a> `00ad4d60` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4d64"></a> `00ad4d64` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4d68"></a> `00ad4d68` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4d6c"></a> `00ad4d6c` | `41 04 00 54` | b.ne 0x00ad4df4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4d70"></a> `00ad4d70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad4d74"></a> `00ad4d74` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad4d78"></a> `00ad4d78` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ad4d7c"></a> `00ad4d7c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad4d80"></a> `00ad4d80` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad4d84"></a> `00ad4d84` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ad4d88"></a> `00ad4d88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad4d8c"></a> `00ad4d8c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4d90"></a> `00ad4d90` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4d94"></a> `00ad4d94` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4d98"></a> `00ad4d98` | `e1 02 00 54` | b.ne 0x00ad4df4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4d9c"></a> `00ad4d9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad4da0"></a> `00ad4da0` | `9f 25 e5 97` | bl 0x0041e41c | `UNCONDITIONAL_CALL`
<a id="insn-00ad4da4"></a> `00ad4da4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4da8"></a> `00ad4da8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4dac"></a> `00ad4dac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4db0"></a> `00ad4db0` | `21 02 00 54` | b.ne 0x00ad4df4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4db4"></a> `00ad4db4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad4db8"></a> `00ad4db8` | `9b 0f e5 97` | bl 0x00418c24 | `CALL_TERMINATOR`
<a id="insn-00ad4dbc"></a> `00ad4dbc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00ad4dc0"></a> `00ad4dc0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad4dc4"></a> `00ad4dc4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad4dc8"></a> `00ad4dc8` | `61 01 00 54` | b.ne 0x00ad4df4 | `CONDITIONAL_JUMP`
<a id="insn-00ad4dcc"></a> `00ad4dcc` | `6d 25 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00ad4df4"></a> `00ad4df4` | `a7 18 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad4bfc`](#insn-00ad4bfc) 範囲 `[['00ad4bfc', '00ad4c4f']]`
  - `CONDITIONAL_JUMP` [`00ad4c4c`](#insn-00ad4c4c) → [`00ad4d8c`](#insn-00ad4d8c)
  - `FALL_THROUGH` [`00ad4c4c`](#insn-00ad4c4c) → [`00ad4c50`](#insn-00ad4c50)
- ブロック [`00ad4c50`](#insn-00ad4c50) 範囲 `[['00ad4c50', '00ad4c8b']]`
  - `CONDITIONAL_JUMP` [`00ad4c88`](#insn-00ad4c88) → [`00ad4ca4`](#insn-00ad4ca4)
  - `FALL_THROUGH` [`00ad4c88`](#insn-00ad4c88) → [`00ad4c8c`](#insn-00ad4c8c)
- ブロック [`00ad4c8c`](#insn-00ad4c8c) 範囲 `[['00ad4c8c', '00ad4c93']]`
  - `CONDITIONAL_JUMP` [`00ad4c90`](#insn-00ad4c90) → [`00ad4dbc`](#insn-00ad4dbc)
  - `FALL_THROUGH` [`00ad4c90`](#insn-00ad4c90) → [`00ad4c94`](#insn-00ad4c94)
- ブロック [`00ad4c94`](#insn-00ad4c94) 範囲 `[['00ad4c94', '00ad4ca3']]`
  - `UNCONDITIONAL_JUMP` [`00ad4ca0`](#insn-00ad4ca0) → [`00ad4ca8`](#insn-00ad4ca8)
- ブロック [`00ad4ca4`](#insn-00ad4ca4) 範囲 `[['00ad4ca4', '00ad4ca7']]`
  - `FALL_THROUGH` [`00ad4ca4`](#insn-00ad4ca4) → [`00ad4ca8`](#insn-00ad4ca8)
- ブロック [`00ad4ca8`](#insn-00ad4ca8) 範囲 `[['00ad4ca8', '00ad4ccb']]`
  - `CONDITIONAL_JUMP` [`00ad4cc8`](#insn-00ad4cc8) → [`00ad4da4`](#insn-00ad4da4)
  - `FALL_THROUGH` [`00ad4cc8`](#insn-00ad4cc8) → [`00ad4ccc`](#insn-00ad4ccc)
- ブロック [`00ad4ccc`](#insn-00ad4ccc) 範囲 `[['00ad4ccc', '00ad4cd7']]`
  - `CONDITIONAL_JUMP` [`00ad4cd4`](#insn-00ad4cd4) → [`00ad4ce8`](#insn-00ad4ce8)
  - `FALL_THROUGH` [`00ad4cd4`](#insn-00ad4cd4) → [`00ad4cd8`](#insn-00ad4cd8)
- ブロック [`00ad4cd8`](#insn-00ad4cd8) 範囲 `[['00ad4cd8', '00ad4ce3']]`
  - `CONDITIONAL_JUMP` [`00ad4ce0`](#insn-00ad4ce0) → [`00ad4d18`](#insn-00ad4d18)
  - `FALL_THROUGH` [`00ad4ce0`](#insn-00ad4ce0) → [`00ad4ce4`](#insn-00ad4ce4)
- ブロック [`00ad4ce4`](#insn-00ad4ce4) 範囲 `[['00ad4ce4', '00ad4ce7']]`
  - `UNCONDITIONAL_JUMP` [`00ad4ce4`](#insn-00ad4ce4) → [`00ad4d28`](#insn-00ad4d28)
- ブロック [`00ad4ce8`](#insn-00ad4ce8) 範囲 `[['00ad4ce8', '00ad4d17']]`
  - `FALL_THROUGH` [`00ad4d14`](#insn-00ad4d14) → [`00ad4d18`](#insn-00ad4d18)
- ブロック [`00ad4d18`](#insn-00ad4d18) 範囲 `[['00ad4d18', '00ad4d27']]`
  - `FALL_THROUGH` [`00ad4d24`](#insn-00ad4d24) → [`00ad4d28`](#insn-00ad4d28)
- ブロック [`00ad4d28`](#insn-00ad4d28) 範囲 `[['00ad4d28', '00ad4d5b']]`
  - `CONDITIONAL_JUMP` [`00ad4d58`](#insn-00ad4d58) → [`00ad4d60`](#insn-00ad4d60)
  - `FALL_THROUGH` [`00ad4d58`](#insn-00ad4d58) → [`00ad4d5c`](#insn-00ad4d5c)
- ブロック [`00ad4d5c`](#insn-00ad4d5c) 範囲 `[['00ad4d5c', '00ad4d5f']]`
  - `FALL_THROUGH` [`00ad4d5c`](#insn-00ad4d5c) → [`00ad4d60`](#insn-00ad4d60)
- ブロック [`00ad4d60`](#insn-00ad4d60) 範囲 `[['00ad4d60', '00ad4d6f']]`
  - `CONDITIONAL_JUMP` [`00ad4d6c`](#insn-00ad4d6c) → [`00ad4df4`](#insn-00ad4df4)
  - `FALL_THROUGH` [`00ad4d6c`](#insn-00ad4d6c) → [`00ad4d70`](#insn-00ad4d70)
- ブロック [`00ad4d70`](#insn-00ad4d70) 範囲 `[['00ad4d70', '00ad4d8b']]`
- ブロック [`00ad4d8c`](#insn-00ad4d8c) 範囲 `[['00ad4d8c', '00ad4d9b']]`
  - `CONDITIONAL_JUMP` [`00ad4d98`](#insn-00ad4d98) → [`00ad4df4`](#insn-00ad4df4)
  - `FALL_THROUGH` [`00ad4d98`](#insn-00ad4d98) → [`00ad4d9c`](#insn-00ad4d9c)
- ブロック [`00ad4d9c`](#insn-00ad4d9c) 範囲 `[['00ad4d9c', '00ad4da3']]`
  - `FALL_THROUGH` [`00ad4da0`](#insn-00ad4da0) → [`00ad4da4`](#insn-00ad4da4)
- ブロック [`00ad4da4`](#insn-00ad4da4) 範囲 `[['00ad4da4', '00ad4db3']]`
  - `CONDITIONAL_JUMP` [`00ad4db0`](#insn-00ad4db0) → [`00ad4df4`](#insn-00ad4df4)
  - `FALL_THROUGH` [`00ad4db0`](#insn-00ad4db0) → [`00ad4db4`](#insn-00ad4db4)
- ブロック [`00ad4db4`](#insn-00ad4db4) 範囲 `[['00ad4db4', '00ad4dbb']]`
- ブロック [`00ad4dbc`](#insn-00ad4dbc) 範囲 `[['00ad4dbc', '00ad4dcb']]`
  - `CONDITIONAL_JUMP` [`00ad4dc8`](#insn-00ad4dc8) → [`00ad4df4`](#insn-00ad4df4)
  - `FALL_THROUGH` [`00ad4dc8`](#insn-00ad4dc8) → [`00ad4dcc`](#insn-00ad4dcc)
- ブロック [`00ad4dcc`](#insn-00ad4dcc) 範囲 `[['00ad4dcc', '00ad4dcf']]`
- ブロック [`00ad4df4`](#insn-00ad4df4) 範囲 `[['00ad4df4', '00ad4df7']]`

## 命令位置別の参照

- [`00ad4c00`](#insn-00ad4c00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c04`](#insn-00ad4c04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c08`](#insn-00ad4c08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c0c`](#insn-00ad4c0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c28`](#insn-00ad4c28) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c4c`](#insn-00ad4c4c) → [`00ad4d8c`](#insn-00ad4d8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c5c`](#insn-00ad4c5c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c88`](#insn-00ad4c88) → [`00ad4ca4`](#insn-00ad4ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c90`](#insn-00ad4c90) → [`00ad4dbc`](#insn-00ad4dbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4c9c`](#insn-00ad4c9c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ca0`](#insn-00ad4ca0) → [`00ad4ca8`](#insn-00ad4ca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cb4`](#insn-00ad4cb4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cbc`](#insn-00ad4cbc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cc0`](#insn-00ad4cc0) → [`00bdb190`](../00bdb/00bdb190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb190` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cc8`](#insn-00ad4cc8) → [`00ad4da4`](#insn-00ad4da4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4cd4`](#insn-00ad4cd4) → [`00ad4ce8`](#insn-00ad4ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ce0`](#insn-00ad4ce0) → [`00ad4d18`](#insn-00ad4d18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4ce4`](#insn-00ad4ce4) → [`00ad4d28`](#insn-00ad4d28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d04`](#insn-00ad4d04) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d24`](#insn-00ad4d24) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d30`](#insn-00ad4d30) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d44`](#insn-00ad4d44) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d4c`](#insn-00ad4d4c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d58`](#insn-00ad4d58) → [`00ad4d60`](#insn-00ad4d60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d5c`](#insn-00ad4d5c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d64`](#insn-00ad4d64) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d6c`](#insn-00ad4d6c) → [`00ad4df4`](#insn-00ad4df4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d74`](#insn-00ad4d74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d78`](#insn-00ad4d78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d7c`](#insn-00ad4d7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d80`](#insn-00ad4d80) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d90`](#insn-00ad4d90) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4d98`](#insn-00ad4d98) → [`00ad4df4`](#insn-00ad4df4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4da0`](#insn-00ad4da0) → [`0041e41c`](../0041e/0041e41c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e41c` · 推定シンボル `None` · 推定型 `None`
- [`00ad4da8`](#insn-00ad4da8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4db0`](#insn-00ad4db0) → [`00ad4df4`](#insn-00ad4df4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4db8`](#insn-00ad4db8) → [`00418c24`](../00418/00418c24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c24` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dc0`](#insn-00ad4dc0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dc8`](#insn-00ad4dc8) → [`00ad4df4`](#insn-00ad4df4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad4dcc`](#insn-00ad4dcc) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00ad4df4`](#insn-00ad4df4) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad4c00`](#insn-00ad4c00)

~~~json
{
  "source": "00ad4c00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c04`](#insn-00ad4c04)

~~~json
{
  "source": "00ad4c04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c08`](#insn-00ad4c08)

~~~json
{
  "source": "00ad4c08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c0c`](#insn-00ad4c0c)

~~~json
{
  "source": "00ad4c0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c28`](#insn-00ad4c28)

~~~json
{
  "source": "00ad4c28",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c4c`](#insn-00ad4c4c)

~~~json
{
  "source": "00ad4c4c",
  "target": "00ad4d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c5c`](#insn-00ad4c5c)

~~~json
{
  "source": "00ad4c5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c88`](#insn-00ad4c88)

~~~json
{
  "source": "00ad4c88",
  "target": "00ad4ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c90`](#insn-00ad4c90)

~~~json
{
  "source": "00ad4c90",
  "target": "00ad4dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4c9c`](#insn-00ad4c9c)

~~~json
{
  "source": "00ad4c9c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4ca0`](#insn-00ad4ca0)

~~~json
{
  "source": "00ad4ca0",
  "target": "00ad4ca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cb4`](#insn-00ad4cb4)

~~~json
{
  "source": "00ad4cb4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cbc`](#insn-00ad4cbc)

~~~json
{
  "source": "00ad4cbc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cc0`](#insn-00ad4cc0)

~~~json
{
  "source": "00ad4cc0",
  "target": "00bdb190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4cc8`](#insn-00ad4cc8)

~~~json
{
  "source": "00ad4cc8",
  "target": "00ad4da4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4cd4`](#insn-00ad4cd4)

~~~json
{
  "source": "00ad4cd4",
  "target": "00ad4ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4ce0`](#insn-00ad4ce0)

~~~json
{
  "source": "00ad4ce0",
  "target": "00ad4d18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4ce4`](#insn-00ad4ce4)

~~~json
{
  "source": "00ad4ce4",
  "target": "00ad4d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d04`](#insn-00ad4d04)

~~~json
{
  "source": "00ad4d04",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4d24`](#insn-00ad4d24)

~~~json
{
  "source": "00ad4d24",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4d30`](#insn-00ad4d30)

~~~json
{
  "source": "00ad4d30",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d44`](#insn-00ad4d44)

~~~json
{
  "source": "00ad4d44",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4d4c`](#insn-00ad4d4c)

~~~json
{
  "source": "00ad4d4c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d58`](#insn-00ad4d58)

~~~json
{
  "source": "00ad4d58",
  "target": "00ad4d60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d5c`](#insn-00ad4d5c)

~~~json
{
  "source": "00ad4d5c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4d64`](#insn-00ad4d64)

~~~json
{
  "source": "00ad4d64",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d6c`](#insn-00ad4d6c)

~~~json
{
  "source": "00ad4d6c",
  "target": "00ad4df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d74`](#insn-00ad4d74)

~~~json
{
  "source": "00ad4d74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d78`](#insn-00ad4d78)

~~~json
{
  "source": "00ad4d78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d7c`](#insn-00ad4d7c)

~~~json
{
  "source": "00ad4d7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d80`](#insn-00ad4d80)

~~~json
{
  "source": "00ad4d80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d90`](#insn-00ad4d90)

~~~json
{
  "source": "00ad4d90",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4d98`](#insn-00ad4d98)

~~~json
{
  "source": "00ad4d98",
  "target": "00ad4df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4da0`](#insn-00ad4da0)

~~~json
{
  "source": "00ad4da0",
  "target": "0041e41c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4da8`](#insn-00ad4da8)

~~~json
{
  "source": "00ad4da8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4db0`](#insn-00ad4db0)

~~~json
{
  "source": "00ad4db0",
  "target": "00ad4df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4db8`](#insn-00ad4db8)

~~~json
{
  "source": "00ad4db8",
  "target": "00418c24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4dc0`](#insn-00ad4dc0)

~~~json
{
  "source": "00ad4dc0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dc8`](#insn-00ad4dc8)

~~~json
{
  "source": "00ad4dc8",
  "target": "00ad4df4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad4dcc`](#insn-00ad4dcc)

~~~json
{
  "source": "00ad4dcc",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad4df4`](#insn-00ad4df4)

~~~json
{
  "source": "00ad4df4",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
