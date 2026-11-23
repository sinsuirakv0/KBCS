# 00b2ebec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b2eb24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b2e/00b2eb24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0065.md#compare-7609ac53286585ff362246be1280f8cd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b2ec30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2ec30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-ab1b513b9dad517c11e004bfe18bd671)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2ebec",
  "name": "_ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10b8e6cca61a1454143af334a03dd898111c183b542edfc91065939c51e660e6",
  "source_text_sha256": "10b8e6cca61a1454143af334a03dd898111c183b542edfc91065939c51e660e6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2ebec",
        "00b2ed43"
      ]
    ],
    "bytes_sha256": "33e5741f614a46608456e5c254da9665062b779c74c4911efb6704696dae4388",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0070](../00be0/00be0070.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2385 bytes

~~~c

void _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_
               (undefined8 *param_1,void *param_2,void *param_3)

{
  void *__src;
  long lVar1;
  ulong uVar2;
  size_t sVar3;
  void *pvVar4;
  ulong uVar5;
  
                    /* try { // try from 00b2ebf8 to 00c2eccb has its CatchHandler @ 00b2c36c */
  lVar1 = param_1[2];
  pvVar4 = (void *)*param_1;
  sVar3 = (long)param_3 - (long)param_2;
  uVar5 = (long)sVar3 >> 3;
  if ((ulong)(lVar1 - (long)pvVar4 >> 3) < uVar5) {
    if (pvVar4 != (void *)0x0) {
      param_1[1] = pvVar4;
      _ZdlPv(pvVar4);
      lVar1 = 0;
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
    }
    if (uVar5 >> 0x3d != 0) {
LAB_00b2ec70:
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if ((ulong)(lVar1 >> 3) < 0xfffffffffffffff) {
      uVar2 = lVar1 >> 2;
      if ((uVar5 <= uVar2) && (uVar5 = uVar2, uVar2 >> 0x3d != 0)) goto LAB_00b2ec70;
    }
    else {
      uVar5 = 0x1fffffffffffffff;
    }
    pvVar4 = (void *)_Znwm(uVar5 * 8);
                    /* try { // try from 00b2ed04 to 00c2ee77 has its CatchHandler @ 00b2c36c */
    *param_1 = pvVar4;
    param_1[1] = pvVar4;
    param_1[2] = (void *)((long)pvVar4 + uVar5 * 8);
    if (0 < (long)sVar3) {
      memcpy(pvVar4,param_2,sVar3);
      pvVar4 = (void *)((long)pvVar4 + sVar3);
    }
    param_1[1] = pvVar4;
  }
  else {
    uVar2 = param_1[1] - (long)pvVar4 >> 3;
    __src = (void *)((long)param_2 + (param_1[1] - (long)pvVar4));
    if (uVar5 <= uVar2) {
      __src = param_3;
    }
    sVar3 = (long)__src - (long)param_2;
    if (sVar3 != 0) {
      memmove(pvVar4,param_2,sVar3);
    }
    if (uVar2 < uVar5) {
      pvVar4 = (void *)param_1[1];
      sVar3 = (long)param_3 - (long)__src;
      if (0 < (long)sVar3) {
                    /* try { // try from 00b2eccc to 00c2ecd7 has its CatchHandler @ 00b2f890 */
        memcpy(pvVar4,__src,sVar3);
        pvVar4 = (void *)((long)pvVar4 + sVar3);
      }
      param_1[1] = pvVar4;
                    /* try { // try from 00b2ecd8 to 00c2ed03 has its CatchHandler @ 00b2f88c */
    }
    else {
      param_1[1] = (void *)((long)pvVar4 + ((long)sVar3 >> 3) * 8);
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2ebec"></a> `00b2ebec` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b2ebf0"></a> `00b2ebf0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ebf4"></a> `00b2ebf4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ebf8"></a> `00b2ebf8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2ebfc"></a> `00b2ebfc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2ec00"></a> `00b2ec00` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b2ec04"></a> `00b2ec04` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ec08"></a> `00b2ec08` | `17 00 40 f9` | ldr x23,[x0] | `FALL_THROUGH`
<a id="insn-00b2ec0c"></a> `00b2ec0c` | `55 00 01 cb` | sub x21,x2,x1 | `FALL_THROUGH`
<a id="insn-00b2ec10"></a> `00b2ec10` | `b9 fe 43 93` | asr x25,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ec14"></a> `00b2ec14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b2ec18"></a> `00b2ec18` | `09 01 17 cb` | sub x9,x8,x23 | `FALL_THROUGH`
<a id="insn-00b2ec1c"></a> `00b2ec1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2ec20"></a> `00b2ec20` | `3f 0f 89 eb` | cmp x25,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00b2ec24"></a> `00b2ec24` | `89 02 00 54` | b.ls 0x00b2ec74 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec28"></a> `00b2ec28` | `f7 00 00 b4` | cbz x23,0x00b2ec44 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec2c"></a> `00b2ec2c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b2ec30"></a> `00b2ec30` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ec34"></a> `00b2ec34` | `f7 b0 02 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ec38"></a> `00b2ec38` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00b2ec3c"></a> `00b2ec3c` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b2ec40"></a> `00b2ec40` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ec44"></a> `00b2ec44` | `29 ff 7d d3` | lsr x9,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00b2ec48"></a> `00b2ec48` | `49 01 00 b5` | cbnz x9,0x00b2ec70 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec4c"></a> `00b2ec4c` | `e9 eb 7f b2` | orr x9,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00b2ec50"></a> `00b2ec50` | `3f 0d 88 eb` | cmp x9,x8, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00b2ec54"></a> `00b2ec54` | `c3 04 00 54` | b.cc 0x00b2ecec | `CONDITIONAL_JUMP`
<a id="insn-00b2ec58"></a> `00b2ec58` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00b2ec5c"></a> `00b2ec5c` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00b2ec60"></a> `00b2ec60` | `83 04 00 54` | b.cc 0x00b2ecf0 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec64"></a> `00b2ec64` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00b2ec68"></a> `00b2ec68` | `f9 03 08 aa` | mov x25,x8 | `FALL_THROUGH`
<a id="insn-00b2ec6c"></a> `00b2ec6c` | `29 04 00 b4` | cbz x9,0x00b2ecf0 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec70"></a> `00b2ec70` | `80 bd 02 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00b2ec74"></a> `00b2ec74` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ec78"></a> `00b2ec78` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b2ec7c"></a> `00b2ec7c` | `08 01 17 cb` | sub x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00b2ec80"></a> `00b2ec80` | `1a fd 43 93` | asr x26,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ec84"></a> `00b2ec84` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00b2ec88"></a> `00b2ec88` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00b2ec8c"></a> `00b2ec8c` | `15 81 82 9a` | csel x21,x8,x2,hi | `FALL_THROUGH`
<a id="insn-00b2ec90"></a> `00b2ec90` | `b8 02 14 eb` | subs x24,x21,x20 | `FALL_THROUGH`
<a id="insn-00b2ec94"></a> `00b2ec94` | `a0 00 00 54` | b.eq 0x00b2eca8 | `CONDITIONAL_JUMP`
<a id="insn-00b2ec98"></a> `00b2ec98` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b2ec9c"></a> `00b2ec9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b2eca0"></a> `00b2eca0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00b2eca4"></a> `00b2eca4` | `ff b0 02 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2eca8"></a> `00b2eca8` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-00b2ecac"></a> `00b2ecac` | `89 01 00 54` | b.ls 0x00b2ecdc | `CONDITIONAL_JUMP`
<a id="insn-00b2ecb0"></a> `00b2ecb0` | `74 06 40 f9` | ldr x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ecb4"></a> `00b2ecb4` | `d6 02 15 cb` | sub x22,x22,x21 | `FALL_THROUGH`
<a id="insn-00b2ecb8"></a> `00b2ecb8` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00b2ecbc"></a> `00b2ecbc` | `cb 00 00 54` | b.lt 0x00b2ecd4 | `CONDITIONAL_JUMP`
<a id="insn-00b2ecc0"></a> `00b2ecc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b2ecc4"></a> `00b2ecc4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2ecc8"></a> `00b2ecc8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00b2eccc"></a> `00b2eccc` | `25 b1 02 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ecd0"></a> `00b2ecd0` | `94 02 16 8b` | add x20,x20,x22 | `FALL_THROUGH`
<a id="insn-00b2ecd4"></a> `00b2ecd4` | `74 06 00 f9` | str x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ecd8"></a> `00b2ecd8` | `15 00 00 14` | b 0x00b2ed2c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ecdc"></a> `00b2ecdc` | `08 ff 43 93` | asr x8,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ece0"></a> `00b2ece0` | `e8 0e 08 8b` | add x8,x23,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00b2ece4"></a> `00b2ece4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ece8"></a> `00b2ece8` | `11 00 00 14` | b 0x00b2ed2c | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ecec"></a> `00b2ecec` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00b2ecf0"></a> `00b2ecf0` | `37 f3 7d d3` | lsl x23,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00b2ecf4"></a> `00b2ecf4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b2ecf8"></a> `00b2ecf8` | `be b0 02 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ecfc"></a> `00b2ecfc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b2ed00"></a> `00b2ed00` | `08 00 17 8b` | add x8,x0,x23 | `FALL_THROUGH`
<a id="insn-00b2ed04"></a> `00b2ed04` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00b2ed08"></a> `00b2ed08` | `60 02 00 a9` | stp x0,x0,[x19] | `FALL_THROUGH`
<a id="insn-00b2ed0c"></a> `00b2ed0c` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ed10"></a> `00b2ed10` | `cb 00 00 54` | b.lt 0x00b2ed28 | `CONDITIONAL_JUMP`
<a id="insn-00b2ed14"></a> `00b2ed14` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b2ed18"></a> `00b2ed18` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b2ed1c"></a> `00b2ed1c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00b2ed20"></a> `00b2ed20` | `10 b1 02 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ed24"></a> `00b2ed24` | `d6 02 15 8b` | add x22,x22,x21 | `FALL_THROUGH`
<a id="insn-00b2ed28"></a> `00b2ed28` | `76 06 00 f9` | str x22,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ed2c"></a> `00b2ed2c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b2ed30"></a> `00b2ed30` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2ed34"></a> `00b2ed34` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ed38"></a> `00b2ed38` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ed3c"></a> `00b2ed3c` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b2ed40"></a> `00b2ed40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2ebec`](#insn-00b2ebec) 範囲 `[['00b2ebec', '00b2ebf7']]`
  - `FALL_THROUGH` [`00b2ebf4`](#insn-00b2ebf4) → [`00b2ebf8`](#insn-00b2ebf8)
- ブロック [`00b2ebf8`](#insn-00b2ebf8) 範囲 `[['00b2ebf8', '00b2ec27']]`
  - `CONDITIONAL_JUMP` [`00b2ec24`](#insn-00b2ec24) → [`00b2ec74`](#insn-00b2ec74)
  - `FALL_THROUGH` [`00b2ec24`](#insn-00b2ec24) → [`00b2ec28`](#insn-00b2ec28)
- ブロック [`00b2ec28`](#insn-00b2ec28) 範囲 `[['00b2ec28', '00b2ec2b']]`
  - `CONDITIONAL_JUMP` [`00b2ec28`](#insn-00b2ec28) → [`00b2ec44`](#insn-00b2ec44)
  - `FALL_THROUGH` [`00b2ec28`](#insn-00b2ec28) → [`00b2ec2c`](#insn-00b2ec2c)
- ブロック [`00b2ec2c`](#insn-00b2ec2c) 範囲 `[['00b2ec2c', '00b2ec43']]`
  - `FALL_THROUGH` [`00b2ec40`](#insn-00b2ec40) → [`00b2ec44`](#insn-00b2ec44)
- ブロック [`00b2ec44`](#insn-00b2ec44) 範囲 `[['00b2ec44', '00b2ec4b']]`
  - `CONDITIONAL_JUMP` [`00b2ec48`](#insn-00b2ec48) → [`00b2ec70`](#insn-00b2ec70)
  - `FALL_THROUGH` [`00b2ec48`](#insn-00b2ec48) → [`00b2ec4c`](#insn-00b2ec4c)
- ブロック [`00b2ec4c`](#insn-00b2ec4c) 範囲 `[['00b2ec4c', '00b2ec57']]`
  - `CONDITIONAL_JUMP` [`00b2ec54`](#insn-00b2ec54) → [`00b2ecec`](#insn-00b2ecec)
  - `FALL_THROUGH` [`00b2ec54`](#insn-00b2ec54) → [`00b2ec58`](#insn-00b2ec58)
- ブロック [`00b2ec58`](#insn-00b2ec58) 範囲 `[['00b2ec58', '00b2ec63']]`
  - `CONDITIONAL_JUMP` [`00b2ec60`](#insn-00b2ec60) → [`00b2ecf0`](#insn-00b2ecf0)
  - `FALL_THROUGH` [`00b2ec60`](#insn-00b2ec60) → [`00b2ec64`](#insn-00b2ec64)
- ブロック [`00b2ec64`](#insn-00b2ec64) 範囲 `[['00b2ec64', '00b2ec6f']]`
  - `CONDITIONAL_JUMP` [`00b2ec6c`](#insn-00b2ec6c) → [`00b2ecf0`](#insn-00b2ecf0)
  - `FALL_THROUGH` [`00b2ec6c`](#insn-00b2ec6c) → [`00b2ec70`](#insn-00b2ec70)
- ブロック [`00b2ec70`](#insn-00b2ec70) 範囲 `[['00b2ec70', '00b2ec73']]`
- ブロック [`00b2ec74`](#insn-00b2ec74) 範囲 `[['00b2ec74', '00b2ec97']]`
  - `CONDITIONAL_JUMP` [`00b2ec94`](#insn-00b2ec94) → [`00b2eca8`](#insn-00b2eca8)
  - `FALL_THROUGH` [`00b2ec94`](#insn-00b2ec94) → [`00b2ec98`](#insn-00b2ec98)
- ブロック [`00b2ec98`](#insn-00b2ec98) 範囲 `[['00b2ec98', '00b2eca7']]`
  - `FALL_THROUGH` [`00b2eca4`](#insn-00b2eca4) → [`00b2eca8`](#insn-00b2eca8)
- ブロック [`00b2eca8`](#insn-00b2eca8) 範囲 `[['00b2eca8', '00b2ecaf']]`
  - `CONDITIONAL_JUMP` [`00b2ecac`](#insn-00b2ecac) → [`00b2ecdc`](#insn-00b2ecdc)
  - `FALL_THROUGH` [`00b2ecac`](#insn-00b2ecac) → [`00b2ecb0`](#insn-00b2ecb0)
- ブロック [`00b2ecb0`](#insn-00b2ecb0) 範囲 `[['00b2ecb0', '00b2ecbf']]`
  - `CONDITIONAL_JUMP` [`00b2ecbc`](#insn-00b2ecbc) → [`00b2ecd4`](#insn-00b2ecd4)
  - `FALL_THROUGH` [`00b2ecbc`](#insn-00b2ecbc) → [`00b2ecc0`](#insn-00b2ecc0)
- ブロック [`00b2ecc0`](#insn-00b2ecc0) 範囲 `[['00b2ecc0', '00b2eccb']]`
  - `FALL_THROUGH` [`00b2ecc8`](#insn-00b2ecc8) → [`00b2eccc`](#insn-00b2eccc)
- ブロック [`00b2eccc`](#insn-00b2eccc) 範囲 `[['00b2eccc', '00b2ecd3']]`
  - `FALL_THROUGH` [`00b2ecd0`](#insn-00b2ecd0) → [`00b2ecd4`](#insn-00b2ecd4)
- ブロック [`00b2ecd4`](#insn-00b2ecd4) 範囲 `[['00b2ecd4', '00b2ecd7']]`
  - `FALL_THROUGH` [`00b2ecd4`](#insn-00b2ecd4) → [`00b2ecd8`](#insn-00b2ecd8)
- ブロック [`00b2ecd8`](#insn-00b2ecd8) 範囲 `[['00b2ecd8', '00b2ecdb']]`
  - `UNCONDITIONAL_JUMP` [`00b2ecd8`](#insn-00b2ecd8) → [`00b2ed2c`](#insn-00b2ed2c)
- ブロック [`00b2ecdc`](#insn-00b2ecdc) 範囲 `[['00b2ecdc', '00b2eceb']]`
  - `UNCONDITIONAL_JUMP` [`00b2ece8`](#insn-00b2ece8) → [`00b2ed2c`](#insn-00b2ed2c)
- ブロック [`00b2ecec`](#insn-00b2ecec) 範囲 `[['00b2ecec', '00b2ecef']]`
  - `FALL_THROUGH` [`00b2ecec`](#insn-00b2ecec) → [`00b2ecf0`](#insn-00b2ecf0)
- ブロック [`00b2ecf0`](#insn-00b2ecf0) 範囲 `[['00b2ecf0', '00b2ed03']]`
  - `FALL_THROUGH` [`00b2ed00`](#insn-00b2ed00) → [`00b2ed04`](#insn-00b2ed04)
- ブロック [`00b2ed04`](#insn-00b2ed04) 範囲 `[['00b2ed04', '00b2ed13']]`
  - `CONDITIONAL_JUMP` [`00b2ed10`](#insn-00b2ed10) → [`00b2ed28`](#insn-00b2ed28)
  - `FALL_THROUGH` [`00b2ed10`](#insn-00b2ed10) → [`00b2ed14`](#insn-00b2ed14)
- ブロック [`00b2ed14`](#insn-00b2ed14) 範囲 `[['00b2ed14', '00b2ed27']]`
  - `FALL_THROUGH` [`00b2ed24`](#insn-00b2ed24) → [`00b2ed28`](#insn-00b2ed28)
- ブロック [`00b2ed28`](#insn-00b2ed28) 範囲 `[['00b2ed28', '00b2ed2b']]`
  - `FALL_THROUGH` [`00b2ed28`](#insn-00b2ed28) → [`00b2ed2c`](#insn-00b2ed2c)
- ブロック [`00b2ed2c`](#insn-00b2ed2c) 範囲 `[['00b2ed2c', '00b2ed43']]`

## 命令位置別の参照

- [`00b2ebec`](#insn-00b2ebec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebf0`](#insn-00b2ebf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebf4`](#insn-00b2ebf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebf8`](#insn-00b2ebf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebfc`](#insn-00b2ebfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec24`](#insn-00b2ec24) → [`00b2ec74`](#insn-00b2ec74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec28`](#insn-00b2ec28) → [`00b2ec44`](#insn-00b2ec44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec34`](#insn-00b2ec34) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec48`](#insn-00b2ec48) → [`00b2ec70`](#insn-00b2ec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec54`](#insn-00b2ec54) → [`00b2ecec`](#insn-00b2ecec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec60`](#insn-00b2ec60) → [`00b2ecf0`](#insn-00b2ecf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec6c`](#insn-00b2ec6c) → [`00b2ecf0`](#insn-00b2ecf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec70`](#insn-00b2ec70) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec94`](#insn-00b2ec94) → [`00b2eca8`](#insn-00b2eca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eca4`](#insn-00b2eca4) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00b2ecac`](#insn-00b2ecac) → [`00b2ecdc`](#insn-00b2ecdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ecbc`](#insn-00b2ecbc) → [`00b2ecd4`](#insn-00b2ecd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eccc`](#insn-00b2eccc) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00b2ecd8`](#insn-00b2ecd8) → [`00b2ed2c`](#insn-00b2ed2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ece8`](#insn-00b2ece8) → [`00b2ed2c`](#insn-00b2ed2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ecf8`](#insn-00b2ecf8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed10`](#insn-00b2ed10) → [`00b2ed28`](#insn-00b2ed28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed20`](#insn-00b2ed20) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed2c`](#insn-00b2ed2c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed30`](#insn-00b2ed30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed34`](#insn-00b2ed34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ed38`](#insn-00b2ed38) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2ebec`](#insn-00b2ebec)

~~~json
{
  "source": "00b2ebec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebf0`](#insn-00b2ebf0)

~~~json
{
  "source": "00b2ebf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebf4`](#insn-00b2ebf4)

~~~json
{
  "source": "00b2ebf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebf8`](#insn-00b2ebf8)

~~~json
{
  "source": "00b2ebf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebfc`](#insn-00b2ebfc)

~~~json
{
  "source": "00b2ebfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec24`](#insn-00b2ec24)

~~~json
{
  "source": "00b2ec24",
  "target": "00b2ec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec28`](#insn-00b2ec28)

~~~json
{
  "source": "00b2ec28",
  "target": "00b2ec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec34`](#insn-00b2ec34)

~~~json
{
  "source": "00b2ec34",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ec48`](#insn-00b2ec48)

~~~json
{
  "source": "00b2ec48",
  "target": "00b2ec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec54`](#insn-00b2ec54)

~~~json
{
  "source": "00b2ec54",
  "target": "00b2ecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec60`](#insn-00b2ec60)

~~~json
{
  "source": "00b2ec60",
  "target": "00b2ecf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec6c`](#insn-00b2ec6c)

~~~json
{
  "source": "00b2ec6c",
  "target": "00b2ecf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec70`](#insn-00b2ec70)

~~~json
{
  "source": "00b2ec70",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ec94`](#insn-00b2ec94)

~~~json
{
  "source": "00b2ec94",
  "target": "00b2eca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eca4`](#insn-00b2eca4)

~~~json
{
  "source": "00b2eca4",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ecac`](#insn-00b2ecac)

~~~json
{
  "source": "00b2ecac",
  "target": "00b2ecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ecbc`](#insn-00b2ecbc)

~~~json
{
  "source": "00b2ecbc",
  "target": "00b2ecd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eccc`](#insn-00b2eccc)

~~~json
{
  "source": "00b2eccc",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ecd8`](#insn-00b2ecd8)

~~~json
{
  "source": "00b2ecd8",
  "target": "00b2ed2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ece8`](#insn-00b2ece8)

~~~json
{
  "source": "00b2ece8",
  "target": "00b2ed2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ecf8`](#insn-00b2ecf8)

~~~json
{
  "source": "00b2ecf8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ed10`](#insn-00b2ed10)

~~~json
{
  "source": "00b2ed10",
  "target": "00b2ed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ed20`](#insn-00b2ed20)

~~~json
{
  "source": "00b2ed20",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ed2c`](#insn-00b2ed2c)

~~~json
{
  "source": "00b2ed2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ed30`](#insn-00b2ed30)

~~~json
{
  "source": "00b2ed30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ed34`](#insn-00b2ed34)

~~~json
{
  "source": "00b2ed34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ed38`](#insn-00b2ed38)

~~~json
{
  "source": "00b2ed38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
