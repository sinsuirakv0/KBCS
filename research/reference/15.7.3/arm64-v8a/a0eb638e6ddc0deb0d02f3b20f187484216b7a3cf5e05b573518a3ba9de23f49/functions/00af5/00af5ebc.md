# 00af5ebc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af5df4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af5/00af5df4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-894c9f2c0599fad4c3b4a1ee32757ed2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af5f00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5f00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-68800ce38337d722ca55b493100acaa1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5ebc",
  "name": "_ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7578960214fbb73b11328c9113b23c532ceca2f5e0d0103459447f4b910222c8",
  "source_text_sha256": "7578960214fbb73b11328c9113b23c532ceca2f5e0d0103459447f4b910222c8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5ebc",
        "00af5feb"
      ]
    ],
    "bytes_sha256": "38345fe3efc1ca4574fba601669435dc7a714cac1278f52b06c9919acbcc5c53",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bde050](../00bde/00bde050.md)
- [00bde7d0](../00bde/00bde7d0.md)
- [00bde7e0](../00bde/00bde7e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1588 bytes

~~~c

void _ZN8firebase4util32JniResultCallback_nativeOnResultEP7_JNIEnvP8_jobjectS4_hhP8_jstringll
               (long *param_1,undefined8 param_2,undefined8 param_3,char param_4,char param_5,
               undefined8 param_6,code *param_7,long *param_8)

{
  void *pvVar1;
  long *__ptr;
  long lVar2;
  long lVar3;
  long lVar4;
  long lVar5;
  undefined4 uVar6;
  byte local_80 [16];
  void *local_70;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
                    /* try { // try from 00af5ee8 to 00bf5eef has its CatchHandler @ 00affb10 */
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a0a88);
  lVar3 = param_8[1];
  uVar6 = 1;
  *(undefined1 *)(param_8 + 4) = 1;
  if (*param_8 != 0) {
    (**(code **)(*param_1 + 0xb0))(param_1);
    __ptr = (long *)param_8[2];
    lVar4 = param_8[3];
    lVar2 = *__ptr;
    *(long *)(lVar2 + 8) = __ptr[1];
    *(long *)__ptr[1] = lVar2;
    *(long *)(lVar4 + 0x10) = *(long *)(lVar4 + 0x10) + -1;
    _ZdlPv(__ptr);
  }
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a0a88);
  _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(local_80,param_1,param_6);
  if (param_5 != '\0') {
    uVar6 = 2;
  }
  if (param_4 != '\0') {
    uVar6 = 0;
  }
  pvVar1 = (void *)((ulong)local_80 | 1);
  if ((local_80[0] & 1) != 0) {
    pvVar1 = local_70;
  }
  (*param_7)(param_1,param_3,uVar6,pvVar1,lVar3);
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar5 + 0x28) == local_68) {
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
<a id="insn-00af5ebc"></a> `00af5ebc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00af5ec0"></a> `00af5ec0` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5ec4"></a> `00af5ec4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af5ec8"></a> `00af5ec8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af5ecc"></a> `00af5ecc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af5ed0"></a> `00af5ed0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af5ed4"></a> `00af5ed4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af5ed8"></a> `00af5ed8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00af5edc"></a> `00af5edc` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af5ee0"></a> `00af5ee0` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00af5ee4"></a> `00af5ee4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af5ee8"></a> `00af5ee8` | `40 2d 00 f0` | adrp x0,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5eec"></a> `00af5eec` | `00 20 2a 91` | add x0,x0,#0xa88 | `FALL_THROUGH`
<a id="insn-00af5ef0"></a> `00af5ef0` | `fa 03 07 aa` | mov x26,x7 | `FALL_THROUGH`
<a id="insn-00af5ef4"></a> `00af5ef4` | `f3 03 06 aa` | mov x19,x6 | `FALL_THROUGH`
<a id="insn-00af5ef8"></a> `00af5ef8` | `f9 03 05 aa` | mov x25,x5 | `FALL_THROUGH`
<a id="insn-00af5efc"></a> `00af5efc` | `f7 03 04 2a` | mov w23,w4 | `FALL_THROUGH`
<a id="insn-00af5f00"></a> `00af5f00` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00af5f04"></a> `00af5f04` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00af5f08"></a> `00af5f08` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af5f0c"></a> `00af5f0c` | `31 a2 03 94` | bl 0x00bde7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00af5f10"></a> `00af5f10` | `41 63 40 a9` | ldp x1,x24,[x26] | `FALL_THROUGH`
<a id="insn-00af5f14"></a> `00af5f14` | `3c 00 80 52` | mov w28,#0x1 | `FALL_THROUGH`
<a id="insn-00af5f18"></a> `00af5f18` | `5c 83 00 39` | strb w28,[x26, #0x20] | `FALL_THROUGH`
<a id="insn-00af5f1c"></a> `00af5f1c` | `c1 01 00 b4` | cbz x1,0x00af5f54 | `CONDITIONAL_JUMP`
<a id="insn-00af5f20"></a> `00af5f20` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00af5f24"></a> `00af5f24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af5f28"></a> `00af5f28` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00af5f2c"></a> `00af5f2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5f30"></a> `00af5f30` | `40 23 41 a9` | ldp x0,x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00af5f34"></a> `00af5f34` | `09 28 40 a9` | ldp x9,x10,[x0] | `FALL_THROUGH`
<a id="insn-00af5f38"></a> `00af5f38` | `2a 05 00 f9` | str x10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00af5f3c"></a> `00af5f3c` | `0a 04 40 f9` | ldr x10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af5f40"></a> `00af5f40` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00af5f44"></a> `00af5f44` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af5f48"></a> `00af5f48` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00af5f4c"></a> `00af5f4c` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af5f50"></a> `00af5f50` | `30 94 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00af5f54"></a> `00af5f54` | `40 2d 00 f0` | adrp x0,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af5f58"></a> `00af5f58` | `00 20 2a 91` | add x0,x0,#0xa88 | `FALL_THROUGH`
<a id="insn-00af5f5c"></a> `00af5f5c` | `21 a2 03 94` | bl 0x00bde7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af5f60"></a> `00af5f60` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00af5f64"></a> `00af5f64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af5f68"></a> `00af5f68` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00af5f6c"></a> `00af5f6c` | `fa 03 00 91` | mov x26,sp | `FALL_THROUGH`
<a id="insn-00af5f70"></a> `00af5f70` | `38 a0 03 94` | bl 0x00bde050 | `UNCONDITIONAL_CALL`
<a id="insn-00af5f74"></a> `00af5f74` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00af5f78"></a> `00af5f78` | `ea 0b 40 f9` | ldr x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5f7c"></a> `00af5f7c` | `ff 1e 00 72` | tst w23,#0xff | `FALL_THROUGH`
<a id="insn-00af5f80"></a> `00af5f80` | `89 07 9c 1a` | cinc w9,w28,ne | `FALL_THROUGH`
<a id="insn-00af5f84"></a> `00af5f84` | `df 1e 00 72` | tst w22,#0xff | `FALL_THROUGH`
<a id="insn-00af5f88"></a> `00af5f88` | `22 01 9f 1a` | csel w2,w9,wzr,eq | `FALL_THROUGH`
<a id="insn-00af5f8c"></a> `00af5f8c` | `49 03 40 b2` | orr x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00af5f90"></a> `00af5f90` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af5f94"></a> `00af5f94` | `23 01 8a 9a` | csel x3,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00af5f98"></a> `00af5f98` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af5f9c"></a> `00af5f9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af5fa0"></a> `00af5fa0` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00af5fa4"></a> `00af5fa4` | `60 02 3f d6` | blr x19 | `COMPUTED_CALL`
<a id="insn-00af5fa8"></a> `00af5fa8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00af5fac"></a> `00af5fac` | `68 00 00 36` | tbz w8,#0x0,0x00af5fb8 | `CONDITIONAL_JUMP`
<a id="insn-00af5fb0"></a> `00af5fb0` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5fb4"></a> `00af5fb4` | `17 94 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00af5fb8"></a> `00af5fb8` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00af5fbc"></a> `00af5fbc` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af5fc0"></a> `00af5fc0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af5fc4"></a> `00af5fc4` | `21 01 00 54` | b.ne 0x00af5fe8 | `CONDITIONAL_JUMP`
<a id="insn-00af5fc8"></a> `00af5fc8` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af5fcc"></a> `00af5fcc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af5fd0"></a> `00af5fd0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af5fd4"></a> `00af5fd4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af5fd8"></a> `00af5fd8` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af5fdc"></a> `00af5fdc` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5fe0"></a> `00af5fe0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00af5fe4"></a> `00af5fe4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af5fe8"></a> `00af5fe8` | `16 94 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af5ebc`](#insn-00af5ebc) 範囲 `[['00af5ebc', '00af5ee7']]`
  - `FALL_THROUGH` [`00af5ee4`](#insn-00af5ee4) → [`00af5ee8`](#insn-00af5ee8)
- ブロック [`00af5ee8`](#insn-00af5ee8) 範囲 `[['00af5ee8', '00af5f1f']]`
  - `CONDITIONAL_JUMP` [`00af5f1c`](#insn-00af5f1c) → [`00af5f54`](#insn-00af5f54)
  - `FALL_THROUGH` [`00af5f1c`](#insn-00af5f1c) → [`00af5f20`](#insn-00af5f20)
- ブロック [`00af5f20`](#insn-00af5f20) 範囲 `[['00af5f20', '00af5f53']]`
  - `FALL_THROUGH` [`00af5f50`](#insn-00af5f50) → [`00af5f54`](#insn-00af5f54)
- ブロック [`00af5f54`](#insn-00af5f54) 範囲 `[['00af5f54', '00af5faf']]`
  - `CONDITIONAL_JUMP` [`00af5fac`](#insn-00af5fac) → [`00af5fb8`](#insn-00af5fb8)
  - `FALL_THROUGH` [`00af5fac`](#insn-00af5fac) → [`00af5fb0`](#insn-00af5fb0)
- ブロック [`00af5fb0`](#insn-00af5fb0) 範囲 `[['00af5fb0', '00af5fb7']]`
  - `FALL_THROUGH` [`00af5fb4`](#insn-00af5fb4) → [`00af5fb8`](#insn-00af5fb8)
- ブロック [`00af5fb8`](#insn-00af5fb8) 範囲 `[['00af5fb8', '00af5fc7']]`
  - `CONDITIONAL_JUMP` [`00af5fc4`](#insn-00af5fc4) → [`00af5fe8`](#insn-00af5fe8)
  - `FALL_THROUGH` [`00af5fc4`](#insn-00af5fc4) → [`00af5fc8`](#insn-00af5fc8)
- ブロック [`00af5fc8`](#insn-00af5fc8) 範囲 `[['00af5fc8', '00af5fe7']]`
- ブロック [`00af5fe8`](#insn-00af5fe8) 範囲 `[['00af5fe8', '00af5feb']]`

## 命令位置別の参照

- [`00af5ec0`](#insn-00af5ec0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ec4`](#insn-00af5ec4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ec8`](#insn-00af5ec8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ecc`](#insn-00af5ecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ed0`](#insn-00af5ed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5ed4`](#insn-00af5ed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5eec`](#insn-00af5eec) → `010a0a88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5f08`](#insn-00af5f08) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5f0c`](#insn-00af5f0c) → [`00bde7d0`](../00bde/00bde7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde7d0` · 推定シンボル `None` · 推定型 `None`
- [`00af5f1c`](#insn-00af5f1c) → [`00af5f54`](#insn-00af5f54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5f50`](#insn-00af5f50) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00af5f58`](#insn-00af5f58) → `010a0a88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5f5c`](#insn-00af5f5c) → [`00bde7e0`](../00bde/00bde7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde7e0` · 推定シンボル `None` · 推定型 `None`
- [`00af5f70`](#insn-00af5f70) → [`00bde050`](../00bde/00bde050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde050` · 推定シンボル `None` · 推定型 `None`
- [`00af5f74`](#insn-00af5f74) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5f78`](#insn-00af5f78) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fa8`](#insn-00af5fa8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fac`](#insn-00af5fac) → [`00af5fb8`](#insn-00af5fb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fb0`](#insn-00af5fb0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fb4`](#insn-00af5fb4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00af5fbc`](#insn-00af5fbc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fc4`](#insn-00af5fc4) → [`00af5fe8`](#insn-00af5fe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fc8`](#insn-00af5fc8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fcc`](#insn-00af5fcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fd0`](#insn-00af5fd0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fd4`](#insn-00af5fd4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fd8`](#insn-00af5fd8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fdc`](#insn-00af5fdc) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5fe8`](#insn-00af5fe8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5ec0`](#insn-00af5ec0)

~~~json
{
  "source": "00af5ec0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ec4`](#insn-00af5ec4)

~~~json
{
  "source": "00af5ec4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ec8`](#insn-00af5ec8)

~~~json
{
  "source": "00af5ec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ecc`](#insn-00af5ecc)

~~~json
{
  "source": "00af5ecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ed0`](#insn-00af5ed0)

~~~json
{
  "source": "00af5ed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5ed4`](#insn-00af5ed4)

~~~json
{
  "source": "00af5ed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5eec`](#insn-00af5eec)

~~~json
{
  "source": "00af5eec",
  "target": "010a0a88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5f08`](#insn-00af5f08)

~~~json
{
  "source": "00af5f08",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5f0c`](#insn-00af5f0c)

~~~json
{
  "source": "00af5f0c",
  "target": "00bde7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5f1c`](#insn-00af5f1c)

~~~json
{
  "source": "00af5f1c",
  "target": "00af5f54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5f50`](#insn-00af5f50)

~~~json
{
  "source": "00af5f50",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5f58`](#insn-00af5f58)

~~~json
{
  "source": "00af5f58",
  "target": "010a0a88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5f5c`](#insn-00af5f5c)

~~~json
{
  "source": "00af5f5c",
  "target": "00bde7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5f70`](#insn-00af5f70)

~~~json
{
  "source": "00af5f70",
  "target": "00bde050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5f74`](#insn-00af5f74)

~~~json
{
  "source": "00af5f74",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5f78`](#insn-00af5f78)

~~~json
{
  "source": "00af5f78",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fa8`](#insn-00af5fa8)

~~~json
{
  "source": "00af5fa8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fac`](#insn-00af5fac)

~~~json
{
  "source": "00af5fac",
  "target": "00af5fb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fb0`](#insn-00af5fb0)

~~~json
{
  "source": "00af5fb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fb4`](#insn-00af5fb4)

~~~json
{
  "source": "00af5fb4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5fbc`](#insn-00af5fbc)

~~~json
{
  "source": "00af5fbc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fc4`](#insn-00af5fc4)

~~~json
{
  "source": "00af5fc4",
  "target": "00af5fe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fc8`](#insn-00af5fc8)

~~~json
{
  "source": "00af5fc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fcc`](#insn-00af5fcc)

~~~json
{
  "source": "00af5fcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fd0`](#insn-00af5fd0)

~~~json
{
  "source": "00af5fd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fd4`](#insn-00af5fd4)

~~~json
{
  "source": "00af5fd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fd8`](#insn-00af5fd8)

~~~json
{
  "source": "00af5fd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fdc`](#insn-00af5fdc)

~~~json
{
  "source": "00af5fdc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5fe8`](#insn-00af5fe8)

~~~json
{
  "source": "00af5fe8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
