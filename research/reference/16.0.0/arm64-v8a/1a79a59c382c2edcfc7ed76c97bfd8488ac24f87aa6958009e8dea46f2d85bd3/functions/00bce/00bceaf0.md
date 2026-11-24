# 00bceaf0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5f5f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-30e6b3df9c54cccb8ae9d27e56d4d7e0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcef18`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bcef18.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-9a05831e70b75c7c93c6d4273d973e92)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceaf0",
  "name": "_ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_",
  "size": 568,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aac1f46478a7e5cb1e905f325b32ec7e15dc4abe8edd0e7c2111df45e91e5d63",
  "source_text_sha256": "aac1f46478a7e5cb1e905f325b32ec7e15dc4abe8edd0e7c2111df45e91e5d63",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceaf0",
        "00bced27"
      ]
    ],
    "bytes_sha256": "6e5a301c53acbe7a7ec2d5f8663f0c3288253e8b072721fb51a8453253640dbf",
    "instruction_count": 142,
    "instruction_bytes": 568,
    "body_bytes": 568,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57be0](../00c57/00c57be0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d7c0](../00c5d/00c5d7c0.md)
- [00c5d800](../00c5d/00c5d800.md)
- [00c5d8d0](../00c5d/00c5d8d0.md)
- [00c5d930](../00c5d/00c5d930.md)

## 関連文字列（未確認候補）

~~~text
"Empty email or password are not allowed."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4129 bytes

~~~c

void _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_
               (undefined8 param_1,long *param_2,char *param_3,char *param_4)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  size_t sVar4;
  long *plVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uVar9;
  long lVar10;
  long lVar11;
  undefined4 uVar12;
  undefined8 *puVar13;
  undefined1 auStack_90 [16];
  undefined1 auStack_80 [16];
  undefined1 auStack_70 [16];
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_70,lVar1,7);
  if ((((param_3 == (char *)0x0) || (sVar4 = strlen(param_3), param_4 == (char *)0x0)) ||
      (sVar4 == 0)) || (sVar4 = strlen(param_4), sVar4 == 0)) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_80,auStack_70);
    uVar12 = 0x25;
    if (param_3 != (char *)0x0) {
      sVar4 = strlen(param_3);
      uVar12 = 0x25;
      if (sVar4 != 0) {
        uVar12 = 0x26;
      }
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (lVar1,auStack_80,uVar12,"Empty email or password are not allowed.",auStack_60);
    _ZN8firebase12FutureHandleD2Ev(auStack_80);
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  else {
    plVar5 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
    uVar6 = (**(code **)(*plVar5 + 0x538))(plVar5,param_3);
    uVar7 = (**(code **)(*plVar5 + 0x538))(plVar5,param_4);
    uVar8 = FUN_004977f4(plVar5,*(undefined8 *)(*param_2 + 0x1f8),DAT_011263b8,uVar6,uVar7);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar6);
    (**(code **)(*plVar5 + 0xb8))(plVar5,uVar7);
                    /* try { // try from 00bcebe8 to 00ccebef has its CatchHandler @ 00bcebf0 */
                    /* catch() { ... } // from try @ 00bcebe8 with catch @ 00bcebf0
                       try { // try from 00bcebf0 to 00ccec23 has its CatchHandler @ 00bcea58 */
    uVar9 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                      (plVar5,lVar1,auStack_70);
    if ((uVar9 & 1) == 0) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,auStack_70);
      puVar13 = (undefined8 *)*param_2;
      uVar6 = _ZNK8firebase3App9GetJNIEnvEv(*puVar13);
      lVar10 = _Znwm(0x20);
                    /* try { // try from 00bcec24 to 00ccef7b has its CatchHandler @ 00bcec24
                       catch() { ... } // from try @ 00bcec24 with catch @ 00bcec24
                       catch() { ... } // from try @ 00bcef84 with catch @ 00bcec24 */
      _ZN8firebase12FutureHandleC1ERKS0_(lVar10,auStack_90);
      puVar3 = 
      PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9b620
      ;
      *(undefined8 **)(lVar10 + 0x10) = puVar13;
      *(undefined **)(lVar10 + 0x18) = puVar3;
      if ((*(byte *)(puVar13 + 0x28) & 1) == 0) {
        lVar11 = (long)puVar13 + 0x141;
      }
      else {
        lVar11 = puVar13[0x2a];
      }
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (uVar6,uVar8,
                 PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b600
                 ,lVar10,lVar11);
      _ZN8firebase12FutureHandleD2Ev(auStack_90);
      (**(code **)(*plVar5 + 0xb8))(plVar5,uVar8);
    }
    _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
              (param_1,lVar1,auStack_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_70);
  if (*(long *)(lVar2 + 0x28) != local_58) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceaf0"></a> `00bceaf0` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bceaf4"></a> `00bceaf4` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bceaf8"></a> `00bceaf8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bceafc"></a> `00bceafc` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bceb00"></a> `00bceb00` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bceb04"></a> `00bceb04` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bceb08"></a> `00bceb08` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bceb0c"></a> `00bceb0c` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bceb10"></a> `00bceb10` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bceb14"></a> `00bceb14` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bceb18"></a> `00bceb18` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bceb1c"></a> `00bceb1c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bceb20"></a> `00bceb20` | `e1 00 80 52` | mov w1,#0x7 | `FALL_THROUGH`
<a id="insn-00bceb24"></a> `00bceb24` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bceb28"></a> `00bceb28` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceb2c"></a> `00bceb2c` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bceb30"></a> `00bceb30` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bceb34"></a> `00bceb34` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bceb38"></a> `00bceb38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bceb3c"></a> `00bceb3c` | `31 3b 02 94` | bl 0x00c5d800 | `UNCONDITIONAL_CALL`
<a id="insn-00bceb40"></a> `00bceb40` | `77 08 00 b4` | cbz x23,0x00bcec4c | `CONDITIONAL_JUMP`
<a id="insn-00bceb44"></a> `00bceb44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bceb48"></a> `00bceb48` | `26 24 02 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceb4c"></a> `00bceb4c` | `18 08 00 b4` | cbz x24,0x00bcec4c | `CONDITIONAL_JUMP`
<a id="insn-00bceb50"></a> `00bceb50` | `e0 07 00 b4` | cbz x0,0x00bcec4c | `CONDITIONAL_JUMP`
<a id="insn-00bceb54"></a> `00bceb54` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bceb58"></a> `00bceb58` | `22 24 02 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-00bceb5c"></a> `00bceb5c` | `80 07 00 b4` | cbz x0,0x00bcec4c | `CONDITIONAL_JUMP`
<a id="insn-00bceb60"></a> `00bceb60` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bceb64"></a> `00bceb64` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bceb68"></a> `00bceb68` | `46 30 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bceb6c"></a> `00bceb6c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bceb70"></a> `00bceb70` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bceb74"></a> `00bceb74` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bceb78"></a> `00bceb78` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bceb7c"></a> `00bceb7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceb80"></a> `00bceb80` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bceb84"></a> `00bceb84` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bceb88"></a> `00bceb88` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bceb8c"></a> `00bceb8c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bceb90"></a> `00bceb90` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bceb94"></a> `00bceb94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceb98"></a> `00bceb98` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bceb9c"></a> `00bceb9c` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bceba0"></a> `00bceba0` | `22 dd 41 f9` | ldr x2,[x9, #0x3b8] | `FALL_THROUGH`
<a id="insn-00bceba4"></a> `00bceba4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bceba8"></a> `00bceba8` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcebac"></a> `00bcebac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcebb0"></a> `00bcebb0` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bcebb4"></a> `00bcebb4` | `e4 03 18 aa` | mov x4,x24 | `FALL_THROUGH`
<a id="insn-00bcebb8"></a> `00bcebb8` | `0f 23 e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcebbc"></a> `00bcebbc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcebc0"></a> `00bcebc0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcebc4"></a> `00bcebc4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcebc8"></a> `00bcebc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcebcc"></a> `00bcebcc` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bcebd0"></a> `00bcebd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcebd4"></a> `00bcebd4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcebd8"></a> `00bcebd8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcebdc"></a> `00bcebdc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcebe0"></a> `00bcebe0` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcebe4"></a> `00bcebe4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcebe8"></a> `00bcebe8` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcebec"></a> `00bcebec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcebf0"></a> `00bcebf0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcebf4"></a> `00bcebf4` | `37 3b 02 94` | bl 0x00c5d8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcebf8"></a> `00bcebf8` | `c0 08 00 37` | tbnz w0,#0x0,0x00bced10 | `CONDITIONAL_JUMP`
<a id="insn-00bcebfc"></a> `00bcebfc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcec00"></a> `00bcec00` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcec04"></a> `00bcec04` | `7f 2f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec08"></a> `00bcec08` | `d9 02 40 f9` | ldr x25,[x22] | `FALL_THROUGH`
<a id="insn-00bcec0c"></a> `00bcec0c` | `20 03 40 f9` | ldr x0,[x25] | `FALL_THROUGH`
<a id="insn-00bcec10"></a> `00bcec10` | `1c 30 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec14"></a> `00bcec14` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcec18"></a> `00bcec18` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcec1c"></a> `00bcec1c` | `9d 23 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec20"></a> `00bcec20` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcec24"></a> `00bcec24` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bcec28"></a> `00bcec28` | `76 2f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec2c"></a> `00bcec2c` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcec30"></a> `00bcec30` | `08 11 43 f9` | ldr x8,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-00bcec34"></a> `00bcec34` | `19 23 01 a9` | stp x25,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec38"></a> `00bcec38` | `28 03 45 39` | ldrb w8,[x25, #0x140] | `FALL_THROUGH`
<a id="insn-00bcec3c"></a> `00bcec3c` | `e8 04 00 37` | tbnz w8,#0x0,0x00bcecd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcec40"></a> `00bcec40` | `28 03 05 91` | add x8,x25,#0x140 | `FALL_THROUGH`
<a id="insn-00bcec44"></a> `00bcec44` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec48"></a> `00bcec48` | `25 00 00 14` | b 0x00bcecdc | `UNCONDITIONAL_JUMP`
<a id="insn-00bcec4c"></a> `00bcec4c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcec50"></a> `00bcec50` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcec54"></a> `00bcec54` | `6b 2f 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec58"></a> `00bcec58` | `b5 04 80 52` | mov w21,#0x25 | `FALL_THROUGH`
<a id="insn-00bcec5c"></a> `00bcec5c` | `b7 00 00 b4` | cbz x23,0x00bcec70 | `CONDITIONAL_JUMP`
<a id="insn-00bcec60"></a> `00bcec60` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcec64"></a> `00bcec64` | `df 23 02 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec68"></a> `00bcec68` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bcec6c"></a> `00bcec6c` | `b5 06 95 1a` | cinc w21,w21,ne | `FALL_THROUGH`
<a id="insn-00bcec70"></a> `00bcec70` | `e3 b6 ff d0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcec74"></a> `00bcec74` | `63 f4 08 91` | add x3,x3,#0x23d | `FALL_THROUGH`
<a id="insn-00bcec78"></a> `00bcec78` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcec7c"></a> `00bcec7c` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcec80"></a> `00bcec80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcec84"></a> `00bcec84` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bcec88"></a> `00bcec88` | `ce 3a 02 94` | bl 0x00c5d7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec8c"></a> `00bcec8c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcec90"></a> `00bcec90` | `80 2e 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec94"></a> `00bcec94` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcec98"></a> `00bcec98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcec9c"></a> `00bcec9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bceca0"></a> `00bceca0` | `24 3b 02 94` | bl 0x00c5d930 | `UNCONDITIONAL_CALL`
<a id="insn-00bceca4"></a> `00bceca4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bceca8"></a> `00bceca8` | `7a 2e 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecac"></a> `00bcecac` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcecb8"></a> `00bcecb8` | `61 03 00 54` | b.ne 0x00bced24 | `CONDITIONAL_JUMP`
<a id="insn-00bcecbc"></a> `00bcecbc` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bcecc0"></a> `00bcecc0` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcecc8"></a> `00bcecc8` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bceccc"></a> `00bceccc` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcecd0"></a> `00bcecd0` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcecd8"></a> `00bcecd8` | `24 ab 40 f9` | ldr x4,[x25, #0x150] | `FALL_THROUGH`
<a id="insn-00bcecdc"></a> `00bcecdc` | `62 06 00 b0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcece0"></a> `00bcece0` | `42 00 43 f9` | ldr x2,[x2, #0x600] | `FALL_THROUGH`
<a id="insn-00bcece4"></a> `00bcece4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bcece8"></a> `00bcece8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bcecec"></a> `00bcecec` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcecf0"></a> `00bcecf0` | `94 2f 02 94` | bl 0x00c5ab40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecf4"></a> `00bcecf4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bcecf8"></a> `00bcecf8` | `66 2e 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecfc"></a> `00bcecfc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bced00"></a> `00bced00` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bced04"></a> `00bced04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bced08"></a> `00bced08` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bced0c"></a> `00bced0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bced10"></a> `00bced10` | `e2 83 00 91` | add x2,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bced14"></a> `00bced14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bced18"></a> `00bced18` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bced1c"></a> `00bced1c` | `05 3b 02 94` | bl 0x00c5d930 | `UNCONDITIONAL_CALL`
<a id="insn-00bced20"></a> `00bced20` | `e1 ff ff 17` | b 0x00bceca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bced24"></a> `00bced24` | `6f 23 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceaf0`](#insn-00bceaf0) 範囲 `[['00bceaf0', '00bceb43']]`
  - `CONDITIONAL_JUMP` [`00bceb40`](#insn-00bceb40) → [`00bcec4c`](#insn-00bcec4c)
  - `FALL_THROUGH` [`00bceb40`](#insn-00bceb40) → [`00bceb44`](#insn-00bceb44)
- ブロック [`00bceb44`](#insn-00bceb44) 範囲 `[['00bceb44', '00bceb4f']]`
  - `CONDITIONAL_JUMP` [`00bceb4c`](#insn-00bceb4c) → [`00bcec4c`](#insn-00bcec4c)
  - `FALL_THROUGH` [`00bceb4c`](#insn-00bceb4c) → [`00bceb50`](#insn-00bceb50)
- ブロック [`00bceb50`](#insn-00bceb50) 範囲 `[['00bceb50', '00bceb53']]`
  - `CONDITIONAL_JUMP` [`00bceb50`](#insn-00bceb50) → [`00bcec4c`](#insn-00bcec4c)
  - `FALL_THROUGH` [`00bceb50`](#insn-00bceb50) → [`00bceb54`](#insn-00bceb54)
- ブロック [`00bceb54`](#insn-00bceb54) 範囲 `[['00bceb54', '00bceb5f']]`
  - `CONDITIONAL_JUMP` [`00bceb5c`](#insn-00bceb5c) → [`00bcec4c`](#insn-00bcec4c)
  - `FALL_THROUGH` [`00bceb5c`](#insn-00bceb5c) → [`00bceb60`](#insn-00bceb60)
- ブロック [`00bceb60`](#insn-00bceb60) 範囲 `[['00bceb60', '00bcebe7']]`
  - `FALL_THROUGH` [`00bcebe4`](#insn-00bcebe4) → [`00bcebe8`](#insn-00bcebe8)
- ブロック [`00bcebe8`](#insn-00bcebe8) 範囲 `[['00bcebe8', '00bcebef']]`
  - `FALL_THROUGH` [`00bcebec`](#insn-00bcebec) → [`00bcebf0`](#insn-00bcebf0)
- ブロック [`00bcebf0`](#insn-00bcebf0) 範囲 `[['00bcebf0', '00bcebfb']]`
  - `CONDITIONAL_JUMP` [`00bcebf8`](#insn-00bcebf8) → [`00bced10`](#insn-00bced10)
  - `FALL_THROUGH` [`00bcebf8`](#insn-00bcebf8) → [`00bcebfc`](#insn-00bcebfc)
- ブロック [`00bcebfc`](#insn-00bcebfc) 範囲 `[['00bcebfc', '00bcec23']]`
  - `FALL_THROUGH` [`00bcec20`](#insn-00bcec20) → [`00bcec24`](#insn-00bcec24)
- ブロック [`00bcec24`](#insn-00bcec24) 範囲 `[['00bcec24', '00bcec3f']]`
  - `CONDITIONAL_JUMP` [`00bcec3c`](#insn-00bcec3c) → [`00bcecd8`](#insn-00bcecd8)
  - `FALL_THROUGH` [`00bcec3c`](#insn-00bcec3c) → [`00bcec40`](#insn-00bcec40)
- ブロック [`00bcec40`](#insn-00bcec40) 範囲 `[['00bcec40', '00bcec4b']]`
  - `UNCONDITIONAL_JUMP` [`00bcec48`](#insn-00bcec48) → [`00bcecdc`](#insn-00bcecdc)
- ブロック [`00bcec4c`](#insn-00bcec4c) 範囲 `[['00bcec4c', '00bcec5f']]`
  - `CONDITIONAL_JUMP` [`00bcec5c`](#insn-00bcec5c) → [`00bcec70`](#insn-00bcec70)
  - `FALL_THROUGH` [`00bcec5c`](#insn-00bcec5c) → [`00bcec60`](#insn-00bcec60)
- ブロック [`00bcec60`](#insn-00bcec60) 範囲 `[['00bcec60', '00bcec6f']]`
  - `FALL_THROUGH` [`00bcec6c`](#insn-00bcec6c) → [`00bcec70`](#insn-00bcec70)
- ブロック [`00bcec70`](#insn-00bcec70) 範囲 `[['00bcec70', '00bceca3']]`
  - `FALL_THROUGH` [`00bceca0`](#insn-00bceca0) → [`00bceca4`](#insn-00bceca4)
- ブロック [`00bceca4`](#insn-00bceca4) 範囲 `[['00bceca4', '00bcecbb']]`
  - `CONDITIONAL_JUMP` [`00bcecb8`](#insn-00bcecb8) → [`00bced24`](#insn-00bced24)
  - `FALL_THROUGH` [`00bcecb8`](#insn-00bcecb8) → [`00bcecbc`](#insn-00bcecbc)
- ブロック [`00bcecbc`](#insn-00bcecbc) 範囲 `[['00bcecbc', '00bcecd7']]`
- ブロック [`00bcecd8`](#insn-00bcecd8) 範囲 `[['00bcecd8', '00bcecdb']]`
  - `FALL_THROUGH` [`00bcecd8`](#insn-00bcecd8) → [`00bcecdc`](#insn-00bcecdc)
- ブロック [`00bcecdc`](#insn-00bcecdc) 範囲 `[['00bcecdc', '00bced0f']]`
  - `FALL_THROUGH` [`00bced0c`](#insn-00bced0c) → [`00bced10`](#insn-00bced10)
- ブロック [`00bced10`](#insn-00bced10) 範囲 `[['00bced10', '00bced23']]`
  - `UNCONDITIONAL_JUMP` [`00bced20`](#insn-00bced20) → [`00bceca4`](#insn-00bceca4)
- ブロック [`00bced24`](#insn-00bced24) 範囲 `[['00bced24', '00bced27']]`

## 命令位置別の参照

- [`00bceaf4`](#insn-00bceaf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceaf8`](#insn-00bceaf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceafc`](#insn-00bceafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb00`](#insn-00bceb00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb04`](#insn-00bceb04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb24`](#insn-00bceb24) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb3c`](#insn-00bceb3c) → [`00c5d800`](../00c5d/00c5d800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d800` · 推定シンボル `None` · 推定型 `None`
- [`00bceb40`](#insn-00bceb40) → [`00bcec4c`](#insn-00bcec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb48`](#insn-00bceb48) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`00bceb4c`](#insn-00bceb4c) → [`00bcec4c`](#insn-00bcec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb50`](#insn-00bceb50) → [`00bcec4c`](#insn-00bcec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb58`](#insn-00bceb58) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`00bceb5c`](#insn-00bceb5c) → [`00bcec4c`](#insn-00bcec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceb68`](#insn-00bceb68) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bceba0`](#insn-00bceba0) → `011263b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcebb8`](#insn-00bcebb8) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bcebf4`](#insn-00bcebf4) → [`00c5d8d0`](../00c5d/00c5d8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d8d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcebf8`](#insn-00bcebf8) → [`00bced10`](#insn-00bced10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec04`](#insn-00bcec04) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcec10`](#insn-00bcec10) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcec1c`](#insn-00bcec1c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcec28`](#insn-00bcec28) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcec30`](#insn-00bcec30) → `00c9b620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcec34`](#insn-00bcec34) → [`00bd4404`](../00bd4/00bd4404.md) · `DATA` · `ANALYSIS` · 関数 `00bd4404` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcec3c`](#insn-00bcec3c) → [`00bcecd8`](#insn-00bcecd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec48`](#insn-00bcec48) → [`00bcecdc`](#insn-00bcecdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec54`](#insn-00bcec54) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcec5c`](#insn-00bcec5c) → [`00bcec70`](#insn-00bcec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec64`](#insn-00bcec64) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec74`](#insn-00bcec74) → `002ac23d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcec88`](#insn-00bcec88) → [`00c5d7c0`](../00c5d/00c5d7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec90`](#insn-00bcec90) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bceca0`](#insn-00bceca0) → [`00c5d930`](../00c5d/00c5d930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d930` · 推定シンボル `None` · 推定型 `None`
- [`00bceca8`](#insn-00bceca8) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb0`](#insn-00bcecb0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb8`](#insn-00bcecb8) → [`00bced24`](#insn-00bced24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecbc`](#insn-00bcecbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc0`](#insn-00bcecc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc4`](#insn-00bcecc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc8`](#insn-00bcecc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceccc`](#insn-00bceccc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcece0`](#insn-00bcece0) → `00c9b600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcece0`](#insn-00bcece0) → [`00bcf91c`](../00bcf/00bcf91c.md) · `PARAM` · `ANALYSIS` · 関数 `00bcf91c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcecf0`](#insn-00bcecf0) → [`00c5ab40`](../00c5a/00c5ab40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab40` · 推定シンボル `None` · 推定型 `None`
- [`00bcecf8`](#insn-00bcecf8) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bced1c`](#insn-00bced1c) → [`00c5d930`](../00c5d/00c5d930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d930` · 推定シンボル `None` · 推定型 `None`
- [`00bced20`](#insn-00bced20) → [`00bceca4`](#insn-00bceca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bced24`](#insn-00bced24) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bceaf4`](#insn-00bceaf4)

~~~json
{
  "source": "00bceaf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceaf8`](#insn-00bceaf8)

~~~json
{
  "source": "00bceaf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceafc`](#insn-00bceafc)

~~~json
{
  "source": "00bceafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb00`](#insn-00bceb00)

~~~json
{
  "source": "00bceb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb04`](#insn-00bceb04)

~~~json
{
  "source": "00bceb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb24`](#insn-00bceb24)

~~~json
{
  "source": "00bceb24",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb3c`](#insn-00bceb3c)

~~~json
{
  "source": "00bceb3c",
  "target": "00c5d800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceb40`](#insn-00bceb40)

~~~json
{
  "source": "00bceb40",
  "target": "00bcec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb48`](#insn-00bceb48)

~~~json
{
  "source": "00bceb48",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceb4c`](#insn-00bceb4c)

~~~json
{
  "source": "00bceb4c",
  "target": "00bcec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb50`](#insn-00bceb50)

~~~json
{
  "source": "00bceb50",
  "target": "00bcec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb58`](#insn-00bceb58)

~~~json
{
  "source": "00bceb58",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceb5c`](#insn-00bceb5c)

~~~json
{
  "source": "00bceb5c",
  "target": "00bcec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceb68`](#insn-00bceb68)

~~~json
{
  "source": "00bceb68",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceba0`](#insn-00bceba0)

~~~json
{
  "source": "00bceba0",
  "target": "011263b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcebb8`](#insn-00bcebb8)

~~~json
{
  "source": "00bcebb8",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcebf4`](#insn-00bcebf4)

~~~json
{
  "source": "00bcebf4",
  "target": "00c5d8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcebf8`](#insn-00bcebf8)

~~~json
{
  "source": "00bcebf8",
  "target": "00bced10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec04`](#insn-00bcec04)

~~~json
{
  "source": "00bcec04",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec10`](#insn-00bcec10)

~~~json
{
  "source": "00bcec10",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec1c`](#insn-00bcec1c)

~~~json
{
  "source": "00bcec1c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec28`](#insn-00bcec28)

~~~json
{
  "source": "00bcec28",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec30`](#insn-00bcec30)

~~~json
{
  "source": "00bcec30",
  "target": "00c9b620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcec34`](#insn-00bcec34)

~~~json
{
  "source": "00bcec34",
  "target": "00bd4404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec3c`](#insn-00bcec3c)

~~~json
{
  "source": "00bcec3c",
  "target": "00bcecd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec48`](#insn-00bcec48)

~~~json
{
  "source": "00bcec48",
  "target": "00bcecdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec54`](#insn-00bcec54)

~~~json
{
  "source": "00bcec54",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec5c`](#insn-00bcec5c)

~~~json
{
  "source": "00bcec5c",
  "target": "00bcec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec64`](#insn-00bcec64)

~~~json
{
  "source": "00bcec64",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec74`](#insn-00bcec74)

~~~json
{
  "source": "00bcec74",
  "target": "002ac23d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac23d",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "456d70747920656d61696c206f722070617373776f726420617265206e6f7420",
  "capture_start": "002ac23d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcec88`](#insn-00bcec88)

~~~json
{
  "source": "00bcec88",
  "target": "00c5d7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec90`](#insn-00bcec90)

~~~json
{
  "source": "00bcec90",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceca0`](#insn-00bceca0)

~~~json
{
  "source": "00bceca0",
  "target": "00c5d930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bceca8`](#insn-00bceca8)

~~~json
{
  "source": "00bceca8",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecb0`](#insn-00bcecb0)

~~~json
{
  "source": "00bcecb0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecb8`](#insn-00bcecb8)

~~~json
{
  "source": "00bcecb8",
  "target": "00bced24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecbc`](#insn-00bcecbc)

~~~json
{
  "source": "00bcecbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc0`](#insn-00bcecc0)

~~~json
{
  "source": "00bcecc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc4`](#insn-00bcecc4)

~~~json
{
  "source": "00bcecc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecc8`](#insn-00bcecc8)

~~~json
{
  "source": "00bcecc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceccc`](#insn-00bceccc)

~~~json
{
  "source": "00bceccc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcece0`](#insn-00bcece0)

~~~json
{
  "source": "00bcece0",
  "target": "00c9b600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b600",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcece0`](#insn-00bcece0)

~~~json
{
  "source": "00bcece0",
  "target": "00bcf91c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecf0`](#insn-00bcecf0)

~~~json
{
  "source": "00bcecf0",
  "target": "00c5ab40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecf8`](#insn-00bcecf8)

~~~json
{
  "source": "00bcecf8",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced1c`](#insn-00bced1c)

~~~json
{
  "source": "00bced1c",
  "target": "00c5d930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bced20`](#insn-00bced20)

~~~json
{
  "source": "00bced20",
  "target": "00bceca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bced24`](#insn-00bced24)

~~~json
{
  "source": "00bced24",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
