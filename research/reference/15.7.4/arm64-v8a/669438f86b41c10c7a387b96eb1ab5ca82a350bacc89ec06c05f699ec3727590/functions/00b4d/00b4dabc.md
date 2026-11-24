# 00b4dabc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4da78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0068.md#compare-57048c2fc68e4ae2cd83f058ef4925df)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbb818`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbb/00bbb818.md) · 移動量 `+0x6dd5c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-9e17f0b206c5c7b941eb4756ff26a9e1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4dabc",
  "name": "FUN_00b4dabc",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bdd87f7f791b260509162e2a94dd934b4d82b12003acabf9150fc28886b8c4b",
  "source_text_sha256": "0bdd87f7f791b260509162e2a94dd934b4d82b12003acabf9150fc28886b8c4b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4dabc",
        "00b4dc77"
      ]
    ],
    "bytes_sha256": "1599daf0b14cd4ec40a49d9cded709c13c4b029941a335cdb4333d04ae92748d",
    "instruction_count": 111,
    "instruction_bytes": 444,
    "body_bytes": 444,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00b4d7ec](../00b4d/00b4d7ec.md)
- [00b4e948](../00b4e/00b4e948.md)

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc40](../00bdd/00bddc40.md)
- [00bddf80](../00bdd/00bddf80.md)
- [00bde0c0](../00bde/00bde0c0.md)
- [00bde0d0](../00bde/00bde0d0.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde2b0](../00bde/00bde2b0.md)
- [00bdee00](../00bde/00bdee00.md)
- [00be0300](../00be0/00be0300.md)

## 関連文字列（未確認候補）

~~~text
"Messaging"
"Unsubscribe from topic %s"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4795 bytes

~~~c

void FUN_00b4dabc(undefined8 param_1,undefined8 param_2)

{
  void *pvVar1;
  long lVar2;
  char cVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  undefined8 uVar7;
  undefined1 auStack_78 [16];
  byte local_68 [16];
  void *local_58;
  undefined1 auStack_50 [8];
  long local_48;
  
                    /* catch() { ... } // from try @ 00b4cd4c with catch @ 00b4dabc */
                    /* catch() { ... } // from try @ 00b4cd2c with catch @ 00b4dac0 */
                    /* catch() { ... } // from try @ 00b4ca44 with catch @ 00b4dad0 */
                    /* catch() { ... } // from try @ 00b4ca24 with catch @ 00b4dad4 */
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00b4c068 with catch @ 00b4dae4 */
                    /* catch() { ... } // from try @ 00b4c048 with catch @ 00b4dae8 */
  _ZN8firebase8LogDebugEPKcz("Unsubscribe from topic %s",param_1);
                    /* catch() { ... } // from try @ 00b4bd50 with catch @ 00b4daf8 */
                    /* catch() { ... } // from try @ 00b4bd30 with catch @ 00b4dafc */
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(DAT_010a10a0);
                    /* catch() { ... } // from try @ 00b4cd0c with catch @ 00b4db0c */
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_1);
                    /* catch() { ... } // from try @ 00b4ccf8 with catch @ 00b4db2c */
                    /* catch() { ... } // from try @ 00b4ca04 with catch @ 00b4db30 */
  lVar6 = FUN_0047495c(plVar4,DAT_010a10d8,DAT_010a1020,uVar5);
  cVar3 = (**(code **)(*plVar4 + 0x720))(plVar4);
                    /* catch() { ... } // from try @ 00b4c9f0 with catch @ 00b4db50 */
  if (cVar3 == '\0') {
    if (lVar6 != 0) {
      uVar7 = _Znwm(0x10);
      _ZN8firebase12FutureHandleC1ERKS0_(uVar7,param_2);
      _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
                (plVar4,lVar6,FUN_00b4eb58,uVar7,"Messaging");
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
                    /* catch() { ... } // from try @ 00b4d3c0 with catch @ 00b4dc24 */
                    /* catch() { ... } // from try @ 00b4d028 with catch @ 00b4dc28 */
      (**(code **)(*plVar4 + 0xb8))(plVar4,lVar6);
    }
  }
  else {
                    /* catch() { ... } // from try @ 00b4c028 with catch @ 00b4db54 */
    uVar7 = (**(code **)(*plVar4 + 0x78))(plVar4);
                    /* catch() { ... } // from try @ 00b4c014 with catch @ 00b4db74 */
    (**(code **)(*plVar4 + 0x88))(plVar4);
                    /* catch() { ... } // from try @ 00b4bd10 with catch @ 00b4db78 */
    _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject(local_68,plVar4,uVar7);
    uVar7 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* catch() { ... } // from try @ 00b4bcfc with catch @ 00b4db98 */
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,param_2);
                    /* catch() { ... } // from try @ 00b4ccd4 with catch @ 00b4db9c */
                    /* catch() { ... } // from try @ 00b4c9cc with catch @ 00b4dba0 */
                    /* catch() { ... } // from try @ 00b4c92c with catch @ 00b4dba4 */
                    /* catch() { ... } // from try @ 00b4c8a4 with catch @ 00b4dba8 */
    pvVar1 = (void *)((ulong)local_68 | 1);
                    /* catch() { ... } // from try @ 00b4bff0 with catch @ 00b4dbb0 */
    if ((local_68[0] & 1) != 0) {
      pvVar1 = local_58;
    }
                    /* catch() { ... } // from try @ 00b4bcd8 with catch @ 00b4dbb4 */
                    /* catch() { ... } // from try @ 00b4d66c with catch @ 00b4dbb8 */
                    /* catch() { ... } // from try @ 00b4d2c8 with catch @ 00b4dbbc */
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (uVar7,auStack_78,2,pvVar1,auStack_50);
    _ZN8firebase12FutureHandleD1Ev(auStack_78);
    if ((local_68[0] & 1) != 0) {
      _ZdlPv(local_58);
    }
  }
                    /* catch() { ... } // from try @ 00b4cf30 with catch @ 00b4dc3c */
                    /* catch() { ... } // from try @ 00b4cc24 with catch @ 00b4dc40 */
                    /* catch() { ... } // from try @ 00b4c244 with catch @ 00b4dc44 */
                    /* catch() { ... } // from try @ 00b4bf2c with catch @ 00b4dc48 */
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  if (*(long *)(lVar2 + 0x28) == local_48) {
                    /* catch() { ... } // from try @ 00b4c4b0 with catch @ 00b4dc64 */
                    /* catch() { ... } // from try @ 00b4c490 with catch @ 00b4dc68 */
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
<a id="insn-00b4dabc"></a> `00b4dabc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b4dac0"></a> `00b4dac0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4dac4"></a> `00b4dac4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4dac8"></a> `00b4dac8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4dacc"></a> `00b4dacc` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4dad0"></a> `00b4dad0` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b4dad4"></a> `00b4dad4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b4dad8"></a> `00b4dad8` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dadc"></a> `00b4dadc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b4dae0"></a> `00b4dae0` | `00 bb ff d0` | adrp x0,0x2af000 | `FALL_THROUGH`
<a id="insn-00b4dae4"></a> `00b4dae4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b4dae8"></a> `00b4dae8` | `00 74 15 91` | add x0,x0,#0x55d | `FALL_THROUGH`
<a id="insn-00b4daec"></a> `00b4daec` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b4daf0"></a> `00b4daf0` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b4daf4"></a> `00b4daf4` | `ef 41 02 94` | bl 0x00bde2b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4daf8"></a> `00b4daf8` | `a8 2a 00 90` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4dafc"></a> `00b4dafc` | `00 51 40 f9` | ldr x0,[x8, #0xa0] | `FALL_THROUGH`
<a id="insn-00b4db00"></a> `00b4db00` | `c0 41 02 94` | bl 0x00bde200 | `UNCONDITIONAL_CALL`
<a id="insn-00b4db04"></a> `00b4db04` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b4db08"></a> `00b4db08` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b4db0c"></a> `00b4db0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4db10"></a> `00b4db10` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00b4db14"></a> `00b4db14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4db18"></a> `00b4db18` | `a8 2a 00 90` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4db1c"></a> `00b4db1c` | `a9 2a 00 90` | adrp x9,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b4db20"></a> `00b4db20` | `01 6d 40 f9` | ldr x1,[x8, #0xd8] | `FALL_THROUGH`
<a id="insn-00b4db24"></a> `00b4db24` | `22 11 40 f9` | ldr x2,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00b4db28"></a> `00b4db28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b4db2c"></a> `00b4db2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4db30"></a> `00b4db30` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00b4db34"></a> `00b4db34` | `8a 9b e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b4db38"></a> `00b4db38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4db3c"></a> `00b4db3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b4db40"></a> `00b4db40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4db44"></a> `00b4db44` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4db48"></a> `00b4db48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4db4c"></a> `00b4db4c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4db50"></a> `00b4db50` | `a0 04 00 54` | b.eq 0x00b4dbe4 | `CONDITIONAL_JUMP`
<a id="insn-00b4db54"></a> `00b4db54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4db58"></a> `00b4db58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4db5c"></a> `00b4db5c` | `08 3d 40 f9` | ldr x8,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00b4db60"></a> `00b4db60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4db64"></a> `00b4db64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4db68"></a> `00b4db68` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b4db6c"></a> `00b4db6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4db70"></a> `00b4db70` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4db74"></a> `00b4db74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4db78"></a> `00b4db78` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4db7c"></a> `00b4db7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4db80"></a> `00b4db80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4db84"></a> `00b4db84` | `53 41 02 94` | bl 0x00bde0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4db88"></a> `00b4db88` | `de 49 02 94` | bl 0x00be0300 | `UNCONDITIONAL_CALL`
<a id="insn-00b4db8c"></a> `00b4db8c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b4db90"></a> `00b4db90` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b4db94"></a> `00b4db94` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4db98"></a> `00b4db98` | `fa 40 02 94` | bl 0x00bddf80 | `UNCONDITIONAL_CALL`
<a id="insn-00b4db9c"></a> `00b4db9c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b4dba0"></a> `00b4dba0` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dba4"></a> `00b4dba4` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00b4dba8"></a> `00b4dba8` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00b4dbac"></a> `00b4dbac` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b4dbb0"></a> `00b4dbb0` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00b4dbb4"></a> `00b4dbb4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b4dbb8"></a> `00b4dbb8` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b4dbbc"></a> `00b4dbbc` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-00b4dbc0"></a> `00b4dbc0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b4dbc4"></a> `00b4dbc4` | `8f 44 02 94` | bl 0x00bdee00 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbc8"></a> `00b4dbc8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00b4dbcc"></a> `00b4dbcc` | `1d 40 02 94` | bl 0x00bddc40 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbd0"></a> `00b4dbd0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b4dbd4"></a> `00b4dbd4` | `28 03 00 36` | tbz w8,#0x0,0x00b4dc38 | `CONDITIONAL_JUMP`
<a id="insn-00b4dbd8"></a> `00b4dbd8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dbdc"></a> `00b4dbdc` | `21 35 02 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbe0"></a> `00b4dbe0` | `16 00 00 14` | b 0x00b4dc38 | `UNCONDITIONAL_JUMP`
<a id="insn-00b4dbe4"></a> `00b4dbe4` | `b6 02 00 b4` | cbz x22,0x00b4dc38 | `CONDITIONAL_JUMP`
<a id="insn-00b4dbe8"></a> `00b4dbe8` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00b4dbec"></a> `00b4dbec` | `15 35 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbf0"></a> `00b4dbf0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b4dbf4"></a> `00b4dbf4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b4dbf8"></a> `00b4dbf8` | `e2 40 02 94` | bl 0x00bddf80 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dbfc"></a> `00b4dbfc` | `02 00 00 b0` | adrp x2,0xb4e000 | `FALL_THROUGH`
<a id="insn-00b4dc00"></a> `00b4dc00` | `44 bd ff f0` | adrp x4,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4dc04"></a> `00b4dc04` | `42 60 2d 91` | add x2,x2,#0xb58 | `FALL_THROUGH`
<a id="insn-00b4dc08"></a> `00b4dc08` | `84 e4 25 91` | add x4,x4,#0x979 | `FALL_THROUGH`
<a id="insn-00b4dc0c"></a> `00b4dc0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc10"></a> `00b4dc10` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4dc14"></a> `00b4dc14` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00b4dc18"></a> `00b4dc18` | `2a 41 02 94` | bl 0x00bde0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc1c"></a> `00b4dc1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc20"></a> `00b4dc20` | `30 41 02 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4dc24"></a> `00b4dc24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4dc28"></a> `00b4dc28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc2c"></a> `00b4dc2c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b4dc30"></a> `00b4dc30` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00b4dc34"></a> `00b4dc34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc38"></a> `00b4dc38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4dc3c"></a> `00b4dc3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4dc40"></a> `00b4dc40` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b4dc44"></a> `00b4dc44` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00b4dc48"></a> `00b4dc48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4dc4c"></a> `00b4dc4c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00b4dc50"></a> `00b4dc50` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b4dc54"></a> `00b4dc54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b4dc58"></a> `00b4dc58` | `e1 00 00 54` | b.ne 0x00b4dc74 | `CONDITIONAL_JUMP`
<a id="insn-00b4dc5c"></a> `00b4dc5c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b4dc60"></a> `00b4dc60` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b4dc64"></a> `00b4dc64` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b4dc68"></a> `00b4dc68` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b4dc6c"></a> `00b4dc6c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00b4dc70"></a> `00b4dc70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b4dc74"></a> `00b4dc74` | `07 35 02 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4dabc`](#insn-00b4dabc) 範囲 `[['00b4dabc', '00b4dabf']]`
  - `FALL_THROUGH` [`00b4dabc`](#insn-00b4dabc) → [`00b4dac0`](#insn-00b4dac0)
- ブロック [`00b4dac0`](#insn-00b4dac0) 範囲 `[['00b4dac0', '00b4dacf']]`
  - `FALL_THROUGH` [`00b4dacc`](#insn-00b4dacc) → [`00b4dad0`](#insn-00b4dad0)
- ブロック [`00b4dad0`](#insn-00b4dad0) 範囲 `[['00b4dad0', '00b4dad3']]`
  - `FALL_THROUGH` [`00b4dad0`](#insn-00b4dad0) → [`00b4dad4`](#insn-00b4dad4)
- ブロック [`00b4dad4`](#insn-00b4dad4) 範囲 `[['00b4dad4', '00b4dae3']]`
  - `FALL_THROUGH` [`00b4dae0`](#insn-00b4dae0) → [`00b4dae4`](#insn-00b4dae4)
- ブロック [`00b4dae4`](#insn-00b4dae4) 範囲 `[['00b4dae4', '00b4dae7']]`
  - `FALL_THROUGH` [`00b4dae4`](#insn-00b4dae4) → [`00b4dae8`](#insn-00b4dae8)
- ブロック [`00b4dae8`](#insn-00b4dae8) 範囲 `[['00b4dae8', '00b4daf7']]`
  - `FALL_THROUGH` [`00b4daf4`](#insn-00b4daf4) → [`00b4daf8`](#insn-00b4daf8)
- ブロック [`00b4daf8`](#insn-00b4daf8) 範囲 `[['00b4daf8', '00b4dafb']]`
  - `FALL_THROUGH` [`00b4daf8`](#insn-00b4daf8) → [`00b4dafc`](#insn-00b4dafc)
- ブロック [`00b4dafc`](#insn-00b4dafc) 範囲 `[['00b4dafc', '00b4db0b']]`
  - `FALL_THROUGH` [`00b4db08`](#insn-00b4db08) → [`00b4db0c`](#insn-00b4db0c)
- ブロック [`00b4db0c`](#insn-00b4db0c) 範囲 `[['00b4db0c', '00b4db2b']]`
  - `FALL_THROUGH` [`00b4db28`](#insn-00b4db28) → [`00b4db2c`](#insn-00b4db2c)
- ブロック [`00b4db2c`](#insn-00b4db2c) 範囲 `[['00b4db2c', '00b4db2f']]`
  - `FALL_THROUGH` [`00b4db2c`](#insn-00b4db2c) → [`00b4db30`](#insn-00b4db30)
- ブロック [`00b4db30`](#insn-00b4db30) 範囲 `[['00b4db30', '00b4db4f']]`
  - `FALL_THROUGH` [`00b4db4c`](#insn-00b4db4c) → [`00b4db50`](#insn-00b4db50)
- ブロック [`00b4db50`](#insn-00b4db50) 範囲 `[['00b4db50', '00b4db53']]`
  - `CONDITIONAL_JUMP` [`00b4db50`](#insn-00b4db50) → [`00b4dbe4`](#insn-00b4dbe4)
  - `FALL_THROUGH` [`00b4db50`](#insn-00b4db50) → [`00b4db54`](#insn-00b4db54)
- ブロック [`00b4db54`](#insn-00b4db54) 範囲 `[['00b4db54', '00b4db73']]`
  - `FALL_THROUGH` [`00b4db70`](#insn-00b4db70) → [`00b4db74`](#insn-00b4db74)
- ブロック [`00b4db74`](#insn-00b4db74) 範囲 `[['00b4db74', '00b4db77']]`
  - `FALL_THROUGH` [`00b4db74`](#insn-00b4db74) → [`00b4db78`](#insn-00b4db78)
- ブロック [`00b4db78`](#insn-00b4db78) 範囲 `[['00b4db78', '00b4db97']]`
  - `FALL_THROUGH` [`00b4db94`](#insn-00b4db94) → [`00b4db98`](#insn-00b4db98)
- ブロック [`00b4db98`](#insn-00b4db98) 範囲 `[['00b4db98', '00b4db9b']]`
  - `FALL_THROUGH` [`00b4db98`](#insn-00b4db98) → [`00b4db9c`](#insn-00b4db9c)
- ブロック [`00b4db9c`](#insn-00b4db9c) 範囲 `[['00b4db9c', '00b4db9f']]`
  - `FALL_THROUGH` [`00b4db9c`](#insn-00b4db9c) → [`00b4dba0`](#insn-00b4dba0)
- ブロック [`00b4dba0`](#insn-00b4dba0) 範囲 `[['00b4dba0', '00b4dba3']]`
  - `FALL_THROUGH` [`00b4dba0`](#insn-00b4dba0) → [`00b4dba4`](#insn-00b4dba4)
- ブロック [`00b4dba4`](#insn-00b4dba4) 範囲 `[['00b4dba4', '00b4dba7']]`
  - `FALL_THROUGH` [`00b4dba4`](#insn-00b4dba4) → [`00b4dba8`](#insn-00b4dba8)
- ブロック [`00b4dba8`](#insn-00b4dba8) 範囲 `[['00b4dba8', '00b4dbaf']]`
  - `FALL_THROUGH` [`00b4dbac`](#insn-00b4dbac) → [`00b4dbb0`](#insn-00b4dbb0)
- ブロック [`00b4dbb0`](#insn-00b4dbb0) 範囲 `[['00b4dbb0', '00b4dbb3']]`
  - `FALL_THROUGH` [`00b4dbb0`](#insn-00b4dbb0) → [`00b4dbb4`](#insn-00b4dbb4)
- ブロック [`00b4dbb4`](#insn-00b4dbb4) 範囲 `[['00b4dbb4', '00b4dbb7']]`
  - `FALL_THROUGH` [`00b4dbb4`](#insn-00b4dbb4) → [`00b4dbb8`](#insn-00b4dbb8)
- ブロック [`00b4dbb8`](#insn-00b4dbb8) 範囲 `[['00b4dbb8', '00b4dbbb']]`
  - `FALL_THROUGH` [`00b4dbb8`](#insn-00b4dbb8) → [`00b4dbbc`](#insn-00b4dbbc)
- ブロック [`00b4dbbc`](#insn-00b4dbbc) 範囲 `[['00b4dbbc', '00b4dbd7']]`
  - `CONDITIONAL_JUMP` [`00b4dbd4`](#insn-00b4dbd4) → [`00b4dc38`](#insn-00b4dc38)
  - `FALL_THROUGH` [`00b4dbd4`](#insn-00b4dbd4) → [`00b4dbd8`](#insn-00b4dbd8)
- ブロック [`00b4dbd8`](#insn-00b4dbd8) 範囲 `[['00b4dbd8', '00b4dbe3']]`
  - `UNCONDITIONAL_JUMP` [`00b4dbe0`](#insn-00b4dbe0) → [`00b4dc38`](#insn-00b4dc38)
- ブロック [`00b4dbe4`](#insn-00b4dbe4) 範囲 `[['00b4dbe4', '00b4dbe7']]`
  - `CONDITIONAL_JUMP` [`00b4dbe4`](#insn-00b4dbe4) → [`00b4dc38`](#insn-00b4dc38)
  - `FALL_THROUGH` [`00b4dbe4`](#insn-00b4dbe4) → [`00b4dbe8`](#insn-00b4dbe8)
- ブロック [`00b4dbe8`](#insn-00b4dbe8) 範囲 `[['00b4dbe8', '00b4dc23']]`
  - `FALL_THROUGH` [`00b4dc20`](#insn-00b4dc20) → [`00b4dc24`](#insn-00b4dc24)
- ブロック [`00b4dc24`](#insn-00b4dc24) 範囲 `[['00b4dc24', '00b4dc27']]`
  - `FALL_THROUGH` [`00b4dc24`](#insn-00b4dc24) → [`00b4dc28`](#insn-00b4dc28)
- ブロック [`00b4dc28`](#insn-00b4dc28) 範囲 `[['00b4dc28', '00b4dc37']]`
  - `FALL_THROUGH` [`00b4dc34`](#insn-00b4dc34) → [`00b4dc38`](#insn-00b4dc38)
- ブロック [`00b4dc38`](#insn-00b4dc38) 範囲 `[['00b4dc38', '00b4dc3b']]`
  - `FALL_THROUGH` [`00b4dc38`](#insn-00b4dc38) → [`00b4dc3c`](#insn-00b4dc3c)
- ブロック [`00b4dc3c`](#insn-00b4dc3c) 範囲 `[['00b4dc3c', '00b4dc3f']]`
  - `FALL_THROUGH` [`00b4dc3c`](#insn-00b4dc3c) → [`00b4dc40`](#insn-00b4dc40)
- ブロック [`00b4dc40`](#insn-00b4dc40) 範囲 `[['00b4dc40', '00b4dc43']]`
  - `FALL_THROUGH` [`00b4dc40`](#insn-00b4dc40) → [`00b4dc44`](#insn-00b4dc44)
- ブロック [`00b4dc44`](#insn-00b4dc44) 範囲 `[['00b4dc44', '00b4dc47']]`
  - `FALL_THROUGH` [`00b4dc44`](#insn-00b4dc44) → [`00b4dc48`](#insn-00b4dc48)
- ブロック [`00b4dc48`](#insn-00b4dc48) 範囲 `[['00b4dc48', '00b4dc5b']]`
  - `CONDITIONAL_JUMP` [`00b4dc58`](#insn-00b4dc58) → [`00b4dc74`](#insn-00b4dc74)
  - `FALL_THROUGH` [`00b4dc58`](#insn-00b4dc58) → [`00b4dc5c`](#insn-00b4dc5c)
- ブロック [`00b4dc5c`](#insn-00b4dc5c) 範囲 `[['00b4dc5c', '00b4dc63']]`
  - `FALL_THROUGH` [`00b4dc60`](#insn-00b4dc60) → [`00b4dc64`](#insn-00b4dc64)
- ブロック [`00b4dc64`](#insn-00b4dc64) 範囲 `[['00b4dc64', '00b4dc67']]`
  - `FALL_THROUGH` [`00b4dc64`](#insn-00b4dc64) → [`00b4dc68`](#insn-00b4dc68)
- ブロック [`00b4dc68`](#insn-00b4dc68) 範囲 `[['00b4dc68', '00b4dc73']]`
- ブロック [`00b4dc74`](#insn-00b4dc74) 範囲 `[['00b4dc74', '00b4dc77']]`

## 命令位置別の参照

- [`00b4dac0`](#insn-00b4dac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dac4`](#insn-00b4dac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dac8`](#insn-00b4dac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dacc`](#insn-00b4dacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dae8`](#insn-00b4dae8) → `002af55d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4daf0`](#insn-00b4daf0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4daf4`](#insn-00b4daf4) → [`00bde2b0`](../00bde/00bde2b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2b0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dafc`](#insn-00b4dafc) → `010a10a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4db00`](#insn-00b4db00) → [`00bde200`](../00bde/00bde200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde200` · 推定シンボル `None` · 推定型 `None`
- [`00b4db20`](#insn-00b4db20) → `010a10d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4db24`](#insn-00b4db24) → `010a1020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4db34`](#insn-00b4db34) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b4db50`](#insn-00b4db50) → [`00b4dbe4`](#insn-00b4dbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4db84`](#insn-00b4db84) → [`00bde0d0`](../00bde/00bde0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0d0` · 推定シンボル `None` · 推定型 `None`
- [`00b4db88`](#insn-00b4db88) → [`00be0300`](../00be0/00be0300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0300` · 推定シンボル `None` · 推定型 `None`
- [`00b4db98`](#insn-00b4db98) → [`00bddf80`](../00bdd/00bddf80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf80` · 推定シンボル `None` · 推定型 `None`
- [`00b4db9c`](#insn-00b4db9c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dba0`](#insn-00b4dba0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbc4`](#insn-00b4dbc4) → [`00bdee00`](../00bde/00bdee00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdee00` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbcc`](#insn-00b4dbcc) → [`00bddc40`](../00bdd/00bddc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc40` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbd0`](#insn-00b4dbd0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbd4`](#insn-00b4dbd4) → [`00b4dc38`](#insn-00b4dc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbd8`](#insn-00b4dbd8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbdc`](#insn-00b4dbdc) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbe0`](#insn-00b4dbe0) → [`00b4dc38`](#insn-00b4dc38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbe4`](#insn-00b4dbe4) → [`00b4dc38`](#insn-00b4dc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbec`](#insn-00b4dbec) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b4dbf8`](#insn-00b4dbf8) → [`00bddf80`](../00bdd/00bddf80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf80` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc04`](#insn-00b4dc04) → [`00b4eb58`](../00b4e/00b4eb58.md) · `PARAM` · `ANALYSIS` · 関数 `00b4eb58` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc08`](#insn-00b4dc08) → `002f8979`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4dc18`](#insn-00b4dc18) → [`00bde0c0`](../00bde/00bde0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0c0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc20`](#insn-00b4dc20) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc50`](#insn-00b4dc50) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc58`](#insn-00b4dc58) → [`00b4dc74`](#insn-00b4dc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc5c`](#insn-00b4dc5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc60`](#insn-00b4dc60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc64`](#insn-00b4dc64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc68`](#insn-00b4dc68) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4dc74`](#insn-00b4dc74) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4dac0`](#insn-00b4dac0)

~~~json
{
  "source": "00b4dac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dac4`](#insn-00b4dac4)

~~~json
{
  "source": "00b4dac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dac8`](#insn-00b4dac8)

~~~json
{
  "source": "00b4dac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dacc`](#insn-00b4dacc)

~~~json
{
  "source": "00b4dacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dae8`](#insn-00b4dae8)

~~~json
{
  "source": "00b4dae8",
  "target": "002af55d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af55d",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "556e7375627363726962652066726f6d20746f70696320257300",
  "capture_start": "002af55d",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4daf0`](#insn-00b4daf0)

~~~json
{
  "source": "00b4daf0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4daf4`](#insn-00b4daf4)

~~~json
{
  "source": "00b4daf4",
  "target": "00bde2b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dafc`](#insn-00b4dafc)

~~~json
{
  "source": "00b4dafc",
  "target": "010a10a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a10a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4db00`](#insn-00b4db00)

~~~json
{
  "source": "00b4db00",
  "target": "00bde200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4db20`](#insn-00b4db20)

~~~json
{
  "source": "00b4db20",
  "target": "010a10d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a10d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4db24`](#insn-00b4db24)

~~~json
{
  "source": "00b4db24",
  "target": "010a1020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4db34`](#insn-00b4db34)

~~~json
{
  "source": "00b4db34",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4db50`](#insn-00b4db50)

~~~json
{
  "source": "00b4db50",
  "target": "00b4dbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4db84`](#insn-00b4db84)

~~~json
{
  "source": "00b4db84",
  "target": "00bde0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4db88`](#insn-00b4db88)

~~~json
{
  "source": "00b4db88",
  "target": "00be0300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4db98`](#insn-00b4db98)

~~~json
{
  "source": "00b4db98",
  "target": "00bddf80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4db9c`](#insn-00b4db9c)

~~~json
{
  "source": "00b4db9c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dba0`](#insn-00b4dba0)

~~~json
{
  "source": "00b4dba0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbc4`](#insn-00b4dbc4)

~~~json
{
  "source": "00b4dbc4",
  "target": "00bdee00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbcc`](#insn-00b4dbcc)

~~~json
{
  "source": "00b4dbcc",
  "target": "00bddc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbd0`](#insn-00b4dbd0)

~~~json
{
  "source": "00b4dbd0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbd4`](#insn-00b4dbd4)

~~~json
{
  "source": "00b4dbd4",
  "target": "00b4dc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbd8`](#insn-00b4dbd8)

~~~json
{
  "source": "00b4dbd8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbdc`](#insn-00b4dbdc)

~~~json
{
  "source": "00b4dbdc",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbe0`](#insn-00b4dbe0)

~~~json
{
  "source": "00b4dbe0",
  "target": "00b4dc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbe4`](#insn-00b4dbe4)

~~~json
{
  "source": "00b4dbe4",
  "target": "00b4dc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dbec`](#insn-00b4dbec)

~~~json
{
  "source": "00b4dbec",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dbf8`](#insn-00b4dbf8)

~~~json
{
  "source": "00b4dbf8",
  "target": "00bddf80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc04`](#insn-00b4dc04)

~~~json
{
  "source": "00b4dc04",
  "target": "00b4eb58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc08`](#insn-00b4dc08)

~~~json
{
  "source": "00b4dc08",
  "target": "002f8979",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002f8979",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4d6573736167696e6700",
  "capture_start": "002f8979",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4dc18`](#insn-00b4dc18)

~~~json
{
  "source": "00b4dc18",
  "target": "00bde0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc20`](#insn-00b4dc20)

~~~json
{
  "source": "00b4dc20",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4dc50`](#insn-00b4dc50)

~~~json
{
  "source": "00b4dc50",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc58`](#insn-00b4dc58)

~~~json
{
  "source": "00b4dc58",
  "target": "00b4dc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc5c`](#insn-00b4dc5c)

~~~json
{
  "source": "00b4dc5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc60`](#insn-00b4dc60)

~~~json
{
  "source": "00b4dc60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc64`](#insn-00b4dc64)

~~~json
{
  "source": "00b4dc64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc68`](#insn-00b4dc68)

~~~json
{
  "source": "00b4dc68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4dc74`](#insn-00b4dc74)

~~~json
{
  "source": "00b4dc74",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
