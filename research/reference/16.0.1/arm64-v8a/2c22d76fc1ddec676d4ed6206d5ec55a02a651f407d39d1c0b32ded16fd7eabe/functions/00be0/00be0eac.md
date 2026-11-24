# 00be0eac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00be0a84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0a84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-77ee09f4342f579bee4f16cd7932f328)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00be0f48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be0/00be0f48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0010.md#compare-fe52c7503df0e61eae27874c1fa07cf1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00be0eac",
  "name": "_ZN8firebase4auth4User6DeleteEv",
  "size": 416,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "829407e523b711f403444e0f00d8b4a25f5d83e7c4f04e414ed5ad21b08568d1",
  "source_text_sha256": "829407e523b711f403444e0f00d8b4a25f5d83e7c4f04e414ed5ad21b08568d1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00be0eac",
        "00be104b"
      ]
    ],
    "bytes_sha256": "632596cce49c142f7670abb0914afa2825203588c0b2941b564b2ac34dacd3e0",
    "instruction_count": 104,
    "instruction_bytes": 416,
    "body_bytes": 416,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5aa80](../00c5a/00c5aa80.md)

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5abe0](../00c5a/00c5abe0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5add0](../00c5a/00c5add0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5ae40](../00c5a/00c5ae40.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dd00](../00c5d/00c5dd00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2904 bytes

~~~c

void _ZN8firebase4auth4User6DeleteEv(long param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  undefined8 uVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  undefined8 *puVar9;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  lVar8 = *(long *)(param_2 + 0x98);
  if ((lVar8 == 0) || (*(long *)(lVar8 + 0x200) == 0)) {
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar8 = lVar8 + 0x10;
                    /* try { // try from 00be0ef0 to 00ce0efb has its CatchHandler @ 00be1120 */
    _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(auStack_68,lVar8,0x18,0,0);
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00be0f20 to 00ce0f2b has its CatchHandler @ 00be1110 */
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
                    /* try { // try from 00be0f2c to 00ce0f47 has its CatchHandler @ 00be1130 */
    uVar3 = FUN_00497834(plVar2,*(undefined8 *)(*(long *)(param_2 + 0x98) + 0x200),DAT_01126d90);
                    /* try { // try from 00be0f48 to 00ce11af has its CatchHandler @ 00be0c3c */
    uVar4 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorIvEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar2,lVar8,auStack_78);
    if ((uVar4 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
      puVar9 = *(undefined8 **)(param_2 + 0x98);
      uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar9);
      lVar6 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar6,auStack_88);
      *(undefined8 **)(lVar6 + 0x10) = puVar9;
      *(code **)(lVar6 + 0x18) = FUN_00be129c;
      if ((*(byte *)(puVar9 + 0x28) & 1) == 0) {
        lVar7 = (long)puVar9 + 0x141;
      }
      else {
        lVar7 = puVar9[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar5,uVar3,
                 PTR__ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba18
                 ,lVar6,lVar7);
      _ZN8firebase12FutureHandleD2Ev(auStack_88);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    }
    _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar8,auStack_78);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
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
<a id="insn-00be0eac"></a> `00be0eac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00be0eb0"></a> `00be0eb0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00be0eb4"></a> `00be0eb4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be0eb8"></a> `00be0eb8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00be0ebc"></a> `00be0ebc` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00be0ec0"></a> `00be0ec0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00be0ec4"></a> `00be0ec4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00be0ec8"></a> `00be0ec8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00be0ecc"></a> `00be0ecc` | `29 17 40 f9` | ldr x9,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00be0ed0"></a> `00be0ed0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00be0ed4"></a> `00be0ed4` | `e9 1f 00 f9` | str x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00be0ed8"></a> `00be0ed8` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00be0edc"></a> `00be0edc` | `69 06 00 b4` | cbz x9,0x00be0fa8 | `CONDITIONAL_JUMP`
<a id="insn-00be0ee0"></a> `00be0ee0` | `28 01 41 f9` | ldr x8,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00be0ee4"></a> `00be0ee4` | `28 06 00 b4` | cbz x8,0x00be0fa8 | `CONDITIONAL_JUMP`
<a id="insn-00be0ee8"></a> `00be0ee8` | `34 41 00 91` | add x20,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00be0eec"></a> `00be0eec` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00be0ef0"></a> `00be0ef0` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00be0ef4"></a> `00be0ef4` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00be0ef8"></a> `00be0ef8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00be0efc"></a> `00be0efc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00be0f00"></a> `00be0f00` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00be0f04"></a> `00be0f04` | `cf e7 01 94` | bl 0x00c5ae40 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f08"></a> `00be0f08` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0f0c"></a> `00be0f0c` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00be0f10"></a> `00be0f10` | `bc e7 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f14"></a> `00be0f14` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00be0f18"></a> `00be0f18` | `de e6 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f1c"></a> `00be0f1c` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be0f20"></a> `00be0f20` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00be0f24"></a> `00be0f24` | `57 e8 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f28"></a> `00be0f28` | `e8 4e 40 f9` | ldr x8,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be0f2c"></a> `00be0f2c` | `29 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00be0f30"></a> `00be0f30` | `22 c9 46 f9` | ldr x2,[x9, #0xd90] | `FALL_THROUGH`
<a id="insn-00be0f34"></a> `00be0f34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00be0f38"></a> `00be0f38` | `01 01 41 f9` | ldr x1,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00be0f3c"></a> `00be0f3c` | `3e da e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f40"></a> `00be0f40` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00be0f44"></a> `00be0f44` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0f48"></a> `00be0f48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be0f4c"></a> `00be0f4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00be0f50"></a> `00be0f50` | `6c f3 01 94` | bl 0x00c5dd00 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f54"></a> `00be0f54` | `80 05 00 37` | tbnz w0,#0x0,0x00be1004 | `CONDITIONAL_JUMP`
<a id="insn-00be0f58"></a> `00be0f58` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be0f5c"></a> `00be0f5c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be0f60"></a> `00be0f60` | `a8 e7 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f64"></a> `00be0f64` | `fa 4e 40 f9` | ldr x26,[x23, #0x98] | `FALL_THROUGH`
<a id="insn-00be0f68"></a> `00be0f68` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00be0f6c"></a> `00be0f6c` | `45 e8 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f70"></a> `00be0f70` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00be0f74"></a> `00be0f74` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00be0f78"></a> `00be0f78` | `c6 db 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f7c"></a> `00be0f7c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00be0f80"></a> `00be0f80` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be0f84"></a> `00be0f84` | `9f e7 01 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00be0f88"></a> `00be0f88` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00be0f8c"></a> `00be0f8c` | `88 18 00 10` | adr x8,0xbe129c | `FALL_THROUGH`
<a id="insn-00be0f90"></a> `00be0f90` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00be0f94"></a> `00be0f94` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00be0f98"></a> `00be0f98` | `a8 01 00 37` | tbnz w8,#0x0,0x00be0fcc | `CONDITIONAL_JUMP`
<a id="insn-00be0f9c"></a> `00be0f9c` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00be0fa0"></a> `00be0fa0` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00be0fa4"></a> `00be0fa4` | `0b 00 00 14` | b 0x00be0fd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00be0fa8"></a> `00be0fa8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00be0fac"></a> `00be0fac` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00be0fb0"></a> `00be0fb0` | `30 e7 01 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00be0fb4"></a> `00be0fb4` | `60 c2 00 91` | add x0,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00be0fb8"></a> `00be0fb8` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00be0fbc"></a> `00be0fbc` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00be0fc0"></a> `00be0fc0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00be0fc4"></a> `00be0fc4` | `07 e7 01 94` | bl 0x00c5abe0 | `UNCONDITIONAL_CALL`
<a id="insn-00be0fc8"></a> `00be0fc8` | `15 00 00 14` | b 0x00be101c | `UNCONDITIONAL_JUMP`
<a id="insn-00be0fcc"></a> `00be0fcc` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00be0fd0"></a> `00be0fd0` | `c2 05 00 f0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00be0fd4"></a> `00be0fd4` | `42 0c 45 f9` | ldr x2,[x2, #0xa18] | `FALL_THROUGH`
<a id="insn-00be0fd8"></a> `00be0fd8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00be0fdc"></a> `00be0fdc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00be0fe0"></a> `00be0fe0` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00be0fe4"></a> `00be0fe4` | `d7 e7 01 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00be0fe8"></a> `00be0fe8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00be0fec"></a> `00be0fec` | `a9 e6 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00be0ff0"></a> `00be0ff0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00be0ff4"></a> `00be0ff4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00be0ff8"></a> `00be0ff8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00be0ffc"></a> `00be0ffc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00be1000"></a> `00be1000` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00be1004"></a> `00be1004` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be1008"></a> `00be1008` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00be100c"></a> `00be100c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00be1010"></a> `00be1010` | `70 e7 01 94` | bl 0x00c5add0 | `UNCONDITIONAL_CALL`
<a id="insn-00be1014"></a> `00be1014` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00be1018"></a> `00be1018` | `9e e6 01 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00be101c"></a> `00be101c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00be1020"></a> `00be1020` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00be1024"></a> `00be1024` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00be1028"></a> `00be1028` | `01 01 00 54` | b.ne 0x00be1048 | `CONDITIONAL_JUMP`
<a id="insn-00be102c"></a> `00be102c` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00be1030"></a> `00be1030` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00be1034"></a> `00be1034` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00be1038"></a> `00be1038` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00be103c"></a> `00be103c` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00be1040"></a> `00be1040` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00be1044"></a> `00be1044` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00be1048"></a> `00be1048` | `a6 db 01 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00be0eac`](#insn-00be0eac) 範囲 `[['00be0eac', '00be0edf']]`
  - `CONDITIONAL_JUMP` [`00be0edc`](#insn-00be0edc) → [`00be0fa8`](#insn-00be0fa8)
  - `FALL_THROUGH` [`00be0edc`](#insn-00be0edc) → [`00be0ee0`](#insn-00be0ee0)
- ブロック [`00be0ee0`](#insn-00be0ee0) 範囲 `[['00be0ee0', '00be0ee7']]`
  - `CONDITIONAL_JUMP` [`00be0ee4`](#insn-00be0ee4) → [`00be0fa8`](#insn-00be0fa8)
  - `FALL_THROUGH` [`00be0ee4`](#insn-00be0ee4) → [`00be0ee8`](#insn-00be0ee8)
- ブロック [`00be0ee8`](#insn-00be0ee8) 範囲 `[['00be0ee8', '00be0eef']]`
  - `FALL_THROUGH` [`00be0eec`](#insn-00be0eec) → [`00be0ef0`](#insn-00be0ef0)
- ブロック [`00be0ef0`](#insn-00be0ef0) 範囲 `[['00be0ef0', '00be0f1f']]`
  - `FALL_THROUGH` [`00be0f1c`](#insn-00be0f1c) → [`00be0f20`](#insn-00be0f20)
- ブロック [`00be0f20`](#insn-00be0f20) 範囲 `[['00be0f20', '00be0f2b']]`
  - `FALL_THROUGH` [`00be0f28`](#insn-00be0f28) → [`00be0f2c`](#insn-00be0f2c)
- ブロック [`00be0f2c`](#insn-00be0f2c) 範囲 `[['00be0f2c', '00be0f47']]`
  - `FALL_THROUGH` [`00be0f44`](#insn-00be0f44) → [`00be0f48`](#insn-00be0f48)
- ブロック [`00be0f48`](#insn-00be0f48) 範囲 `[['00be0f48', '00be0f57']]`
  - `CONDITIONAL_JUMP` [`00be0f54`](#insn-00be0f54) → [`00be1004`](#insn-00be1004)
  - `FALL_THROUGH` [`00be0f54`](#insn-00be0f54) → [`00be0f58`](#insn-00be0f58)
- ブロック [`00be0f58`](#insn-00be0f58) 範囲 `[['00be0f58', '00be0f9b']]`
  - `CONDITIONAL_JUMP` [`00be0f98`](#insn-00be0f98) → [`00be0fcc`](#insn-00be0fcc)
  - `FALL_THROUGH` [`00be0f98`](#insn-00be0f98) → [`00be0f9c`](#insn-00be0f9c)
- ブロック [`00be0f9c`](#insn-00be0f9c) 範囲 `[['00be0f9c', '00be0fa7']]`
  - `UNCONDITIONAL_JUMP` [`00be0fa4`](#insn-00be0fa4) → [`00be0fd0`](#insn-00be0fd0)
- ブロック [`00be0fa8`](#insn-00be0fa8) 範囲 `[['00be0fa8', '00be0fcb']]`
  - `UNCONDITIONAL_JUMP` [`00be0fc8`](#insn-00be0fc8) → [`00be101c`](#insn-00be101c)
- ブロック [`00be0fcc`](#insn-00be0fcc) 範囲 `[['00be0fcc', '00be0fcf']]`
  - `FALL_THROUGH` [`00be0fcc`](#insn-00be0fcc) → [`00be0fd0`](#insn-00be0fd0)
- ブロック [`00be0fd0`](#insn-00be0fd0) 範囲 `[['00be0fd0', '00be1003']]`
  - `FALL_THROUGH` [`00be1000`](#insn-00be1000) → [`00be1004`](#insn-00be1004)
- ブロック [`00be1004`](#insn-00be1004) 範囲 `[['00be1004', '00be101b']]`
  - `FALL_THROUGH` [`00be1018`](#insn-00be1018) → [`00be101c`](#insn-00be101c)
- ブロック [`00be101c`](#insn-00be101c) 範囲 `[['00be101c', '00be102b']]`
  - `CONDITIONAL_JUMP` [`00be1028`](#insn-00be1028) → [`00be1048`](#insn-00be1048)
  - `FALL_THROUGH` [`00be1028`](#insn-00be1028) → [`00be102c`](#insn-00be102c)
- ブロック [`00be102c`](#insn-00be102c) 範囲 `[['00be102c', '00be1047']]`
- ブロック [`00be1048`](#insn-00be1048) 範囲 `[['00be1048', '00be104b']]`

## 命令位置別の参照

- [`00be0eb0`](#insn-00be0eb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0eb4`](#insn-00be0eb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0eb8`](#insn-00be0eb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0ebc`](#insn-00be0ebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0ec0`](#insn-00be0ec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0ed4`](#insn-00be0ed4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0edc`](#insn-00be0edc) → [`00be0fa8`](#insn-00be0fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0ee4`](#insn-00be0ee4) → [`00be0fa8`](#insn-00be0fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0f04`](#insn-00be0f04) → [`00c5ae40`](../00c5a/00c5ae40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae40` · 推定シンボル `None` · 推定型 `None`
- [`00be0f10`](#insn-00be0f10) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00be0f18`](#insn-00be0f18) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00be0f24`](#insn-00be0f24) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00be0f30`](#insn-00be0f30) → `01126d90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00be0f3c`](#insn-00be0f3c) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00be0f50`](#insn-00be0f50) → [`00c5dd00`](../00c5d/00c5dd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd00` · 推定シンボル `None` · 推定型 `None`
- [`00be0f54`](#insn-00be0f54) → [`00be1004`](#insn-00be1004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0f60`](#insn-00be0f60) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00be0f6c`](#insn-00be0f6c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00be0f78`](#insn-00be0f78) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00be0f84`](#insn-00be0f84) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00be0f90`](#insn-00be0f90) → [`00be129c`](../00be1/00be129c.md) · `DATA` · `ANALYSIS` · 関数 `00be129c` · 推定シンボル `None` · 推定型 `None`
- [`00be0f98`](#insn-00be0f98) → [`00be0fcc`](#insn-00be0fcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0fa4`](#insn-00be0fa4) → [`00be0fd0`](#insn-00be0fd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0fb0`](#insn-00be0fb0) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00be0fc4`](#insn-00be0fc4) → [`00c5abe0`](../00c5a/00c5abe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5abe0` · 推定シンボル `None` · 推定型 `None`
- [`00be0fc8`](#insn-00be0fc8) → [`00be101c`](#insn-00be101c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be0fd4`](#insn-00be0fd4) → `00c9ba18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00be0fd4`](#insn-00be0fd4) → [`00bd04c0`](../00bd0/00bd04c0.md) · `PARAM` · `ANALYSIS` · 関数 `00bd04c0` · 推定シンボル `_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00be0fe4`](#insn-00be0fe4) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00be0fec`](#insn-00be0fec) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00be1010`](#insn-00be1010) → [`00c5add0`](../00c5a/00c5add0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5add0` · 推定シンボル `None` · 推定型 `None`
- [`00be1018`](#insn-00be1018) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00be1020`](#insn-00be1020) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1028`](#insn-00be1028) → [`00be1048`](#insn-00be1048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be102c`](#insn-00be102c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1030`](#insn-00be1030) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1034`](#insn-00be1034) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1038`](#insn-00be1038) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be103c`](#insn-00be103c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00be1048`](#insn-00be1048) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00be0eb0`](#insn-00be0eb0)

~~~json
{
  "source": "00be0eb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0eb4`](#insn-00be0eb4)

~~~json
{
  "source": "00be0eb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0eb8`](#insn-00be0eb8)

~~~json
{
  "source": "00be0eb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0ebc`](#insn-00be0ebc)

~~~json
{
  "source": "00be0ebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0ec0`](#insn-00be0ec0)

~~~json
{
  "source": "00be0ec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0ed4`](#insn-00be0ed4)

~~~json
{
  "source": "00be0ed4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0edc`](#insn-00be0edc)

~~~json
{
  "source": "00be0edc",
  "target": "00be0fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0ee4`](#insn-00be0ee4)

~~~json
{
  "source": "00be0ee4",
  "target": "00be0fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0f04`](#insn-00be0f04)

~~~json
{
  "source": "00be0f04",
  "target": "00c5ae40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f10`](#insn-00be0f10)

~~~json
{
  "source": "00be0f10",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f18`](#insn-00be0f18)

~~~json
{
  "source": "00be0f18",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f24`](#insn-00be0f24)

~~~json
{
  "source": "00be0f24",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f30`](#insn-00be0f30)

~~~json
{
  "source": "00be0f30",
  "target": "01126d90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d90",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00be0f3c`](#insn-00be0f3c)

~~~json
{
  "source": "00be0f3c",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f50`](#insn-00be0f50)

~~~json
{
  "source": "00be0f50",
  "target": "00c5dd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f54`](#insn-00be0f54)

~~~json
{
  "source": "00be0f54",
  "target": "00be1004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0f60`](#insn-00be0f60)

~~~json
{
  "source": "00be0f60",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f6c`](#insn-00be0f6c)

~~~json
{
  "source": "00be0f6c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f78`](#insn-00be0f78)

~~~json
{
  "source": "00be0f78",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f84`](#insn-00be0f84)

~~~json
{
  "source": "00be0f84",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f90`](#insn-00be0f90)

~~~json
{
  "source": "00be0f90",
  "target": "00be129c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0f98`](#insn-00be0f98)

~~~json
{
  "source": "00be0f98",
  "target": "00be0fcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0fa4`](#insn-00be0fa4)

~~~json
{
  "source": "00be0fa4",
  "target": "00be0fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0fb0`](#insn-00be0fb0)

~~~json
{
  "source": "00be0fb0",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0fc4`](#insn-00be0fc4)

~~~json
{
  "source": "00be0fc4",
  "target": "00c5abe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0fc8`](#insn-00be0fc8)

~~~json
{
  "source": "00be0fc8",
  "target": "00be101c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be0fd4`](#insn-00be0fd4)

~~~json
{
  "source": "00be0fd4",
  "target": "00c9ba18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00be0fd4`](#insn-00be0fd4)

~~~json
{
  "source": "00be0fd4",
  "target": "00bd04c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0fe4`](#insn-00be0fe4)

~~~json
{
  "source": "00be0fe4",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be0fec`](#insn-00be0fec)

~~~json
{
  "source": "00be0fec",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1010`](#insn-00be1010)

~~~json
{
  "source": "00be1010",
  "target": "00c5add0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1018`](#insn-00be1018)

~~~json
{
  "source": "00be1018",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00be1020`](#insn-00be1020)

~~~json
{
  "source": "00be1020",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1028`](#insn-00be1028)

~~~json
{
  "source": "00be1028",
  "target": "00be1048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be102c`](#insn-00be102c)

~~~json
{
  "source": "00be102c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1030`](#insn-00be1030)

~~~json
{
  "source": "00be1030",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1034`](#insn-00be1034)

~~~json
{
  "source": "00be1034",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1038`](#insn-00be1038)

~~~json
{
  "source": "00be1038",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be103c`](#insn-00be103c)

~~~json
{
  "source": "00be103c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00be1048`](#insn-00be1048)

~~~json
{
  "source": "00be1048",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
