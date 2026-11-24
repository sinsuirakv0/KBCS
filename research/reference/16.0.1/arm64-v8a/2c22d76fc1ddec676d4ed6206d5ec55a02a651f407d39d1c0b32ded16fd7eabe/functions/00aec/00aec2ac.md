# 00aec2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aebe84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-100dc33342f0c1a471f0bf4dbf8b17a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aec348`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aec/00aec348.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-7bfa297c4e0a30c3d8bee0a90a83af2c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec2ac",
  "name": "FUN_00aec2ac",
  "size": 640,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d133c3f4303d666934a7809cb984a93ab963c76c3d14fde8fd3b874cb8029a1",
  "source_text_sha256": "4d133c3f4303d666934a7809cb984a93ab963c76c3d14fde8fd3b874cb8029a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aec2ac",
        "00aec52b"
      ]
    ],
    "bytes_sha256": "ff5a74366f10a969ad83dfba7a0eb687d936e62193d458a518e97f5ad472724e",
    "instruction_count": 160,
    "instruction_bytes": 640,
    "body_bytes": 640,
    "indirect": 9,
    "unresolved": 9
  }
}
~~~

## 呼び出し元

- [00aec52c](../00aec/00aec52c.md)

## 呼び出し先

- [0067e5e8](../0067e/0067e5e8.md)
- [00682324](../00682/00682324.md)
- [006b21e4](../006b2/006b21e4.md)
- [006b7694](../006b7/006b7694.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4233 bytes

~~~c

void FUN_00aec2ac(undefined8 *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  long *plVar4;
  
  *param_1 = &PTR_FUN_00c8d940;
                    /* try { // try from 00aec2d0 to 00bec2e3 has its CatchHandler @ 00aec834 */
  FUN_0067e5e8(param_1 + 0xa2);
  FUN_006b7694(param_1 + 0x9f,param_1[0xa0]);
  plVar4 = (long *)param_1[0x9e];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
                    /* try { // try from 00aec2fc to 00bec307 has its CatchHandler @ 00aec828 */
    (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* try { // try from 00aec308 to 00bec313 has its CatchHandler @ 00aec810 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x9c];
                    /* try { // try from 00aec314 to 00bec31f has its CatchHandler @ 00aec800 */
                    /* try { // try from 00aec320 to 00bec35f has its CatchHandler @ 00aec250 */
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x9a];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
                    /* try { // try from 00aec360 to 00bec367 has its CatchHandler @ 00aec7fc */
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x98];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* try { // try from 00aec398 to 00bec3a3 has its CatchHandler @ 00aec7e0 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x96];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  FUN_006b21e4(param_1 + 0x7e);
  FUN_006b21e4(param_1 + 0x68);
  puVar1 = (void *)param_1[0x65];
  while (puVar1 != (void *)0x0) {
    plVar4 = (long *)puVar1[4];
    pvVar3 = (void *)*puVar1;
    if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    _ZdlPv(puVar1);
    puVar1 = pvVar3;
  }
  pvVar3 = (void *)param_1[99];
  param_1[99] = 0;
  if (pvVar3 != (void *)0x0) {
    _ZdlPv(pvVar3);
  }
  puVar1 = (void *)param_1[0x60];
  while (puVar1 != (void *)0x0) {
    plVar4 = (long *)puVar1[4];
    pvVar3 = (void *)*puVar1;
                    /* try { // try from 00aec4fc to 00bec50f has its CatchHandler @ 00aec854 */
    if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    _ZdlPv(puVar1);
    puVar1 = pvVar3;
  }
  pvVar3 = (void *)param_1[0x5e];
  param_1[0x5e] = 0;
  if (pvVar3 != (void *)0x0) {
                    /* try { // try from 00aec40c to 00bec41b has its CatchHandler @ 00aec868 */
    _ZdlPv(pvVar3);
  }
  plVar4 = (long *)param_1[0x5d];
  *param_1 = &PTR_FUN_00c78330;
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x5b];
                    /* try { // try from 00aec450 to 00bec463 has its CatchHandler @ 00aec858 */
  *param_1 = &PTR_FUN_00c74810;
                    /* try { // try from 00aec464 to 00bec4fb has its CatchHandler @ 00aec250 */
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  FUN_00682324(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aec2ac"></a> `00aec2ac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aec2b0"></a> `00aec2b0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec2b4"></a> `00aec2b4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec2b8"></a> `00aec2b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aec2bc"></a> `00aec2bc` | `08 0d 00 b0` | adrp x8,0xc8d000 | `FALL_THROUGH`
<a id="insn-00aec2c0"></a> `00aec2c0` | `08 01 25 91` | add x8,x8,#0x940 | `FALL_THROUGH`
<a id="insn-00aec2c4"></a> `00aec2c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aec2c8"></a> `00aec2c8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00aec2cc"></a> `00aec2cc` | `00 40 14 91` | add x0,x0,#0x510 | `FALL_THROUGH`
<a id="insn-00aec2d0"></a> `00aec2d0` | `c6 48 ee 97` | bl 0x0067e5e8 | `UNCONDITIONAL_CALL`
<a id="insn-00aec2d4"></a> `00aec2d4` | `61 82 42 f9` | ldr x1,[x19, #0x500] | `FALL_THROUGH`
<a id="insn-00aec2d8"></a> `00aec2d8` | `60 e2 13 91` | add x0,x19,#0x4f8 | `FALL_THROUGH`
<a id="insn-00aec2dc"></a> `00aec2dc` | `ee 2c ef 97` | bl 0x006b7694 | `UNCONDITIONAL_CALL`
<a id="insn-00aec2e0"></a> `00aec2e0` | `74 7a 42 f9` | ldr x20,[x19, #0x4f0] | `FALL_THROUGH`
<a id="insn-00aec2e4"></a> `00aec2e4` | `74 01 00 b4` | cbz x20,0x00aec310 | `CONDITIONAL_JUMP`
<a id="insn-00aec2e8"></a> `00aec2e8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec2ec"></a> `00aec2ec` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec2f0"></a> `00aec2f0` | `84 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec2f4"></a> `00aec2f4` | `e0 00 00 b5` | cbnz x0,0x00aec310 | `CONDITIONAL_JUMP`
<a id="insn-00aec2f8"></a> `00aec2f8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec2fc"></a> `00aec2fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec300"></a> `00aec300` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec304"></a> `00aec304` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec308"></a> `00aec308` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec30c"></a> `00aec30c` | `dd ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec310"></a> `00aec310` | `74 72 42 f9` | ldr x20,[x19, #0x4e0] | `FALL_THROUGH`
<a id="insn-00aec314"></a> `00aec314` | `74 01 00 b4` | cbz x20,0x00aec340 | `CONDITIONAL_JUMP`
<a id="insn-00aec318"></a> `00aec318` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec31c"></a> `00aec31c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec320"></a> `00aec320` | `78 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec324"></a> `00aec324` | `e0 00 00 b5` | cbnz x0,0x00aec340 | `CONDITIONAL_JUMP`
<a id="insn-00aec328"></a> `00aec328` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec32c"></a> `00aec32c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec330"></a> `00aec330` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec334"></a> `00aec334` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec338"></a> `00aec338` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec33c"></a> `00aec33c` | `d1 ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec340"></a> `00aec340` | `74 6a 42 f9` | ldr x20,[x19, #0x4d0] | `FALL_THROUGH`
<a id="insn-00aec344"></a> `00aec344` | `74 01 00 b4` | cbz x20,0x00aec370 | `CONDITIONAL_JUMP`
<a id="insn-00aec348"></a> `00aec348` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec34c"></a> `00aec34c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec350"></a> `00aec350` | `6c 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec354"></a> `00aec354` | `e0 00 00 b5` | cbnz x0,0x00aec370 | `CONDITIONAL_JUMP`
<a id="insn-00aec358"></a> `00aec358` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec35c"></a> `00aec35c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec360"></a> `00aec360` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec364"></a> `00aec364` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec368"></a> `00aec368` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec36c"></a> `00aec36c` | `c5 ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec370"></a> `00aec370` | `74 62 42 f9` | ldr x20,[x19, #0x4c0] | `FALL_THROUGH`
<a id="insn-00aec374"></a> `00aec374` | `74 01 00 b4` | cbz x20,0x00aec3a0 | `CONDITIONAL_JUMP`
<a id="insn-00aec378"></a> `00aec378` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec37c"></a> `00aec37c` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec380"></a> `00aec380` | `60 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec384"></a> `00aec384` | `e0 00 00 b5` | cbnz x0,0x00aec3a0 | `CONDITIONAL_JUMP`
<a id="insn-00aec388"></a> `00aec388` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec38c"></a> `00aec38c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec390"></a> `00aec390` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec394"></a> `00aec394` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec398"></a> `00aec398` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec39c"></a> `00aec39c` | `b9 ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3a0"></a> `00aec3a0` | `74 5a 42 f9` | ldr x20,[x19, #0x4b0] | `FALL_THROUGH`
<a id="insn-00aec3a4"></a> `00aec3a4` | `74 01 00 b4` | cbz x20,0x00aec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00aec3a8"></a> `00aec3a8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec3ac"></a> `00aec3ac` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec3b0"></a> `00aec3b0` | `54 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3b4"></a> `00aec3b4` | `e0 00 00 b5` | cbnz x0,0x00aec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00aec3b8"></a> `00aec3b8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec3bc"></a> `00aec3bc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec3c0"></a> `00aec3c0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec3c4"></a> `00aec3c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec3c8"></a> `00aec3c8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec3cc"></a> `00aec3cc` | `ad ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3d0"></a> `00aec3d0` | `60 c2 0f 91` | add x0,x19,#0x3f0 | `FALL_THROUGH`
<a id="insn-00aec3d4"></a> `00aec3d4` | `84 17 ef 97` | bl 0x006b21e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3d8"></a> `00aec3d8` | `60 02 0d 91` | add x0,x19,#0x340 | `FALL_THROUGH`
<a id="insn-00aec3dc"></a> `00aec3dc` | `82 17 ef 97` | bl 0x006b21e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3e0"></a> `00aec3e0` | `76 96 41 f9` | ldr x22,[x19, #0x328] | `FALL_THROUGH`
<a id="insn-00aec3e4"></a> `00aec3e4` | `36 06 00 b5` | cbnz x22,0x00aec4a8 | `CONDITIONAL_JUMP`
<a id="insn-00aec3e8"></a> `00aec3e8` | `60 8e 41 f9` | ldr x0,[x19, #0x318] | `FALL_THROUGH`
<a id="insn-00aec3ec"></a> `00aec3ec` | `7f 8e 01 f9` | str xzr,[x19, #0x318] | `FALL_THROUGH`
<a id="insn-00aec3f0"></a> `00aec3f0` | `40 00 00 b4` | cbz x0,0x00aec3f8 | `CONDITIONAL_JUMP`
<a id="insn-00aec3f4"></a> `00aec3f4` | `af ae 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aec3f8"></a> `00aec3f8` | `76 82 41 f9` | ldr x22,[x19, #0x300] | `FALL_THROUGH`
<a id="insn-00aec3fc"></a> `00aec3fc` | `b6 07 00 b5` | cbnz x22,0x00aec4f0 | `CONDITIONAL_JUMP`
<a id="insn-00aec400"></a> `00aec400` | `60 7a 41 f9` | ldr x0,[x19, #0x2f0] | `FALL_THROUGH`
<a id="insn-00aec404"></a> `00aec404` | `7f 7a 01 f9` | str xzr,[x19, #0x2f0] | `FALL_THROUGH`
<a id="insn-00aec408"></a> `00aec408` | `40 00 00 b4` | cbz x0,0x00aec410 | `CONDITIONAL_JUMP`
<a id="insn-00aec40c"></a> `00aec40c` | `a9 ae 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aec410"></a> `00aec410` | `74 76 41 f9` | ldr x20,[x19, #0x2e8] | `FALL_THROUGH`
<a id="insn-00aec414"></a> `00aec414` | `68 0c 00 90` | adrp x8,0xc78000 | `FALL_THROUGH`
<a id="insn-00aec418"></a> `00aec418` | `08 c1 0c 91` | add x8,x8,#0x330 | `FALL_THROUGH`
<a id="insn-00aec41c"></a> `00aec41c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec420"></a> `00aec420` | `74 01 00 b4` | cbz x20,0x00aec44c | `CONDITIONAL_JUMP`
<a id="insn-00aec424"></a> `00aec424` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec428"></a> `00aec428` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec42c"></a> `00aec42c` | `35 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec430"></a> `00aec430` | `e0 00 00 b5` | cbnz x0,0x00aec44c | `CONDITIONAL_JUMP`
<a id="insn-00aec434"></a> `00aec434` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec438"></a> `00aec438` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec43c"></a> `00aec43c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec440"></a> `00aec440` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec444"></a> `00aec444` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec448"></a> `00aec448` | `8e ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec44c"></a> `00aec44c` | `74 6e 41 f9` | ldr x20,[x19, #0x2d8] | `FALL_THROUGH`
<a id="insn-00aec450"></a> `00aec450` | `48 0c 00 90` | adrp x8,0xc74000 | `FALL_THROUGH`
<a id="insn-00aec454"></a> `00aec454` | `08 41 20 91` | add x8,x8,#0x810 | `FALL_THROUGH`
<a id="insn-00aec458"></a> `00aec458` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00aec45c"></a> `00aec45c` | `74 01 00 b4` | cbz x20,0x00aec488 | `CONDITIONAL_JUMP`
<a id="insn-00aec460"></a> `00aec460` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aec464"></a> `00aec464` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec468"></a> `00aec468` | `26 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec46c"></a> `00aec46c` | `e0 00 00 b5` | cbnz x0,0x00aec488 | `CONDITIONAL_JUMP`
<a id="insn-00aec470"></a> `00aec470` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aec474"></a> `00aec474` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec478"></a> `00aec478` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec47c"></a> `00aec47c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec480"></a> `00aec480` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec484"></a> `00aec484` | `7f ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec488"></a> `00aec488` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aec48c"></a> `00aec48c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aec490"></a> `00aec490` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aec494"></a> `00aec494` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aec498"></a> `00aec498` | `a3 57 ee 17` | b 0x00682324 | `CALL_TERMINATOR`
<a id="insn-00aec49c"></a> `00aec49c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec4a0"></a> `00aec4a0` | `84 ae 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aec4a4"></a> `00aec4a4` | `36 fa ff b4` | cbz x22,0x00aec3e8 | `CONDITIONAL_JUMP`
<a id="insn-00aec4a8"></a> `00aec4a8` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aec4ac"></a> `00aec4ac` | `d5 12 40 f9` | ldr x21,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aec4b0"></a> `00aec4b0` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00aec4b4"></a> `00aec4b4` | `55 ff ff b4` | cbz x21,0x00aec49c | `CONDITIONAL_JUMP`
<a id="insn-00aec4b8"></a> `00aec4b8` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00aec4bc"></a> `00aec4bc` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec4c0"></a> `00aec4c0` | `10 9e 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec4c4"></a> `00aec4c4` | `c0 fe ff b5` | cbnz x0,0x00aec49c | `CONDITIONAL_JUMP`
<a id="insn-00aec4c8"></a> `00aec4c8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00aec4cc"></a> `00aec4cc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aec4d0"></a> `00aec4d0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec4d4"></a> `00aec4d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec4d8"></a> `00aec4d8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aec4dc"></a> `00aec4dc` | `69 ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec4e0"></a> `00aec4e0` | `ef ff ff 17` | b 0x00aec49c | `UNCONDITIONAL_JUMP`
<a id="insn-00aec4e4"></a> `00aec4e4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aec4e8"></a> `00aec4e8` | `72 ae 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00aec4ec"></a> `00aec4ec` | `b6 f8 ff b4` | cbz x22,0x00aec400 | `CONDITIONAL_JUMP`
<a id="insn-00aec4f0"></a> `00aec4f0` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aec4f4"></a> `00aec4f4` | `d5 12 40 f9` | ldr x21,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aec4f8"></a> `00aec4f8` | `d6 02 40 f9` | ldr x22,[x22] | `FALL_THROUGH`
<a id="insn-00aec4fc"></a> `00aec4fc` | `55 ff ff b4` | cbz x21,0x00aec4e4 | `CONDITIONAL_JUMP`
<a id="insn-00aec500"></a> `00aec500` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00aec504"></a> `00aec504` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aec508"></a> `00aec508` | `fe 9d 05 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00aec50c"></a> `00aec50c` | `c0 fe ff b5` | cbnz x0,0x00aec4e4 | `CONDITIONAL_JUMP`
<a id="insn-00aec510"></a> `00aec510` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00aec514"></a> `00aec514` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aec518"></a> `00aec518` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aec51c"></a> `00aec51c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aec520"></a> `00aec520` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aec524"></a> `00aec524` | `57 ae 05 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00aec528"></a> `00aec528` | `ef ff ff 17` | b 0x00aec4e4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aec2ac`](#insn-00aec2ac) 範囲 `[['00aec2ac', '00aec2cf']]`
  - `FALL_THROUGH` [`00aec2cc`](#insn-00aec2cc) → [`00aec2d0`](#insn-00aec2d0)
- ブロック [`00aec2d0`](#insn-00aec2d0) 範囲 `[['00aec2d0', '00aec2e7']]`
  - `CONDITIONAL_JUMP` [`00aec2e4`](#insn-00aec2e4) → [`00aec310`](#insn-00aec310)
  - `FALL_THROUGH` [`00aec2e4`](#insn-00aec2e4) → [`00aec2e8`](#insn-00aec2e8)
- ブロック [`00aec2e8`](#insn-00aec2e8) 範囲 `[['00aec2e8', '00aec2f7']]`
  - `CONDITIONAL_JUMP` [`00aec2f4`](#insn-00aec2f4) → [`00aec310`](#insn-00aec310)
  - `FALL_THROUGH` [`00aec2f4`](#insn-00aec2f4) → [`00aec2f8`](#insn-00aec2f8)
- ブロック [`00aec2f8`](#insn-00aec2f8) 範囲 `[['00aec2f8', '00aec2fb']]`
  - `FALL_THROUGH` [`00aec2f8`](#insn-00aec2f8) → [`00aec2fc`](#insn-00aec2fc)
- ブロック [`00aec2fc`](#insn-00aec2fc) 範囲 `[['00aec2fc', '00aec307']]`
  - `FALL_THROUGH` [`00aec304`](#insn-00aec304) → [`00aec308`](#insn-00aec308)
- ブロック [`00aec308`](#insn-00aec308) 範囲 `[['00aec308', '00aec30f']]`
  - `FALL_THROUGH` [`00aec30c`](#insn-00aec30c) → [`00aec310`](#insn-00aec310)
- ブロック [`00aec310`](#insn-00aec310) 範囲 `[['00aec310', '00aec313']]`
  - `FALL_THROUGH` [`00aec310`](#insn-00aec310) → [`00aec314`](#insn-00aec314)
- ブロック [`00aec314`](#insn-00aec314) 範囲 `[['00aec314', '00aec317']]`
  - `CONDITIONAL_JUMP` [`00aec314`](#insn-00aec314) → [`00aec340`](#insn-00aec340)
  - `FALL_THROUGH` [`00aec314`](#insn-00aec314) → [`00aec318`](#insn-00aec318)
- ブロック [`00aec318`](#insn-00aec318) 範囲 `[['00aec318', '00aec31f']]`
  - `FALL_THROUGH` [`00aec31c`](#insn-00aec31c) → [`00aec320`](#insn-00aec320)
- ブロック [`00aec320`](#insn-00aec320) 範囲 `[['00aec320', '00aec327']]`
  - `CONDITIONAL_JUMP` [`00aec324`](#insn-00aec324) → [`00aec340`](#insn-00aec340)
  - `FALL_THROUGH` [`00aec324`](#insn-00aec324) → [`00aec328`](#insn-00aec328)
- ブロック [`00aec328`](#insn-00aec328) 範囲 `[['00aec328', '00aec33f']]`
  - `FALL_THROUGH` [`00aec33c`](#insn-00aec33c) → [`00aec340`](#insn-00aec340)
- ブロック [`00aec340`](#insn-00aec340) 範囲 `[['00aec340', '00aec347']]`
  - `CONDITIONAL_JUMP` [`00aec344`](#insn-00aec344) → [`00aec370`](#insn-00aec370)
  - `FALL_THROUGH` [`00aec344`](#insn-00aec344) → [`00aec348`](#insn-00aec348)
- ブロック [`00aec348`](#insn-00aec348) 範囲 `[['00aec348', '00aec357']]`
  - `CONDITIONAL_JUMP` [`00aec354`](#insn-00aec354) → [`00aec370`](#insn-00aec370)
  - `FALL_THROUGH` [`00aec354`](#insn-00aec354) → [`00aec358`](#insn-00aec358)
- ブロック [`00aec358`](#insn-00aec358) 範囲 `[['00aec358', '00aec35f']]`
  - `FALL_THROUGH` [`00aec35c`](#insn-00aec35c) → [`00aec360`](#insn-00aec360)
- ブロック [`00aec360`](#insn-00aec360) 範囲 `[['00aec360', '00aec36f']]`
  - `FALL_THROUGH` [`00aec36c`](#insn-00aec36c) → [`00aec370`](#insn-00aec370)
- ブロック [`00aec370`](#insn-00aec370) 範囲 `[['00aec370', '00aec377']]`
  - `CONDITIONAL_JUMP` [`00aec374`](#insn-00aec374) → [`00aec3a0`](#insn-00aec3a0)
  - `FALL_THROUGH` [`00aec374`](#insn-00aec374) → [`00aec378`](#insn-00aec378)
- ブロック [`00aec378`](#insn-00aec378) 範囲 `[['00aec378', '00aec387']]`
  - `CONDITIONAL_JUMP` [`00aec384`](#insn-00aec384) → [`00aec3a0`](#insn-00aec3a0)
  - `FALL_THROUGH` [`00aec384`](#insn-00aec384) → [`00aec388`](#insn-00aec388)
- ブロック [`00aec388`](#insn-00aec388) 範囲 `[['00aec388', '00aec397']]`
  - `FALL_THROUGH` [`00aec394`](#insn-00aec394) → [`00aec398`](#insn-00aec398)
- ブロック [`00aec398`](#insn-00aec398) 範囲 `[['00aec398', '00aec39f']]`
  - `FALL_THROUGH` [`00aec39c`](#insn-00aec39c) → [`00aec3a0`](#insn-00aec3a0)
- ブロック [`00aec3a0`](#insn-00aec3a0) 範囲 `[['00aec3a0', '00aec3a7']]`
  - `CONDITIONAL_JUMP` [`00aec3a4`](#insn-00aec3a4) → [`00aec3d0`](#insn-00aec3d0)
  - `FALL_THROUGH` [`00aec3a4`](#insn-00aec3a4) → [`00aec3a8`](#insn-00aec3a8)
- ブロック [`00aec3a8`](#insn-00aec3a8) 範囲 `[['00aec3a8', '00aec3b7']]`
  - `CONDITIONAL_JUMP` [`00aec3b4`](#insn-00aec3b4) → [`00aec3d0`](#insn-00aec3d0)
  - `FALL_THROUGH` [`00aec3b4`](#insn-00aec3b4) → [`00aec3b8`](#insn-00aec3b8)
- ブロック [`00aec3b8`](#insn-00aec3b8) 範囲 `[['00aec3b8', '00aec3cf']]`
  - `FALL_THROUGH` [`00aec3cc`](#insn-00aec3cc) → [`00aec3d0`](#insn-00aec3d0)
- ブロック [`00aec3d0`](#insn-00aec3d0) 範囲 `[['00aec3d0', '00aec3e7']]`
  - `CONDITIONAL_JUMP` [`00aec3e4`](#insn-00aec3e4) → [`00aec4a8`](#insn-00aec4a8)
  - `FALL_THROUGH` [`00aec3e4`](#insn-00aec3e4) → [`00aec3e8`](#insn-00aec3e8)
- ブロック [`00aec3e8`](#insn-00aec3e8) 範囲 `[['00aec3e8', '00aec3f3']]`
  - `CONDITIONAL_JUMP` [`00aec3f0`](#insn-00aec3f0) → [`00aec3f8`](#insn-00aec3f8)
  - `FALL_THROUGH` [`00aec3f0`](#insn-00aec3f0) → [`00aec3f4`](#insn-00aec3f4)
- ブロック [`00aec3f4`](#insn-00aec3f4) 範囲 `[['00aec3f4', '00aec3f7']]`
  - `FALL_THROUGH` [`00aec3f4`](#insn-00aec3f4) → [`00aec3f8`](#insn-00aec3f8)
- ブロック [`00aec3f8`](#insn-00aec3f8) 範囲 `[['00aec3f8', '00aec3ff']]`
  - `CONDITIONAL_JUMP` [`00aec3fc`](#insn-00aec3fc) → [`00aec4f0`](#insn-00aec4f0)
  - `FALL_THROUGH` [`00aec3fc`](#insn-00aec3fc) → [`00aec400`](#insn-00aec400)
- ブロック [`00aec400`](#insn-00aec400) 範囲 `[['00aec400', '00aec40b']]`
  - `CONDITIONAL_JUMP` [`00aec408`](#insn-00aec408) → [`00aec410`](#insn-00aec410)
  - `FALL_THROUGH` [`00aec408`](#insn-00aec408) → [`00aec40c`](#insn-00aec40c)
- ブロック [`00aec40c`](#insn-00aec40c) 範囲 `[['00aec40c', '00aec40f']]`
  - `FALL_THROUGH` [`00aec40c`](#insn-00aec40c) → [`00aec410`](#insn-00aec410)
- ブロック [`00aec410`](#insn-00aec410) 範囲 `[['00aec410', '00aec423']]`
  - `CONDITIONAL_JUMP` [`00aec420`](#insn-00aec420) → [`00aec44c`](#insn-00aec44c)
  - `FALL_THROUGH` [`00aec420`](#insn-00aec420) → [`00aec424`](#insn-00aec424)
- ブロック [`00aec424`](#insn-00aec424) 範囲 `[['00aec424', '00aec433']]`
  - `CONDITIONAL_JUMP` [`00aec430`](#insn-00aec430) → [`00aec44c`](#insn-00aec44c)
  - `FALL_THROUGH` [`00aec430`](#insn-00aec430) → [`00aec434`](#insn-00aec434)
- ブロック [`00aec434`](#insn-00aec434) 範囲 `[['00aec434', '00aec44b']]`
  - `FALL_THROUGH` [`00aec448`](#insn-00aec448) → [`00aec44c`](#insn-00aec44c)
- ブロック [`00aec44c`](#insn-00aec44c) 範囲 `[['00aec44c', '00aec44f']]`
  - `FALL_THROUGH` [`00aec44c`](#insn-00aec44c) → [`00aec450`](#insn-00aec450)
- ブロック [`00aec450`](#insn-00aec450) 範囲 `[['00aec450', '00aec45f']]`
  - `CONDITIONAL_JUMP` [`00aec45c`](#insn-00aec45c) → [`00aec488`](#insn-00aec488)
  - `FALL_THROUGH` [`00aec45c`](#insn-00aec45c) → [`00aec460`](#insn-00aec460)
- ブロック [`00aec460`](#insn-00aec460) 範囲 `[['00aec460', '00aec463']]`
  - `FALL_THROUGH` [`00aec460`](#insn-00aec460) → [`00aec464`](#insn-00aec464)
- ブロック [`00aec464`](#insn-00aec464) 範囲 `[['00aec464', '00aec46f']]`
  - `CONDITIONAL_JUMP` [`00aec46c`](#insn-00aec46c) → [`00aec488`](#insn-00aec488)
  - `FALL_THROUGH` [`00aec46c`](#insn-00aec46c) → [`00aec470`](#insn-00aec470)
- ブロック [`00aec470`](#insn-00aec470) 範囲 `[['00aec470', '00aec487']]`
  - `FALL_THROUGH` [`00aec484`](#insn-00aec484) → [`00aec488`](#insn-00aec488)
- ブロック [`00aec488`](#insn-00aec488) 範囲 `[['00aec488', '00aec49b']]`
- ブロック [`00aec49c`](#insn-00aec49c) 範囲 `[['00aec49c', '00aec4a7']]`
  - `CONDITIONAL_JUMP` [`00aec4a4`](#insn-00aec4a4) → [`00aec3e8`](#insn-00aec3e8)
  - `FALL_THROUGH` [`00aec4a4`](#insn-00aec4a4) → [`00aec4a8`](#insn-00aec4a8)
- ブロック [`00aec4a8`](#insn-00aec4a8) 範囲 `[['00aec4a8', '00aec4b7']]`
  - `CONDITIONAL_JUMP` [`00aec4b4`](#insn-00aec4b4) → [`00aec49c`](#insn-00aec49c)
  - `FALL_THROUGH` [`00aec4b4`](#insn-00aec4b4) → [`00aec4b8`](#insn-00aec4b8)
- ブロック [`00aec4b8`](#insn-00aec4b8) 範囲 `[['00aec4b8', '00aec4c7']]`
  - `CONDITIONAL_JUMP` [`00aec4c4`](#insn-00aec4c4) → [`00aec49c`](#insn-00aec49c)
  - `FALL_THROUGH` [`00aec4c4`](#insn-00aec4c4) → [`00aec4c8`](#insn-00aec4c8)
- ブロック [`00aec4c8`](#insn-00aec4c8) 範囲 `[['00aec4c8', '00aec4e3']]`
  - `UNCONDITIONAL_JUMP` [`00aec4e0`](#insn-00aec4e0) → [`00aec49c`](#insn-00aec49c)
- ブロック [`00aec4e4`](#insn-00aec4e4) 範囲 `[['00aec4e4', '00aec4ef']]`
  - `CONDITIONAL_JUMP` [`00aec4ec`](#insn-00aec4ec) → [`00aec400`](#insn-00aec400)
  - `FALL_THROUGH` [`00aec4ec`](#insn-00aec4ec) → [`00aec4f0`](#insn-00aec4f0)
- ブロック [`00aec4f0`](#insn-00aec4f0) 範囲 `[['00aec4f0', '00aec4fb']]`
  - `FALL_THROUGH` [`00aec4f8`](#insn-00aec4f8) → [`00aec4fc`](#insn-00aec4fc)
- ブロック [`00aec4fc`](#insn-00aec4fc) 範囲 `[['00aec4fc', '00aec4ff']]`
  - `CONDITIONAL_JUMP` [`00aec4fc`](#insn-00aec4fc) → [`00aec4e4`](#insn-00aec4e4)
  - `FALL_THROUGH` [`00aec4fc`](#insn-00aec4fc) → [`00aec500`](#insn-00aec500)
- ブロック [`00aec500`](#insn-00aec500) 範囲 `[['00aec500', '00aec50f']]`
  - `CONDITIONAL_JUMP` [`00aec50c`](#insn-00aec50c) → [`00aec4e4`](#insn-00aec4e4)
  - `FALL_THROUGH` [`00aec50c`](#insn-00aec50c) → [`00aec510`](#insn-00aec510)
- ブロック [`00aec510`](#insn-00aec510) 範囲 `[['00aec510', '00aec52b']]`
  - `UNCONDITIONAL_JUMP` [`00aec528`](#insn-00aec528) → [`00aec4e4`](#insn-00aec4e4)

## 命令位置別の参照

- [`00aec2ac`](#insn-00aec2ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2b0`](#insn-00aec2b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2b4`](#insn-00aec2b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2c8`](#insn-00aec2c8) → `00c8d940`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aec2d0`](#insn-00aec2d0) → [`0067e5e8`](../0067e/0067e5e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067e5e8` · 推定シンボル `None` · 推定型 `None`
- [`00aec2dc`](#insn-00aec2dc) → [`006b7694`](../006b7/006b7694.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b7694` · 推定シンボル `None` · 推定型 `None`
- [`00aec2e4`](#insn-00aec2e4) → [`00aec310`](#insn-00aec310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec2f0`](#insn-00aec2f0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec2f4`](#insn-00aec2f4) → [`00aec310`](#insn-00aec310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec30c`](#insn-00aec30c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec314`](#insn-00aec314) → [`00aec340`](#insn-00aec340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec320`](#insn-00aec320) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec324`](#insn-00aec324) → [`00aec340`](#insn-00aec340) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec33c`](#insn-00aec33c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec344`](#insn-00aec344) → [`00aec370`](#insn-00aec370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec350`](#insn-00aec350) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec354`](#insn-00aec354) → [`00aec370`](#insn-00aec370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec36c`](#insn-00aec36c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec374`](#insn-00aec374) → [`00aec3a0`](#insn-00aec3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec380`](#insn-00aec380) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec384`](#insn-00aec384) → [`00aec3a0`](#insn-00aec3a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec39c`](#insn-00aec39c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec3a4`](#insn-00aec3a4) → [`00aec3d0`](#insn-00aec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec3b0`](#insn-00aec3b0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec3b4`](#insn-00aec3b4) → [`00aec3d0`](#insn-00aec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec3cc`](#insn-00aec3cc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec3d4`](#insn-00aec3d4) → [`006b21e4`](../006b2/006b21e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b21e4` · 推定シンボル `None` · 推定型 `None`
- [`00aec3dc`](#insn-00aec3dc) → [`006b21e4`](../006b2/006b21e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006b21e4` · 推定シンボル `None` · 推定型 `None`
- [`00aec3e4`](#insn-00aec3e4) → [`00aec4a8`](#insn-00aec4a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec3f0`](#insn-00aec3f0) → [`00aec3f8`](#insn-00aec3f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec3f4`](#insn-00aec3f4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aec3fc`](#insn-00aec3fc) → [`00aec4f0`](#insn-00aec4f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec408`](#insn-00aec408) → [`00aec410`](#insn-00aec410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec40c`](#insn-00aec40c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aec41c`](#insn-00aec41c) → `00c78330`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aec420`](#insn-00aec420) → [`00aec44c`](#insn-00aec44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec42c`](#insn-00aec42c) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec430`](#insn-00aec430) → [`00aec44c`](#insn-00aec44c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec448`](#insn-00aec448) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec458`](#insn-00aec458) → `00c74810`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aec45c`](#insn-00aec45c) → [`00aec488`](#insn-00aec488) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec468`](#insn-00aec468) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec46c`](#insn-00aec46c) → [`00aec488`](#insn-00aec488) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec484`](#insn-00aec484) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec48c`](#insn-00aec48c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec490`](#insn-00aec490) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec494`](#insn-00aec494) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec498`](#insn-00aec498) → [`00682324`](../00682/00682324.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00682324` · 推定シンボル `None` · 推定型 `None`
- [`00aec4a0`](#insn-00aec4a0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aec4a4`](#insn-00aec4a4) → [`00aec3e8`](#insn-00aec3e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4b4`](#insn-00aec4b4) → [`00aec49c`](#insn-00aec49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4c0`](#insn-00aec4c0) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec4c4`](#insn-00aec4c4) → [`00aec49c`](#insn-00aec49c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4dc`](#insn-00aec4dc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec4e0`](#insn-00aec4e0) → [`00aec49c`](#insn-00aec49c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4e8`](#insn-00aec4e8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00aec4ec`](#insn-00aec4ec) → [`00aec400`](#insn-00aec400) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec4fc`](#insn-00aec4fc) → [`00aec4e4`](#insn-00aec4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec508`](#insn-00aec508) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00aec50c`](#insn-00aec50c) → [`00aec4e4`](#insn-00aec4e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aec524`](#insn-00aec524) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00aec528`](#insn-00aec528) → [`00aec4e4`](#insn-00aec4e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aec2ac`](#insn-00aec2ac)

~~~json
{
  "source": "00aec2ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2b0`](#insn-00aec2b0)

~~~json
{
  "source": "00aec2b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2b4`](#insn-00aec2b4)

~~~json
{
  "source": "00aec2b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2c8`](#insn-00aec2c8)

~~~json
{
  "source": "00aec2c8",
  "target": "00c8d940",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8d940",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aec2d0`](#insn-00aec2d0)

~~~json
{
  "source": "00aec2d0",
  "target": "0067e5e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec2dc`](#insn-00aec2dc)

~~~json
{
  "source": "00aec2dc",
  "target": "006b7694",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec2e4`](#insn-00aec2e4)

~~~json
{
  "source": "00aec2e4",
  "target": "00aec310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec2f0`](#insn-00aec2f0)

~~~json
{
  "source": "00aec2f0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec2f4`](#insn-00aec2f4)

~~~json
{
  "source": "00aec2f4",
  "target": "00aec310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec30c`](#insn-00aec30c)

~~~json
{
  "source": "00aec30c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec314`](#insn-00aec314)

~~~json
{
  "source": "00aec314",
  "target": "00aec340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec320`](#insn-00aec320)

~~~json
{
  "source": "00aec320",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec324`](#insn-00aec324)

~~~json
{
  "source": "00aec324",
  "target": "00aec340",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec33c`](#insn-00aec33c)

~~~json
{
  "source": "00aec33c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec344`](#insn-00aec344)

~~~json
{
  "source": "00aec344",
  "target": "00aec370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec350`](#insn-00aec350)

~~~json
{
  "source": "00aec350",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec354`](#insn-00aec354)

~~~json
{
  "source": "00aec354",
  "target": "00aec370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec36c`](#insn-00aec36c)

~~~json
{
  "source": "00aec36c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec374`](#insn-00aec374)

~~~json
{
  "source": "00aec374",
  "target": "00aec3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec380`](#insn-00aec380)

~~~json
{
  "source": "00aec380",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec384`](#insn-00aec384)

~~~json
{
  "source": "00aec384",
  "target": "00aec3a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec39c`](#insn-00aec39c)

~~~json
{
  "source": "00aec39c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3a4`](#insn-00aec3a4)

~~~json
{
  "source": "00aec3a4",
  "target": "00aec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec3b0`](#insn-00aec3b0)

~~~json
{
  "source": "00aec3b0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3b4`](#insn-00aec3b4)

~~~json
{
  "source": "00aec3b4",
  "target": "00aec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec3cc`](#insn-00aec3cc)

~~~json
{
  "source": "00aec3cc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3d4`](#insn-00aec3d4)

~~~json
{
  "source": "00aec3d4",
  "target": "006b21e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3dc`](#insn-00aec3dc)

~~~json
{
  "source": "00aec3dc",
  "target": "006b21e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3e4`](#insn-00aec3e4)

~~~json
{
  "source": "00aec3e4",
  "target": "00aec4a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec3f0`](#insn-00aec3f0)

~~~json
{
  "source": "00aec3f0",
  "target": "00aec3f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec3f4`](#insn-00aec3f4)

~~~json
{
  "source": "00aec3f4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec3fc`](#insn-00aec3fc)

~~~json
{
  "source": "00aec3fc",
  "target": "00aec4f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec408`](#insn-00aec408)

~~~json
{
  "source": "00aec408",
  "target": "00aec410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec40c`](#insn-00aec40c)

~~~json
{
  "source": "00aec40c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec41c`](#insn-00aec41c)

~~~json
{
  "source": "00aec41c",
  "target": "00c78330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c78330",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aec420`](#insn-00aec420)

~~~json
{
  "source": "00aec420",
  "target": "00aec44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec42c`](#insn-00aec42c)

~~~json
{
  "source": "00aec42c",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec430`](#insn-00aec430)

~~~json
{
  "source": "00aec430",
  "target": "00aec44c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec448`](#insn-00aec448)

~~~json
{
  "source": "00aec448",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec458`](#insn-00aec458)

~~~json
{
  "source": "00aec458",
  "target": "00c74810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c74810",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aec45c`](#insn-00aec45c)

~~~json
{
  "source": "00aec45c",
  "target": "00aec488",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec468`](#insn-00aec468)

~~~json
{
  "source": "00aec468",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec46c`](#insn-00aec46c)

~~~json
{
  "source": "00aec46c",
  "target": "00aec488",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec484`](#insn-00aec484)

~~~json
{
  "source": "00aec484",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec48c`](#insn-00aec48c)

~~~json
{
  "source": "00aec48c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec490`](#insn-00aec490)

~~~json
{
  "source": "00aec490",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec494`](#insn-00aec494)

~~~json
{
  "source": "00aec494",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec498`](#insn-00aec498)

~~~json
{
  "source": "00aec498",
  "target": "00682324",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4a0`](#insn-00aec4a0)

~~~json
{
  "source": "00aec4a0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4a4`](#insn-00aec4a4)

~~~json
{
  "source": "00aec4a4",
  "target": "00aec3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4b4`](#insn-00aec4b4)

~~~json
{
  "source": "00aec4b4",
  "target": "00aec49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4c0`](#insn-00aec4c0)

~~~json
{
  "source": "00aec4c0",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4c4`](#insn-00aec4c4)

~~~json
{
  "source": "00aec4c4",
  "target": "00aec49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4dc`](#insn-00aec4dc)

~~~json
{
  "source": "00aec4dc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4e0`](#insn-00aec4e0)

~~~json
{
  "source": "00aec4e0",
  "target": "00aec49c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4e8`](#insn-00aec4e8)

~~~json
{
  "source": "00aec4e8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec4ec`](#insn-00aec4ec)

~~~json
{
  "source": "00aec4ec",
  "target": "00aec400",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec4fc`](#insn-00aec4fc)

~~~json
{
  "source": "00aec4fc",
  "target": "00aec4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec508`](#insn-00aec508)

~~~json
{
  "source": "00aec508",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec50c`](#insn-00aec50c)

~~~json
{
  "source": "00aec50c",
  "target": "00aec4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aec524`](#insn-00aec524)

~~~json
{
  "source": "00aec524",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aec528`](#insn-00aec528)

~~~json
{
  "source": "00aec528",
  "target": "00aec4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
