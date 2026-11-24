# 00bce4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bce0b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0009.md#compare-52740aeb60187f6d54df91a255c35345)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bce578`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bce/00bce578.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0010.md#compare-bacf2ba9ff95147c6174120d4895b5da)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce4dc",
  "name": "_ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be3f631f9ff131c5fe18efe7a318577dbc351788b4f4163830a29c6090ab0951",
  "source_text_sha256": "be3f631f9ff131c5fe18efe7a318577dbc351788b4f4163830a29c6090ab0951",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce4dc",
        "00bce67f"
      ]
    ],
    "bytes_sha256": "5498a42cb3b9fc1f8b867ed9cf30651eb3ecd2aa4838b94937f28405f9d81798",
    "instruction_count": 105,
    "instruction_bytes": 420,
    "body_bytes": 420,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5dbe0](../00c5d/00c5dbe0.md)
- [00c5dc10](../00c5d/00c5dc10.md)
- [00c5dcf0](../00c5d/00c5dcf0.md)
- [00c5dd50](../00c5d/00c5dd50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2921 bytes

~~~c

void _ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE
               (undefined8 param_1,long *param_2,undefined8 *param_3)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth4UserEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,2);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  if (*(int *)(param_3 + 1) == 0) {
    uVar5 = FUN_00497834(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_011267a0,*param_3);
    uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar4,lVar1,auStack_70);
    if ((uVar6 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar10 = (undefined8 *)*param_2;
      uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
      lVar8 = _Znwm(0x20);
      _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv_00c9ba28
      ;
      *(undefined8 **)(lVar8 + 0x10) = puVar10;
      *(undefined **)(lVar8 + 0x18) = puVar3;
      if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
        lVar9 = (long)puVar10 + 0x141;
      }
      else {
        lVar9 = puVar10[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar7,uVar5,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ba10
                 ,lVar8,lVar9);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
    }
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    lVar8 = (long)param_3 + 0x11;
    if ((*(byte *)(param_3 + 2) & 1) != 0) {
      lVar8 = param_3[4];
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,*(undefined4 *)(param_3 + 1),lVar8,auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
  }
  _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_70);
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) == local_58) {
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
<a id="insn-00bce4dc"></a> `00bce4dc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bce4e0"></a> `00bce4e0` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bce4e4"></a> `00bce4e4` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bce4e8"></a> `00bce4e8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bce4ec"></a> `00bce4ec` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bce4f0"></a> `00bce4f0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bce4f4"></a> `00bce4f4` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bce4f8"></a> `00bce4f8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bce4fc"></a> `00bce4fc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bce500"></a> `00bce500` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bce504"></a> `00bce504` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bce508"></a> `00bce508` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bce50c"></a> `00bce50c` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00bce510"></a> `00bce510` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bce514"></a> `00bce514` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bce518"></a> `00bce518` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bce51c"></a> `00bce51c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce520"></a> `00bce520` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce524"></a> `00bce524` | `bb 3d 02 94` | bl 0x00c5dc10 | `UNCONDITIONAL_CALL`
<a id="insn-00bce528"></a> `00bce528` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bce52c"></a> `00bce52c` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bce530"></a> `00bce530` | `d4 32 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bce534"></a> `00bce534` | `c8 0a 40 b9` | ldr w8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bce538"></a> `00bce538` | `28 02 00 34` | cbz w8,0x00bce57c | `CONDITIONAL_JUMP`
<a id="insn-00bce53c"></a> `00bce53c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bce540"></a> `00bce540` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce544"></a> `00bce544` | `2f 32 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bce548"></a> `00bce548` | `c8 42 40 39` | ldrb w8,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bce54c"></a> `00bce54c` | `c9 12 40 f9` | ldr x9,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00bce550"></a> `00bce550` | `c2 0a 40 b9` | ldr w2,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bce554"></a> `00bce554` | `ca 46 00 91` | add x10,x22,#0x11 | `FALL_THROUGH`
<a id="insn-00bce558"></a> `00bce558` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce55c"></a> `00bce55c` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bce560"></a> `00bce560` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bce564"></a> `00bce564` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bce568"></a> `00bce568` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce56c"></a> `00bce56c` | `9d 3d 02 94` | bl 0x00c5dbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce570"></a> `00bce570` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bce574"></a> `00bce574` | `47 31 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bce578"></a> `00bce578` | `30 00 00 14` | b 0x00bce638 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce57c"></a> `00bce57c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bce580"></a> `00bce580` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bce584"></a> `00bce584` | `22 d1 43 f9` | ldr x2,[x9, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bce588"></a> `00bce588` | `c3 02 40 f9` | ldr x3,[x22] | `FALL_THROUGH`
<a id="insn-00bce58c"></a> `00bce58c` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bce590"></a> `00bce590` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bce594"></a> `00bce594` | `a8 24 e3 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bce598"></a> `00bce598` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bce59c"></a> `00bce59c` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce5a0"></a> `00bce5a0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bce5a4"></a> `00bce5a4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bce5a8"></a> `00bce5a8` | `d2 3d 02 94` | bl 0x00c5dcf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce5ac"></a> `00bce5ac` | `60 04 00 37` | tbnz w0,#0x0,0x00bce638 | `CONDITIONAL_JUMP`
<a id="insn-00bce5b0"></a> `00bce5b0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bce5b4"></a> `00bce5b4` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce5b8"></a> `00bce5b8` | `12 32 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bce5bc"></a> `00bce5bc` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bce5c0"></a> `00bce5c0` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bce5c4"></a> `00bce5c4` | `af 32 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bce5c8"></a> `00bce5c8` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bce5cc"></a> `00bce5cc` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bce5d0"></a> `00bce5d0` | `30 26 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bce5d4"></a> `00bce5d4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bce5d8"></a> `00bce5d8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bce5dc"></a> `00bce5dc` | `09 32 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bce5e0"></a> `00bce5e0` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bce5e4"></a> `00bce5e4` | `08 15 45 f9` | ldr x8,[x8, #0xa28] | `FALL_THROUGH`
<a id="insn-00bce5e8"></a> `00bce5e8` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bce5ec"></a> `00bce5ec` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bce5f0"></a> `00bce5f0` | `88 00 00 37` | tbnz w8,#0x0,0x00bce600 | `CONDITIONAL_JUMP`
<a id="insn-00bce5f4"></a> `00bce5f4` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bce5f8"></a> `00bce5f8` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce5fc"></a> `00bce5fc` | `02 00 00 14` | b 0x00bce604 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce600"></a> `00bce600` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bce604"></a> `00bce604` | `62 06 00 b0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bce608"></a> `00bce608` | `42 08 45 f9` | ldr x2,[x2, #0xa10] | `FALL_THROUGH`
<a id="insn-00bce60c"></a> `00bce60c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bce610"></a> `00bce610` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bce614"></a> `00bce614` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bce618"></a> `00bce618` | `4a 32 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bce61c"></a> `00bce61c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bce620"></a> `00bce620` | `1c 31 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bce624"></a> `00bce624` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bce628"></a> `00bce628` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bce62c"></a> `00bce62c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bce630"></a> `00bce630` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bce634"></a> `00bce634` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce638"></a> `00bce638` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce63c"></a> `00bce63c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce640"></a> `00bce640` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bce644"></a> `00bce644` | `c3 3d 02 94` | bl 0x00c5dd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bce648"></a> `00bce648` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bce64c"></a> `00bce64c` | `11 31 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bce650"></a> `00bce650` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bce654"></a> `00bce654` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bce658"></a> `00bce658` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bce65c"></a> `00bce65c` | `01 01 00 54` | b.ne 0x00bce67c | `CONDITIONAL_JUMP`
<a id="insn-00bce660"></a> `00bce660` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bce664"></a> `00bce664` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bce668"></a> `00bce668` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bce66c"></a> `00bce66c` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bce670"></a> `00bce670` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bce674"></a> `00bce674` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bce678"></a> `00bce678` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce67c"></a> `00bce67c` | `19 26 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bce4dc`](#insn-00bce4dc) 範囲 `[['00bce4dc', '00bce53b']]`
  - `CONDITIONAL_JUMP` [`00bce538`](#insn-00bce538) → [`00bce57c`](#insn-00bce57c)
  - `FALL_THROUGH` [`00bce538`](#insn-00bce538) → [`00bce53c`](#insn-00bce53c)
- ブロック [`00bce53c`](#insn-00bce53c) 範囲 `[['00bce53c', '00bce57b']]`
  - `UNCONDITIONAL_JUMP` [`00bce578`](#insn-00bce578) → [`00bce638`](#insn-00bce638)
- ブロック [`00bce57c`](#insn-00bce57c) 範囲 `[['00bce57c', '00bce5af']]`
  - `CONDITIONAL_JUMP` [`00bce5ac`](#insn-00bce5ac) → [`00bce638`](#insn-00bce638)
  - `FALL_THROUGH` [`00bce5ac`](#insn-00bce5ac) → [`00bce5b0`](#insn-00bce5b0)
- ブロック [`00bce5b0`](#insn-00bce5b0) 範囲 `[['00bce5b0', '00bce5f3']]`
  - `CONDITIONAL_JUMP` [`00bce5f0`](#insn-00bce5f0) → [`00bce600`](#insn-00bce600)
  - `FALL_THROUGH` [`00bce5f0`](#insn-00bce5f0) → [`00bce5f4`](#insn-00bce5f4)
- ブロック [`00bce5f4`](#insn-00bce5f4) 範囲 `[['00bce5f4', '00bce5ff']]`
  - `UNCONDITIONAL_JUMP` [`00bce5fc`](#insn-00bce5fc) → [`00bce604`](#insn-00bce604)
- ブロック [`00bce600`](#insn-00bce600) 範囲 `[['00bce600', '00bce603']]`
  - `FALL_THROUGH` [`00bce600`](#insn-00bce600) → [`00bce604`](#insn-00bce604)
- ブロック [`00bce604`](#insn-00bce604) 範囲 `[['00bce604', '00bce637']]`
  - `FALL_THROUGH` [`00bce634`](#insn-00bce634) → [`00bce638`](#insn-00bce638)
- ブロック [`00bce638`](#insn-00bce638) 範囲 `[['00bce638', '00bce65f']]`
  - `CONDITIONAL_JUMP` [`00bce65c`](#insn-00bce65c) → [`00bce67c`](#insn-00bce67c)
  - `FALL_THROUGH` [`00bce65c`](#insn-00bce65c) → [`00bce660`](#insn-00bce660)
- ブロック [`00bce660`](#insn-00bce660) 範囲 `[['00bce660', '00bce67b']]`
- ブロック [`00bce67c`](#insn-00bce67c) 範囲 `[['00bce67c', '00bce67f']]`

## 命令位置別の参照

- [`00bce4e0`](#insn-00bce4e0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce4e4`](#insn-00bce4e4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce4e8`](#insn-00bce4e8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce4ec`](#insn-00bce4ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce4f0`](#insn-00bce4f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce510`](#insn-00bce510) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce524`](#insn-00bce524) → [`00c5dc10`](../00c5d/00c5dc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dc10` · 推定シンボル `None` · 推定型 `None`
- [`00bce530`](#insn-00bce530) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bce538`](#insn-00bce538) → [`00bce57c`](#insn-00bce57c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce544`](#insn-00bce544) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bce56c`](#insn-00bce56c) → [`00c5dbe0`](../00c5d/00c5dbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbe0` · 推定シンボル `None` · 推定型 `None`
- [`00bce574`](#insn-00bce574) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bce578`](#insn-00bce578) → [`00bce638`](#insn-00bce638) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce584`](#insn-00bce584) → `011267a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce594`](#insn-00bce594) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bce5a8`](#insn-00bce5a8) → [`00c5dcf0`](../00c5d/00c5dcf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcf0` · 推定シンボル `None` · 推定型 `None`
- [`00bce5ac`](#insn-00bce5ac) → [`00bce638`](#insn-00bce638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce5b8`](#insn-00bce5b8) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bce5c4`](#insn-00bce5c4) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bce5d0`](#insn-00bce5d0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bce5dc`](#insn-00bce5dc) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bce5e4`](#insn-00bce5e4) → `00c9ba28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce5e8`](#insn-00bce5e8) → [`00bd4c3c`](../00bd4/00bd4c3c.md) · `DATA` · `ANALYSIS` · 関数 `00bd4c3c` · 推定シンボル `_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv` · 推定型 `None`
- [`00bce5f0`](#insn-00bce5f0) → [`00bce600`](#insn-00bce600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce5fc`](#insn-00bce5fc) → [`00bce604`](#insn-00bce604) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce608`](#insn-00bce608) → `00c9ba10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce608`](#insn-00bce608) → [`00bd010c`](../00bd0/00bd010c.md) · `PARAM` · `ANALYSIS` · 関数 `00bd010c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bce618`](#insn-00bce618) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bce620`](#insn-00bce620) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bce644`](#insn-00bce644) → [`00c5dd50`](../00c5d/00c5dd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd50` · 推定シンボル `None` · 推定型 `None`
- [`00bce64c`](#insn-00bce64c) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bce654`](#insn-00bce654) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce65c`](#insn-00bce65c) → [`00bce67c`](#insn-00bce67c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce660`](#insn-00bce660) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce664`](#insn-00bce664) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce668`](#insn-00bce668) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce66c`](#insn-00bce66c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce670`](#insn-00bce670) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce67c`](#insn-00bce67c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce4e0`](#insn-00bce4e0)

~~~json
{
  "source": "00bce4e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce4e4`](#insn-00bce4e4)

~~~json
{
  "source": "00bce4e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce4e8`](#insn-00bce4e8)

~~~json
{
  "source": "00bce4e8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce4ec`](#insn-00bce4ec)

~~~json
{
  "source": "00bce4ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce4f0`](#insn-00bce4f0)

~~~json
{
  "source": "00bce4f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce510`](#insn-00bce510)

~~~json
{
  "source": "00bce510",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce524`](#insn-00bce524)

~~~json
{
  "source": "00bce524",
  "target": "00c5dc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce530`](#insn-00bce530)

~~~json
{
  "source": "00bce530",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce538`](#insn-00bce538)

~~~json
{
  "source": "00bce538",
  "target": "00bce57c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce544`](#insn-00bce544)

~~~json
{
  "source": "00bce544",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce56c`](#insn-00bce56c)

~~~json
{
  "source": "00bce56c",
  "target": "00c5dbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce574`](#insn-00bce574)

~~~json
{
  "source": "00bce574",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce578`](#insn-00bce578)

~~~json
{
  "source": "00bce578",
  "target": "00bce638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce584`](#insn-00bce584)

~~~json
{
  "source": "00bce584",
  "target": "011267a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce594`](#insn-00bce594)

~~~json
{
  "source": "00bce594",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5a8`](#insn-00bce5a8)

~~~json
{
  "source": "00bce5a8",
  "target": "00c5dcf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5ac`](#insn-00bce5ac)

~~~json
{
  "source": "00bce5ac",
  "target": "00bce638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce5b8`](#insn-00bce5b8)

~~~json
{
  "source": "00bce5b8",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5c4`](#insn-00bce5c4)

~~~json
{
  "source": "00bce5c4",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5d0`](#insn-00bce5d0)

~~~json
{
  "source": "00bce5d0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5dc`](#insn-00bce5dc)

~~~json
{
  "source": "00bce5dc",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5e4`](#insn-00bce5e4)

~~~json
{
  "source": "00bce5e4",
  "target": "00c9ba28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce5e8`](#insn-00bce5e8)

~~~json
{
  "source": "00bce5e8",
  "target": "00bd4c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce5f0`](#insn-00bce5f0)

~~~json
{
  "source": "00bce5f0",
  "target": "00bce600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce5fc`](#insn-00bce5fc)

~~~json
{
  "source": "00bce5fc",
  "target": "00bce604",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce608`](#insn-00bce608)

~~~json
{
  "source": "00bce608",
  "target": "00c9ba10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ba10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce608`](#insn-00bce608)

~~~json
{
  "source": "00bce608",
  "target": "00bd010c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce618`](#insn-00bce618)

~~~json
{
  "source": "00bce618",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce620`](#insn-00bce620)

~~~json
{
  "source": "00bce620",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce644`](#insn-00bce644)

~~~json
{
  "source": "00bce644",
  "target": "00c5dd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce64c`](#insn-00bce64c)

~~~json
{
  "source": "00bce64c",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce654`](#insn-00bce654)

~~~json
{
  "source": "00bce654",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce65c`](#insn-00bce65c)

~~~json
{
  "source": "00bce65c",
  "target": "00bce67c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce660`](#insn-00bce660)

~~~json
{
  "source": "00bce660",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce664`](#insn-00bce664)

~~~json
{
  "source": "00bce664",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce668`](#insn-00bce668)

~~~json
{
  "source": "00bce668",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce66c`](#insn-00bce66c)

~~~json
{
  "source": "00bce66c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce670`](#insn-00bce670)

~~~json
{
  "source": "00bce670",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce67c`](#insn-00bce67c)

~~~json
{
  "source": "00bce67c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
