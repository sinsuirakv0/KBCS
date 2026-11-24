# 00af4cdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af4c98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af4/00af4c98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-4d830bf938afd9beeffc1203cd8a6d48)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b54a60`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b54/00b54a60.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-083bbf007afa6b0aa5509c4be6260534)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af4cdc",
  "name": "_ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94647958ef482864a70dfd3b5f007f2a5a95589cb3d67b9e2d9f3927d575e0c4",
  "source_text_sha256": "94647958ef482864a70dfd3b5f007f2a5a95589cb3d67b9e2d9f3927d575e0c4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af4cdc",
        "00af4e57"
      ]
    ],
    "bytes_sha256": "3e78f36d7924681690f37d3c28fd731c97b71841b2c6150d1cd2b7be59376120",
    "instruction_count": 95,
    "instruction_bytes": 380,
    "body_bytes": 380,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00bde530](../00bde/00bde530.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdd9e0](../00bdd/00bdd9e0.md)
- [00bdd9f0](../00bdd/00bdd9f0.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1883 bytes

~~~c

void _ZN8firebase4util18JIntArrayToVariantEP7_JNIEnvP10_jintArray
               (undefined4 *param_1,long *param_2,undefined8 param_3)

{
  undefined4 *puVar1;
  long lVar2;
  int iVar3;
  long lVar4;
  long *plVar5;
  undefined4 *puVar6;
  long lVar7;
  ulong uVar8;
  ulong uVar9;
  undefined4 local_80 [2];
  long local_78;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  iVar3 = (**(code **)(*param_2 + 0x558))();
  lVar4 = (**(code **)(*param_2 + 0x5d8))(param_2,param_3,0);
  plVar5 = (long *)_Znwm(0x18);
  plVar5[1] = 0;
  plVar5[2] = 0;
  *plVar5 = 0;
  if (iVar3 != 0) {
    uVar8 = (ulong)iVar3;
    if (iVar3 < 0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    puVar6 = (undefined4 *)_Znwm(uVar8 * 0x18);
    puVar1 = puVar6 + uVar8 * 6;
    *plVar5 = (long)puVar6;
    plVar5[1] = (long)puVar6;
    plVar5[2] = (long)puVar1;
    do {
      *puVar6 = 0;
      *(undefined8 *)(puVar6 + 2) = 0;
      puVar6 = puVar6 + 6;
    } while (puVar1 != puVar6);
    plVar5[1] = (long)puVar1;
    if (iVar3 != 0) {
      lVar7 = 0;
      uVar9 = 0;
      do {
        iVar3 = *(int *)(lVar4 + uVar9 * 4);
        local_80[0] = 0;
        _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,1);
        local_78 = (long)iVar3;
        _ZN8firebase7VariantaSEOS0_(*plVar5 + lVar7,local_80);
        _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
        uVar9 = uVar9 + 1;
        lVar7 = lVar7 + 0x18;
      } while (uVar9 < uVar8);
    }
  }
  *param_1 = 0;
  *(undefined8 *)(param_1 + 2) = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(param_1,0);
  *param_1 = 6;
  *(long **)(param_1 + 2) = plVar5;
  (**(code **)(*param_2 + 0x618))(param_2,param_3,lVar4,2);
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af4cdc"></a> `00af4cdc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00af4ce0"></a> `00af4ce0` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4ce4"></a> `00af4ce4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af4ce8"></a> `00af4ce8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af4cec"></a> `00af4cec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af4cf0"></a> `00af4cf0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af4cf4"></a> `00af4cf4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af4cf8"></a> `00af4cf8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00af4cfc"></a> `00af4cfc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af4d00"></a> `00af4d00` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00af4d04"></a> `00af4d04` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00af4d08"></a> `00af4d08` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00af4d0c"></a> `00af4d0c` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00af4d10"></a> `00af4d10` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af4d14"></a> `00af4d14` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00af4d18"></a> `00af4d18` | `29 ad 42 f9` | ldr x9,[x9, #0x558] | `FALL_THROUGH`
<a id="insn-00af4d1c"></a> `00af4d1c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00af4d20"></a> `00af4d20` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00af4d24"></a> `00af4d24` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00af4d28"></a> `00af4d28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af4d2c"></a> `00af4d2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00af4d30"></a> `00af4d30` | `08 ed 42 f9` | ldr x8,[x8, #0x5d8] | `FALL_THROUGH`
<a id="insn-00af4d34"></a> `00af4d34` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00af4d38"></a> `00af4d38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af4d3c"></a> `00af4d3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00af4d40"></a> `00af4d40` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00af4d44"></a> `00af4d44` | `bf 98 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00af4d48"></a> `00af4d48` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00af4d4c"></a> `00af4d4c` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af4d50"></a> `00af4d50` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00af4d54"></a> `00af4d54` | `98 04 00 34` | cbz w24,0x00af4de4 | `CONDITIONAL_JUMP`
<a id="insn-00af4d58"></a> `00af4d58` | `1a 7f 40 93` | sxtw x26,w24 | `FALL_THROUGH`
<a id="insn-00af4d5c"></a> `00af4d5c` | `da 07 f8 37` | tbnz w26,#0x1f,0x00af4e54 | `CONDITIONAL_JUMP`
<a id="insn-00af4d60"></a> `00af4d60` | `48 07 1a 8b` | add x8,x26,x26, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00af4d64"></a> `00af4d64` | `18 f1 7d d3` | lsl x24,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00af4d68"></a> `00af4d68` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00af4d6c"></a> `00af4d6c` | `b5 98 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00af4d70"></a> `00af4d70` | `08 00 18 8b` | add x8,x0,x24 | `FALL_THROUGH`
<a id="insn-00af4d74"></a> `00af4d74` | `e0 02 00 a9` | stp x0,x0,[x23] | `FALL_THROUGH`
<a id="insn-00af4d78"></a> `00af4d78` | `e8 0a 00 f9` | str x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00af4d7c"></a> `00af4d7c` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00af4d80"></a> `00af4d80` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af4d84"></a> `00af4d84` | `00 60 00 91` | add x0,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00af4d88"></a> `00af4d88` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00af4d8c"></a> `00af4d8c` | `81 ff ff 54` | b.ne 0x00af4d7c | `CONDITIONAL_JUMP`
<a id="insn-00af4d90"></a> `00af4d90` | `e8 06 00 f9` | str x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00af4d94"></a> `00af4d94` | `9a 02 00 34` | cbz w26,0x00af4de4 | `CONDITIONAL_JUMP`
<a id="insn-00af4d98"></a> `00af4d98` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00af4d9c"></a> `00af4d9c` | `fb 03 1f aa` | mov x27,xzr | `FALL_THROUGH`
<a id="insn-00af4da0"></a> `00af4da0` | `dc 7a bb b8` | ldrsw x28,[x22, x27, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00af4da4"></a> `00af4da4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00af4da8"></a> `00af4da8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00af4dac"></a> `00af4dac` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00af4db0"></a> `00af4db0` | `0c a3 03 94` | bl 0x00bdd9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4db4"></a> `00af4db4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00af4db8"></a> `00af4db8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00af4dbc"></a> `00af4dbc` | `fc 07 00 f9` | str x28,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af4dc0"></a> `00af4dc0` | `00 01 18 8b` | add x0,x8,x24 | `FALL_THROUGH`
<a id="insn-00af4dc4"></a> `00af4dc4` | `0b a3 03 94` | bl 0x00bdd9f0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4dc8"></a> `00af4dc8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00af4dcc"></a> `00af4dcc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af4dd0"></a> `00af4dd0` | `04 a3 03 94` | bl 0x00bdd9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4dd4"></a> `00af4dd4` | `7b 07 00 91` | add x27,x27,#0x1 | `FALL_THROUGH`
<a id="insn-00af4dd8"></a> `00af4dd8` | `7f 03 1a eb` | cmp x27,x26 | `FALL_THROUGH`
<a id="insn-00af4ddc"></a> `00af4ddc` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00af4de0"></a> `00af4de0` | `03 fe ff 54` | b.cc 0x00af4da0 | `CONDITIONAL_JUMP`
<a id="insn-00af4de4"></a> `00af4de4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af4de8"></a> `00af4de8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af4dec"></a> `00af4dec` | `bf 02 00 b9` | str wzr,[x21] | `FALL_THROUGH`
<a id="insn-00af4df0"></a> `00af4df0` | `bf 06 00 f9` | str xzr,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00af4df4"></a> `00af4df4` | `fb a2 03 94` | bl 0x00bdd9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4df8"></a> `00af4df8` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00af4dfc"></a> `00af4dfc` | `a8 02 00 b9` | str w8,[x21] | `FALL_THROUGH`
<a id="insn-00af4e00"></a> `00af4e00` | `b7 06 00 f9` | str x23,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00af4e04"></a> `00af4e04` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00af4e08"></a> `00af4e08` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00af4e0c"></a> `00af4e0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af4e10"></a> `00af4e10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00af4e14"></a> `00af4e14` | `08 0d 43 f9` | ldr x8,[x8, #0x618] | `FALL_THROUGH`
<a id="insn-00af4e18"></a> `00af4e18` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00af4e1c"></a> `00af4e1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af4e20"></a> `00af4e20` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00af4e24"></a> `00af4e24` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af4e28"></a> `00af4e28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af4e2c"></a> `00af4e2c` | `21 01 00 54` | b.ne 0x00af4e50 | `CONDITIONAL_JUMP`
<a id="insn-00af4e30"></a> `00af4e30` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af4e34"></a> `00af4e34` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af4e38"></a> `00af4e38` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af4e3c"></a> `00af4e3c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af4e40"></a> `00af4e40` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af4e44"></a> `00af4e44` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4e48"></a> `00af4e48` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00af4e4c"></a> `00af4e4c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af4e50"></a> `00af4e50` | `90 98 03 94` | bl 0x00bdb090 | `CALL_TERMINATOR`
<a id="insn-00af4e54"></a> `00af4e54` | `1b a5 03 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af4cdc`](#insn-00af4cdc) 範囲 `[['00af4cdc', '00af4d57']]`
  - `CONDITIONAL_JUMP` [`00af4d54`](#insn-00af4d54) → [`00af4de4`](#insn-00af4de4)
  - `FALL_THROUGH` [`00af4d54`](#insn-00af4d54) → [`00af4d58`](#insn-00af4d58)
- ブロック [`00af4d58`](#insn-00af4d58) 範囲 `[['00af4d58', '00af4d5f']]`
  - `CONDITIONAL_JUMP` [`00af4d5c`](#insn-00af4d5c) → [`00af4e54`](#insn-00af4e54)
  - `FALL_THROUGH` [`00af4d5c`](#insn-00af4d5c) → [`00af4d60`](#insn-00af4d60)
- ブロック [`00af4d60`](#insn-00af4d60) 範囲 `[['00af4d60', '00af4d7b']]`
  - `FALL_THROUGH` [`00af4d78`](#insn-00af4d78) → [`00af4d7c`](#insn-00af4d7c)
- ブロック [`00af4d7c`](#insn-00af4d7c) 範囲 `[['00af4d7c', '00af4d8f']]`
  - `CONDITIONAL_JUMP` [`00af4d8c`](#insn-00af4d8c) → [`00af4d7c`](#insn-00af4d7c)
  - `FALL_THROUGH` [`00af4d8c`](#insn-00af4d8c) → [`00af4d90`](#insn-00af4d90)
- ブロック [`00af4d90`](#insn-00af4d90) 範囲 `[['00af4d90', '00af4d97']]`
  - `CONDITIONAL_JUMP` [`00af4d94`](#insn-00af4d94) → [`00af4de4`](#insn-00af4de4)
  - `FALL_THROUGH` [`00af4d94`](#insn-00af4d94) → [`00af4d98`](#insn-00af4d98)
- ブロック [`00af4d98`](#insn-00af4d98) 範囲 `[['00af4d98', '00af4d9f']]`
  - `FALL_THROUGH` [`00af4d9c`](#insn-00af4d9c) → [`00af4da0`](#insn-00af4da0)
- ブロック [`00af4da0`](#insn-00af4da0) 範囲 `[['00af4da0', '00af4de3']]`
  - `CONDITIONAL_JUMP` [`00af4de0`](#insn-00af4de0) → [`00af4da0`](#insn-00af4da0)
  - `FALL_THROUGH` [`00af4de0`](#insn-00af4de0) → [`00af4de4`](#insn-00af4de4)
- ブロック [`00af4de4`](#insn-00af4de4) 範囲 `[['00af4de4', '00af4e2f']]`
  - `CONDITIONAL_JUMP` [`00af4e2c`](#insn-00af4e2c) → [`00af4e50`](#insn-00af4e50)
  - `FALL_THROUGH` [`00af4e2c`](#insn-00af4e2c) → [`00af4e30`](#insn-00af4e30)
- ブロック [`00af4e30`](#insn-00af4e30) 範囲 `[['00af4e30', '00af4e4f']]`
- ブロック [`00af4e50`](#insn-00af4e50) 範囲 `[['00af4e50', '00af4e53']]`
- ブロック [`00af4e54`](#insn-00af4e54) 範囲 `[['00af4e54', '00af4e57']]`

## 命令位置別の参照

- [`00af4ce0`](#insn-00af4ce0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4ce4`](#insn-00af4ce4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4ce8`](#insn-00af4ce8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4cec`](#insn-00af4cec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4cf0`](#insn-00af4cf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4cf4`](#insn-00af4cf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d10`](#insn-00af4d10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d44`](#insn-00af4d44) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00af4d54`](#insn-00af4d54) → [`00af4de4`](#insn-00af4de4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d5c`](#insn-00af4d5c) → [`00af4e54`](#insn-00af4e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d6c`](#insn-00af4d6c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00af4d8c`](#insn-00af4d8c) → [`00af4d7c`](#insn-00af4d7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d94`](#insn-00af4d94) → [`00af4de4`](#insn-00af4de4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4dac`](#insn-00af4dac) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4db0`](#insn-00af4db0) → [`00bdd9e0`](../00bdd/00bdd9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd9e0` · 推定シンボル `None` · 推定型 `None`
- [`00af4dbc`](#insn-00af4dbc) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4dc4`](#insn-00af4dc4) → [`00bdd9f0`](../00bdd/00bdd9f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd9f0` · 推定シンボル `None` · 推定型 `None`
- [`00af4dd0`](#insn-00af4dd0) → [`00bdd9e0`](../00bdd/00bdd9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd9e0` · 推定シンボル `None` · 推定型 `None`
- [`00af4de0`](#insn-00af4de0) → [`00af4da0`](#insn-00af4da0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4df4`](#insn-00af4df4) → [`00bdd9e0`](../00bdd/00bdd9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd9e0` · 推定シンボル `None` · 推定型 `None`
- [`00af4e24`](#insn-00af4e24) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e2c`](#insn-00af4e2c) → [`00af4e50`](#insn-00af4e50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e30`](#insn-00af4e30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e34`](#insn-00af4e34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e38`](#insn-00af4e38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e3c`](#insn-00af4e3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e40`](#insn-00af4e40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e44`](#insn-00af4e44) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e50`](#insn-00af4e50) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00af4e54`](#insn-00af4e54) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af4ce0`](#insn-00af4ce0)

~~~json
{
  "source": "00af4ce0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4ce4`](#insn-00af4ce4)

~~~json
{
  "source": "00af4ce4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4ce8`](#insn-00af4ce8)

~~~json
{
  "source": "00af4ce8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4cec`](#insn-00af4cec)

~~~json
{
  "source": "00af4cec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4cf0`](#insn-00af4cf0)

~~~json
{
  "source": "00af4cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4cf4`](#insn-00af4cf4)

~~~json
{
  "source": "00af4cf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d10`](#insn-00af4d10)

~~~json
{
  "source": "00af4d10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d44`](#insn-00af4d44)

~~~json
{
  "source": "00af4d44",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d54`](#insn-00af4d54)

~~~json
{
  "source": "00af4d54",
  "target": "00af4de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d5c`](#insn-00af4d5c)

~~~json
{
  "source": "00af4d5c",
  "target": "00af4e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d6c`](#insn-00af4d6c)

~~~json
{
  "source": "00af4d6c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d8c`](#insn-00af4d8c)

~~~json
{
  "source": "00af4d8c",
  "target": "00af4d7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d94`](#insn-00af4d94)

~~~json
{
  "source": "00af4d94",
  "target": "00af4de4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4dac`](#insn-00af4dac)

~~~json
{
  "source": "00af4dac",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4db0`](#insn-00af4db0)

~~~json
{
  "source": "00af4db0",
  "target": "00bdd9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4dbc`](#insn-00af4dbc)

~~~json
{
  "source": "00af4dbc",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4dc4`](#insn-00af4dc4)

~~~json
{
  "source": "00af4dc4",
  "target": "00bdd9f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4dd0`](#insn-00af4dd0)

~~~json
{
  "source": "00af4dd0",
  "target": "00bdd9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4de0`](#insn-00af4de0)

~~~json
{
  "source": "00af4de0",
  "target": "00af4da0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4df4`](#insn-00af4df4)

~~~json
{
  "source": "00af4df4",
  "target": "00bdd9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4e24`](#insn-00af4e24)

~~~json
{
  "source": "00af4e24",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e2c`](#insn-00af4e2c)

~~~json
{
  "source": "00af4e2c",
  "target": "00af4e50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e30`](#insn-00af4e30)

~~~json
{
  "source": "00af4e30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e34`](#insn-00af4e34)

~~~json
{
  "source": "00af4e34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e38`](#insn-00af4e38)

~~~json
{
  "source": "00af4e38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e3c`](#insn-00af4e3c)

~~~json
{
  "source": "00af4e3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e40`](#insn-00af4e40)

~~~json
{
  "source": "00af4e40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e44`](#insn-00af4e44)

~~~json
{
  "source": "00af4e44",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e50`](#insn-00af4e50)

~~~json
{
  "source": "00af4e50",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4e54`](#insn-00af4e54)

~~~json
{
  "source": "00af4e54",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
