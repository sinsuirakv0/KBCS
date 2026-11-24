# 00bd8ffc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b69afc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b69/00b69afc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-842ffb01ddd84d61c42376e41a896cc6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd9424`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd9/00bd9424.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0084.md#compare-41484018171545bf9b4b4d360fa0c535)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd8ffc",
  "name": "_ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ab5fc1decb8a368de0f9771e0c562a4486f08a6970384014008d95e8a856b06",
  "source_text_sha256": "0ab5fc1decb8a368de0f9771e0c562a4486f08a6970384014008d95e8a856b06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd8ffc",
        "00bd929b"
      ]
    ],
    "bytes_sha256": "9a10e34b61ccd138dd242c1c6c2f60328cad50790dd83c65c56f16a72f3e7fc4",
    "instruction_count": 168,
    "instruction_bytes": 672,
    "body_bytes": 672,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57be0](../00c57/00c57be0.md)
- [00c5a7a0](../00c5a/00c5a7a0.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ae60](../00c5a/00c5ae60.md)
- [00c5d910](../00c5d/00c5d910.md)
- [00c5d960](../00c5d/00c5d960.md)
- [00c5da00](../00c5d/00c5da00.md)

## 関連文字列（未確認候補）

~~~text
"A password must be provided."
"An email address must be provided."
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"email && password"
"g_methods_cached"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4249 bytes

~~~c

void _ZN8firebase4auth17EmailAuthProvider13GetCredentialEPKcS3_
               (undefined8 *param_1,char *param_2,char *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined4 uVar4;
  long lVar5;
  long *plVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  long lVar9;
  char *pcVar10;
  size_t sVar11;
  undefined8 local_98;
  undefined4 local_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  ulong local_70;
  ulong local_68;
  void *local_60;
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00bd9028 to 00cd9037 has its CatchHandler @ 00bdeb0c */
  if ((param_2 == (char *)0x0) || (param_3 == (char *)0x0)) {
    pcVar10 = "email && password";
  }
  else {
                    /* try { // try from 00bd9038 to 00cd9997 has its CatchHandler @ 00bd6d50 */
    if (DAT_011268f8 != '\0') {
      lVar5 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar5 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar5);
      uVar7 = (**(code **)(*plVar6 + 0x538))(plVar6,param_2);
      uVar8 = (**(code **)(*plVar6 + 0x538))(plVar6,param_3);
      lVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar6,DAT_01126668,DAT_01126678,uVar7,uVar8);
      (**(code **)(*plVar6 + 0xb8))(plVar6,uVar7);
      (**(code **)(*plVar6 + 0xb8))(plVar6,uVar8);
      local_68 = 0;
      local_60 = (void *)0x0;
      local_70 = 0;
      if (lVar5 == 0) {
        sVar11 = strlen(param_2);
        if (sVar11 == 0) {
          _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                    (&local_70,"An email address must be provided.",0x22);
          uVar4 = 0x25;
          uVar7 = 0;
        }
        else {
          sVar11 = strlen(param_3);
          if (sVar11 == 0) {
            _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (&local_70,"A password must be provided.",0x1c);
            uVar4 = 0x26;
            uVar7 = 0;
          }
          else {
            uVar4 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                              (plVar6,&local_70);
            uVar7 = 0;
          }
        }
      }
      else {
        lVar9 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar9 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar9);
        uVar7 = (**(code **)(*plVar6 + 0xa8))(plVar6,lVar5);
        (**(code **)(*plVar6 + 0xb8))(plVar6,lVar5);
        uVar4 = 0;
      }
      local_90 = 0;
      local_88 = 0;
      uStack_80 = 0;
      local_78 = 0;
      local_98 = uVar7;
      if (lVar5 == 0) {
        uVar1 = local_70 >> 1 & 0x7f;
        pvVar3 = (void *)((ulong)&local_70 | 1);
        if ((local_70 & 1) != 0) {
          uVar1 = local_68;
          pvVar3 = local_60;
        }
        local_90 = uVar4;
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                  (&local_88,pvVar3,uVar1);
      }
      *param_1 = 0;
      *(undefined4 *)(param_1 + 1) = 0;
      param_1[2] = 0;
      param_1[3] = 0;
      param_1[4] = 0;
      _ZN8firebase4auth10CredentialaSERKS1_(param_1,&local_98);
      _ZN8firebase4auth10CredentialD2Ev(&local_98);
      if ((local_70 & 1) != 0) {
        _ZdlPv(local_60);
      }
      goto LAB_00bd91f0;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar10 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar10);
  *param_1 = 0;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
LAB_00bd91f0:
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
<a id="insn-00bd8ffc"></a> `00bd8ffc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bd9000"></a> `00bd9000` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bd9004"></a> `00bd9004` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bd9008"></a> `00bd9008` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bd900c"></a> `00bd900c` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bd9010"></a> `00bd9010` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bd9014"></a> `00bd9014` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00bd9018"></a> `00bd9018` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bd901c"></a> `00bd901c` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bd9020"></a> `00bd9020` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bd9024"></a> `00bd9024` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bd9028"></a> `00bd9028` | `a0 0c 00 b4` | cbz x0,0x00bd91bc | `CONDITIONAL_JUMP`
<a id="insn-00bd902c"></a> `00bd902c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bd9030"></a> `00bd9030` | `61 0c 00 b4` | cbz x1,0x00bd91bc | `CONDITIONAL_JUMP`
<a id="insn-00bd9034"></a> `00bd9034` | `68 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9038"></a> `00bd9038` | `08 e1 63 39` | ldrb w8,[x8, #0x8f8] | `FALL_THROUGH`
<a id="insn-00bd903c"></a> `00bd903c` | `68 0c 00 34` | cbz w8,0x00bd91c8 | `CONDITIONAL_JUMP`
<a id="insn-00bd9040"></a> `00bd9040` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd9044"></a> `00bd9044` | `87 07 02 94` | bl 0x00c5ae60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9048"></a> `00bd9048` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd904c"></a> `00bd904c` | `80 00 00 b5` | cbnz x0,0x00bd905c | `CONDITIONAL_JUMP`
<a id="insn-00bd9050"></a> `00bd9050` | `c0 b6 ff b0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bd9054"></a> `00bd9054` | `00 60 16 91` | add x0,x0,#0x598 | `FALL_THROUGH`
<a id="insn-00bd9058"></a> `00bd9058` | `ea 06 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd905c"></a> `00bd905c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd9060"></a> `00bd9060` | `08 07 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9064"></a> `00bd9064` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd9068"></a> `00bd9068` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd906c"></a> `00bd906c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bd9070"></a> `00bd9070` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bd9074"></a> `00bd9074` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9078"></a> `00bd9078` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bd907c"></a> `00bd907c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bd9080"></a> `00bd9080` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd9084"></a> `00bd9084` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bd9088"></a> `00bd9088` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bd908c"></a> `00bd908c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9090"></a> `00bd9090` | `68 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9094"></a> `00bd9094` | `69 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd9098"></a> `00bd9098` | `01 35 43 f9` | ldr x1,[x8, #0x668] | `FALL_THROUGH`
<a id="insn-00bd909c"></a> `00bd909c` | `22 3d 43 f9` | ldr x2,[x9, #0x678] | `FALL_THROUGH`
<a id="insn-00bd90a0"></a> `00bd90a0` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bd90a4"></a> `00bd90a4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd90a8"></a> `00bd90a8` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bd90ac"></a> `00bd90ac` | `e4 03 19 aa` | mov x4,x25 | `FALL_THROUGH`
<a id="insn-00bd90b0"></a> `00bd90b0` | `bc 05 02 94` | bl 0x00c5a7a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd90b4"></a> `00bd90b4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bd90b8"></a> `00bd90b8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd90bc"></a> `00bd90bc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd90c0"></a> `00bd90c0` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bd90c4"></a> `00bd90c4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd90c8"></a> `00bd90c8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd90cc"></a> `00bd90cc` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bd90d0"></a> `00bd90d0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd90d4"></a> `00bd90d4` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bd90d8"></a> `00bd90d8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd90dc"></a> `00bd90dc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd90e0"></a> `00bd90e0` | `ff ff 03 a9` | stp xzr,xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bd90e4"></a> `00bd90e4` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd90e8"></a> `00bd90e8` | `b4 09 00 b4` | cbz x20,0x00bd921c | `CONDITIONAL_JUMP`
<a id="insn-00bd90ec"></a> `00bd90ec` | `5d 07 02 94` | bl 0x00c5ae60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd90f0"></a> `00bd90f0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd90f4"></a> `00bd90f4` | `80 00 00 b5` | cbnz x0,0x00bd9104 | `CONDITIONAL_JUMP`
<a id="insn-00bd90f8"></a> `00bd90f8` | `c0 b6 ff b0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bd90fc"></a> `00bd90fc` | `00 60 16 91` | add x0,x0,#0x598 | `FALL_THROUGH`
<a id="insn-00bd9100"></a> `00bd9100` | `c0 06 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9104"></a> `00bd9104` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd9108"></a> `00bd9108` | `de 06 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bd910c"></a> `00bd910c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd9110"></a> `00bd9110` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd9114"></a> `00bd9114` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bd9118"></a> `00bd9118` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd911c"></a> `00bd911c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9120"></a> `00bd9120` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bd9124"></a> `00bd9124` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd9128"></a> `00bd9128` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd912c"></a> `00bd912c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bd9130"></a> `00bd9130` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bd9134"></a> `00bd9134` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd9138"></a> `00bd9138` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd913c"></a> `00bd913c` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bd9140"></a> `00bd9140` | `ff 13 00 b9` | str wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd9144"></a> `00bd9144` | `ff ff 01 a9` | stp xzr,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bd9148"></a> `00bd9148` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bd914c"></a> `00bd914c` | `b4 01 00 b5` | cbnz x20,0x00bd9180 | `CONDITIONAL_JUMP`
<a id="insn-00bd9150"></a> `00bd9150` | `e9 c3 40 39` | ldrb w9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd9154"></a> `00bd9154` | `eb ab 43 a9` | ldp x11,x10,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bd9158"></a> `00bd9158` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd915c"></a> `00bd915c` | `ec c3 00 91` | add x12,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd9160"></a> `00bd9160` | `e0 13 00 b9` | str w0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd9164"></a> `00bd9164` | `00 41 00 91` | add x0,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bd9168"></a> `00bd9168` | `88 01 40 b2` | orr x8,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bd916c"></a> `00bd916c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd9170"></a> `00bd9170` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd9174"></a> `00bd9174` | `01 01 8a 9a` | csel x1,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00bd9178"></a> `00bd9178` | `82 01 8b 9a` | csel x2,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00bd917c"></a> `00bd917c` | `cd 06 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9180"></a> `00bd9180` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00bd9184"></a> `00bd9184` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bd9188"></a> `00bd9188` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd918c"></a> `00bd918c` | `9f 0e 01 f8` | str xzr,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd9190"></a> `00bd9190` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bd9194"></a> `00bd9194` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd9198"></a> `00bd9198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd919c"></a> `00bd919c` | `f1 11 02 94` | bl 0x00c5d960 | `UNCONDITIONAL_CALL`
<a id="insn-00bd91a0"></a> `00bd91a0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd91a4"></a> `00bd91a4` | `17 12 02 94` | bl 0x00c5da00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd91a8"></a> `00bd91a8` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd91ac"></a> `00bd91ac` | `28 02 00 36` | tbz w8,#0x0,0x00bd91f0 | `CONDITIONAL_JUMP`
<a id="insn-00bd91b0"></a> `00bd91b0` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bd91b4"></a> `00bd91b4` | `3f fa 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd91b8"></a> `00bd91b8` | `0e 00 00 14` | b 0x00bd91f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd91bc"></a> `00bd91bc` | `80 b6 ff b0` | adrp x0,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bd91c0"></a> `00bd91c0` | `00 7c 24 91` | add x0,x0,#0x91f | `FALL_THROUGH`
<a id="insn-00bd91c4"></a> `00bd91c4` | `06 00 00 14` | b 0x00bd91dc | `UNCONDITIONAL_JUMP`
<a id="insn-00bd91c8"></a> `00bd91c8` | `e0 b6 ff d0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bd91cc"></a> `00bd91cc` | `00 40 37 91` | add x0,x0,#0xdd0 | `FALL_THROUGH`
<a id="insn-00bd91d0"></a> `00bd91d0` | `b4 05 02 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd91d4"></a> `00bd91d4` | `a0 b9 ff f0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bd91d8"></a> `00bd91d8` | `00 c0 02 91` | add x0,x0,#0xb0 | `FALL_THROUGH`
<a id="insn-00bd91dc"></a> `00bd91dc` | `89 06 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd91e0"></a> `00bd91e0` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bd91e4"></a> `00bd91e4` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd91e8"></a> `00bd91e8` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bd91ec"></a> `00bd91ec` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd91f0"></a> `00bd91f0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bd91f4"></a> `00bd91f4` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bd91f8"></a> `00bd91f8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd91fc"></a> `00bd91fc` | `e1 04 00 54` | b.ne 0x00bd9298 | `CONDITIONAL_JUMP`
<a id="insn-00bd9200"></a> `00bd9200` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bd9204"></a> `00bd9204` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bd9208"></a> `00bd9208` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bd920c"></a> `00bd920c` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bd9210"></a> `00bd9210` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bd9214"></a> `00bd9214` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bd9218"></a> `00bd9218` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd921c"></a> `00bd921c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bd9220"></a> `00bd9220` | `70 fa 01 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9224"></a> `00bd9224` | `20 01 00 b4` | cbz x0,0x00bd9248 | `CONDITIONAL_JUMP`
<a id="insn-00bd9228"></a> `00bd9228` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd922c"></a> `00bd922c` | `6d fa 01 94` | bl 0x00c57be0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9230"></a> `00bd9230` | `00 02 00 b4` | cbz x0,0x00bd9270 | `CONDITIONAL_JUMP`
<a id="insn-00bd9234"></a> `00bd9234` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd9238"></a> `00bd9238` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd923c"></a> `00bd923c` | `b5 11 02 94` | bl 0x00c5d910 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9240"></a> `00bd9240` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bd9244"></a> `00bd9244` | `be ff ff 17` | b 0x00bd913c | `UNCONDITIONAL_JUMP`
<a id="insn-00bd9248"></a> `00bd9248` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd924c"></a> `00bd924c` | `45 06 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9250"></a> `00bd9250` | `21 b7 ff d0` | adrp x1,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bd9254"></a> `00bd9254` | `21 10 29 91` | add x1,x1,#0xa44 | `FALL_THROUGH`
<a id="insn-00bd9258"></a> `00bd9258` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd925c"></a> `00bd925c` | `42 04 80 52` | mov w2,#0x22 | `FALL_THROUGH`
<a id="insn-00bd9260"></a> `00bd9260` | `94 06 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9264"></a> `00bd9264` | `a0 04 80 52` | mov w0,#0x25 | `FALL_THROUGH`
<a id="insn-00bd9268"></a> `00bd9268` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bd926c"></a> `00bd926c` | `b4 ff ff 17` | b 0x00bd913c | `UNCONDITIONAL_JUMP`
<a id="insn-00bd9270"></a> `00bd9270` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bd9274"></a> `00bd9274` | `3b 06 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd9278"></a> `00bd9278` | `21 b6 ff d0` | adrp x1,0x29f000 | `FALL_THROUGH`
<a id="insn-00bd927c"></a> `00bd927c` | `21 6c 2f 91` | add x1,x1,#0xbdb | `FALL_THROUGH`
<a id="insn-00bd9280"></a> `00bd9280` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bd9284"></a> `00bd9284` | `82 03 80 52` | mov w2,#0x1c | `FALL_THROUGH`
<a id="insn-00bd9288"></a> `00bd9288` | `8a 06 02 94` | bl 0x00c5acb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd928c"></a> `00bd928c` | `c0 04 80 52` | mov w0,#0x26 | `FALL_THROUGH`
<a id="insn-00bd9290"></a> `00bd9290` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bd9294"></a> `00bd9294` | `aa ff ff 17` | b 0x00bd913c | `UNCONDITIONAL_JUMP`
<a id="insn-00bd9298"></a> `00bd9298` | `12 fa 01 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd8ffc`](#insn-00bd8ffc) 範囲 `[['00bd8ffc', '00bd9027']]`
  - `FALL_THROUGH` [`00bd9024`](#insn-00bd9024) → [`00bd9028`](#insn-00bd9028)
- ブロック [`00bd9028`](#insn-00bd9028) 範囲 `[['00bd9028', '00bd902b']]`
  - `CONDITIONAL_JUMP` [`00bd9028`](#insn-00bd9028) → [`00bd91bc`](#insn-00bd91bc)
  - `FALL_THROUGH` [`00bd9028`](#insn-00bd9028) → [`00bd902c`](#insn-00bd902c)
- ブロック [`00bd902c`](#insn-00bd902c) 範囲 `[['00bd902c', '00bd9033']]`
  - `CONDITIONAL_JUMP` [`00bd9030`](#insn-00bd9030) → [`00bd91bc`](#insn-00bd91bc)
  - `FALL_THROUGH` [`00bd9030`](#insn-00bd9030) → [`00bd9034`](#insn-00bd9034)
- ブロック [`00bd9034`](#insn-00bd9034) 範囲 `[['00bd9034', '00bd9037']]`
  - `FALL_THROUGH` [`00bd9034`](#insn-00bd9034) → [`00bd9038`](#insn-00bd9038)
- ブロック [`00bd9038`](#insn-00bd9038) 範囲 `[['00bd9038', '00bd903f']]`
  - `CONDITIONAL_JUMP` [`00bd903c`](#insn-00bd903c) → [`00bd91c8`](#insn-00bd91c8)
  - `FALL_THROUGH` [`00bd903c`](#insn-00bd903c) → [`00bd9040`](#insn-00bd9040)
- ブロック [`00bd9040`](#insn-00bd9040) 範囲 `[['00bd9040', '00bd904f']]`
  - `CONDITIONAL_JUMP` [`00bd904c`](#insn-00bd904c) → [`00bd905c`](#insn-00bd905c)
  - `FALL_THROUGH` [`00bd904c`](#insn-00bd904c) → [`00bd9050`](#insn-00bd9050)
- ブロック [`00bd9050`](#insn-00bd9050) 範囲 `[['00bd9050', '00bd905b']]`
  - `FALL_THROUGH` [`00bd9058`](#insn-00bd9058) → [`00bd905c`](#insn-00bd905c)
- ブロック [`00bd905c`](#insn-00bd905c) 範囲 `[['00bd905c', '00bd90eb']]`
  - `CONDITIONAL_JUMP` [`00bd90e8`](#insn-00bd90e8) → [`00bd921c`](#insn-00bd921c)
  - `FALL_THROUGH` [`00bd90e8`](#insn-00bd90e8) → [`00bd90ec`](#insn-00bd90ec)
- ブロック [`00bd90ec`](#insn-00bd90ec) 範囲 `[['00bd90ec', '00bd90f7']]`
  - `CONDITIONAL_JUMP` [`00bd90f4`](#insn-00bd90f4) → [`00bd9104`](#insn-00bd9104)
  - `FALL_THROUGH` [`00bd90f4`](#insn-00bd90f4) → [`00bd90f8`](#insn-00bd90f8)
- ブロック [`00bd90f8`](#insn-00bd90f8) 範囲 `[['00bd90f8', '00bd9103']]`
  - `FALL_THROUGH` [`00bd9100`](#insn-00bd9100) → [`00bd9104`](#insn-00bd9104)
- ブロック [`00bd9104`](#insn-00bd9104) 範囲 `[['00bd9104', '00bd913b']]`
  - `FALL_THROUGH` [`00bd9138`](#insn-00bd9138) → [`00bd913c`](#insn-00bd913c)
- ブロック [`00bd913c`](#insn-00bd913c) 範囲 `[['00bd913c', '00bd914f']]`
  - `CONDITIONAL_JUMP` [`00bd914c`](#insn-00bd914c) → [`00bd9180`](#insn-00bd9180)
  - `FALL_THROUGH` [`00bd914c`](#insn-00bd914c) → [`00bd9150`](#insn-00bd9150)
- ブロック [`00bd9150`](#insn-00bd9150) 範囲 `[['00bd9150', '00bd917f']]`
  - `FALL_THROUGH` [`00bd917c`](#insn-00bd917c) → [`00bd9180`](#insn-00bd9180)
- ブロック [`00bd9180`](#insn-00bd9180) 範囲 `[['00bd9180', '00bd91af']]`
  - `CONDITIONAL_JUMP` [`00bd91ac`](#insn-00bd91ac) → [`00bd91f0`](#insn-00bd91f0)
  - `FALL_THROUGH` [`00bd91ac`](#insn-00bd91ac) → [`00bd91b0`](#insn-00bd91b0)
- ブロック [`00bd91b0`](#insn-00bd91b0) 範囲 `[['00bd91b0', '00bd91bb']]`
  - `UNCONDITIONAL_JUMP` [`00bd91b8`](#insn-00bd91b8) → [`00bd91f0`](#insn-00bd91f0)
- ブロック [`00bd91bc`](#insn-00bd91bc) 範囲 `[['00bd91bc', '00bd91c7']]`
  - `UNCONDITIONAL_JUMP` [`00bd91c4`](#insn-00bd91c4) → [`00bd91dc`](#insn-00bd91dc)
- ブロック [`00bd91c8`](#insn-00bd91c8) 範囲 `[['00bd91c8', '00bd91db']]`
  - `FALL_THROUGH` [`00bd91d8`](#insn-00bd91d8) → [`00bd91dc`](#insn-00bd91dc)
- ブロック [`00bd91dc`](#insn-00bd91dc) 範囲 `[['00bd91dc', '00bd91ef']]`
  - `FALL_THROUGH` [`00bd91ec`](#insn-00bd91ec) → [`00bd91f0`](#insn-00bd91f0)
- ブロック [`00bd91f0`](#insn-00bd91f0) 範囲 `[['00bd91f0', '00bd91ff']]`
  - `CONDITIONAL_JUMP` [`00bd91fc`](#insn-00bd91fc) → [`00bd9298`](#insn-00bd9298)
  - `FALL_THROUGH` [`00bd91fc`](#insn-00bd91fc) → [`00bd9200`](#insn-00bd9200)
- ブロック [`00bd9200`](#insn-00bd9200) 範囲 `[['00bd9200', '00bd921b']]`
- ブロック [`00bd921c`](#insn-00bd921c) 範囲 `[['00bd921c', '00bd9227']]`
  - `CONDITIONAL_JUMP` [`00bd9224`](#insn-00bd9224) → [`00bd9248`](#insn-00bd9248)
  - `FALL_THROUGH` [`00bd9224`](#insn-00bd9224) → [`00bd9228`](#insn-00bd9228)
- ブロック [`00bd9228`](#insn-00bd9228) 範囲 `[['00bd9228', '00bd9233']]`
  - `CONDITIONAL_JUMP` [`00bd9230`](#insn-00bd9230) → [`00bd9270`](#insn-00bd9270)
  - `FALL_THROUGH` [`00bd9230`](#insn-00bd9230) → [`00bd9234`](#insn-00bd9234)
- ブロック [`00bd9234`](#insn-00bd9234) 範囲 `[['00bd9234', '00bd9247']]`
  - `UNCONDITIONAL_JUMP` [`00bd9244`](#insn-00bd9244) → [`00bd913c`](#insn-00bd913c)
- ブロック [`00bd9248`](#insn-00bd9248) 範囲 `[['00bd9248', '00bd926f']]`
  - `UNCONDITIONAL_JUMP` [`00bd926c`](#insn-00bd926c) → [`00bd913c`](#insn-00bd913c)
- ブロック [`00bd9270`](#insn-00bd9270) 範囲 `[['00bd9270', '00bd9297']]`
  - `UNCONDITIONAL_JUMP` [`00bd9294`](#insn-00bd9294) → [`00bd913c`](#insn-00bd913c)
- ブロック [`00bd9298`](#insn-00bd9298) 範囲 `[['00bd9298', '00bd929b']]`

## 命令位置別の参照

- [`00bd9000`](#insn-00bd9000) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9004`](#insn-00bd9004) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9008`](#insn-00bd9008) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd900c`](#insn-00bd900c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9010`](#insn-00bd9010) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9024`](#insn-00bd9024) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9028`](#insn-00bd9028) → [`00bd91bc`](#insn-00bd91bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9030`](#insn-00bd9030) → [`00bd91bc`](#insn-00bd91bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9038`](#insn-00bd9038) → `011268f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd903c`](#insn-00bd903c) → [`00bd91c8`](#insn-00bd91c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9044`](#insn-00bd9044) → [`00c5ae60`](../00c5a/00c5ae60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae60` · 推定シンボル `None` · 推定型 `None`
- [`00bd904c`](#insn-00bd904c) → [`00bd905c`](#insn-00bd905c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9054`](#insn-00bd9054) → `002b2598`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9058`](#insn-00bd9058) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd9060`](#insn-00bd9060) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bd9098`](#insn-00bd9098) → `01126668`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd909c`](#insn-00bd909c) → `01126678`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd90b0`](#insn-00bd90b0) → [`00c5a7a0`](../00c5a/00c5a7a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7a0` · 推定シンボル `None` · 推定型 `None`
- [`00bd90e0`](#insn-00bd90e0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd90e4`](#insn-00bd90e4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd90e8`](#insn-00bd90e8) → [`00bd921c`](#insn-00bd921c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd90ec`](#insn-00bd90ec) → [`00c5ae60`](../00c5a/00c5ae60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae60` · 推定シンボル `None` · 推定型 `None`
- [`00bd90f4`](#insn-00bd90f4) → [`00bd9104`](#insn-00bd9104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd90fc`](#insn-00bd90fc) → `002b2598`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9100`](#insn-00bd9100) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd9108`](#insn-00bd9108) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bd913c`](#insn-00bd913c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9140`](#insn-00bd9140) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9144`](#insn-00bd9144) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9148`](#insn-00bd9148) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd914c`](#insn-00bd914c) → [`00bd9180`](#insn-00bd9180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9150`](#insn-00bd9150) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9154`](#insn-00bd9154) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9160`](#insn-00bd9160) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd917c`](#insn-00bd917c) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd919c`](#insn-00bd919c) → [`00c5d960`](../00c5d/00c5d960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d960` · 推定シンボル `None` · 推定型 `None`
- [`00bd91a4`](#insn-00bd91a4) → [`00c5da00`](../00c5d/00c5da00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da00` · 推定シンボル `None` · 推定型 `None`
- [`00bd91a8`](#insn-00bd91a8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91ac`](#insn-00bd91ac) → [`00bd91f0`](#insn-00bd91f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91b0`](#insn-00bd91b0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91b4`](#insn-00bd91b4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bd91b8`](#insn-00bd91b8) → [`00bd91f0`](#insn-00bd91f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91c0`](#insn-00bd91c0) → `002aa91f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd91c4`](#insn-00bd91c4) → [`00bd91dc`](#insn-00bd91dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91cc`](#insn-00bd91cc) → `002b7dd0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd91d0`](#insn-00bd91d0) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bd91d8`](#insn-00bd91d8) → `003100b0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd91dc`](#insn-00bd91dc) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bd91f4`](#insn-00bd91f4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd91fc`](#insn-00bd91fc) → [`00bd9298`](#insn-00bd9298) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9200`](#insn-00bd9200) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9204`](#insn-00bd9204) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9208`](#insn-00bd9208) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd920c`](#insn-00bd920c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9210`](#insn-00bd9210) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9220`](#insn-00bd9220) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`00bd9224`](#insn-00bd9224) → [`00bd9248`](#insn-00bd9248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd922c`](#insn-00bd922c) → [`00c57be0`](../00c57/00c57be0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57be0` · 推定シンボル `None` · 推定型 `None`
- [`00bd9230`](#insn-00bd9230) → [`00bd9270`](#insn-00bd9270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd923c`](#insn-00bd923c) → [`00c5d910`](../00c5d/00c5d910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d910` · 推定シンボル `None` · 推定型 `None`
- [`00bd9244`](#insn-00bd9244) → [`00bd913c`](#insn-00bd913c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd924c`](#insn-00bd924c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bd9254`](#insn-00bd9254) → `002bfa44`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9260`](#insn-00bd9260) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd926c`](#insn-00bd926c) → [`00bd913c`](#insn-00bd913c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9274`](#insn-00bd9274) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bd927c`](#insn-00bd927c) → `0029fbdb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd9288`](#insn-00bd9288) → [`00c5acb0`](../00c5a/00c5acb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5acb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd9294`](#insn-00bd9294) → [`00bd913c`](#insn-00bd913c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd9298`](#insn-00bd9298) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd9000`](#insn-00bd9000)

~~~json
{
  "source": "00bd9000",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9004`](#insn-00bd9004)

~~~json
{
  "source": "00bd9004",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9008`](#insn-00bd9008)

~~~json
{
  "source": "00bd9008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd900c`](#insn-00bd900c)

~~~json
{
  "source": "00bd900c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9010`](#insn-00bd9010)

~~~json
{
  "source": "00bd9010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9024`](#insn-00bd9024)

~~~json
{
  "source": "00bd9024",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9028`](#insn-00bd9028)

~~~json
{
  "source": "00bd9028",
  "target": "00bd91bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9030`](#insn-00bd9030)

~~~json
{
  "source": "00bd9030",
  "target": "00bd91bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9038`](#insn-00bd9038)

~~~json
{
  "source": "00bd9038",
  "target": "011268f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd903c`](#insn-00bd903c)

~~~json
{
  "source": "00bd903c",
  "target": "00bd91c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9044`](#insn-00bd9044)

~~~json
{
  "source": "00bd9044",
  "target": "00c5ae60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd904c`](#insn-00bd904c)

~~~json
{
  "source": "00bd904c",
  "target": "00bd905c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9054`](#insn-00bd9054)

~~~json
{
  "source": "00bd9054",
  "target": "002b2598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2598",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2598",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9058`](#insn-00bd9058)

~~~json
{
  "source": "00bd9058",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9060`](#insn-00bd9060)

~~~json
{
  "source": "00bd9060",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9098`](#insn-00bd9098)

~~~json
{
  "source": "00bd9098",
  "target": "01126668",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126668",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd909c`](#insn-00bd909c)

~~~json
{
  "source": "00bd909c",
  "target": "01126678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126678",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd90b0`](#insn-00bd90b0)

~~~json
{
  "source": "00bd90b0",
  "target": "00c5a7a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd90e0`](#insn-00bd90e0)

~~~json
{
  "source": "00bd90e0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd90e4`](#insn-00bd90e4)

~~~json
{
  "source": "00bd90e4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd90e8`](#insn-00bd90e8)

~~~json
{
  "source": "00bd90e8",
  "target": "00bd921c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd90ec`](#insn-00bd90ec)

~~~json
{
  "source": "00bd90ec",
  "target": "00c5ae60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd90f4`](#insn-00bd90f4)

~~~json
{
  "source": "00bd90f4",
  "target": "00bd9104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd90fc`](#insn-00bd90fc)

~~~json
{
  "source": "00bd90fc",
  "target": "002b2598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2598",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2598",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9100`](#insn-00bd9100)

~~~json
{
  "source": "00bd9100",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9108`](#insn-00bd9108)

~~~json
{
  "source": "00bd9108",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd913c`](#insn-00bd913c)

~~~json
{
  "source": "00bd913c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9140`](#insn-00bd9140)

~~~json
{
  "source": "00bd9140",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9144`](#insn-00bd9144)

~~~json
{
  "source": "00bd9144",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9148`](#insn-00bd9148)

~~~json
{
  "source": "00bd9148",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd914c`](#insn-00bd914c)

~~~json
{
  "source": "00bd914c",
  "target": "00bd9180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9150`](#insn-00bd9150)

~~~json
{
  "source": "00bd9150",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9154`](#insn-00bd9154)

~~~json
{
  "source": "00bd9154",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9160`](#insn-00bd9160)

~~~json
{
  "source": "00bd9160",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd917c`](#insn-00bd917c)

~~~json
{
  "source": "00bd917c",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd919c`](#insn-00bd919c)

~~~json
{
  "source": "00bd919c",
  "target": "00c5d960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd91a4`](#insn-00bd91a4)

~~~json
{
  "source": "00bd91a4",
  "target": "00c5da00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd91a8`](#insn-00bd91a8)

~~~json
{
  "source": "00bd91a8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91ac`](#insn-00bd91ac)

~~~json
{
  "source": "00bd91ac",
  "target": "00bd91f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91b0`](#insn-00bd91b0)

~~~json
{
  "source": "00bd91b0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91b4`](#insn-00bd91b4)

~~~json
{
  "source": "00bd91b4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd91b8`](#insn-00bd91b8)

~~~json
{
  "source": "00bd91b8",
  "target": "00bd91f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91c0`](#insn-00bd91c0)

~~~json
{
  "source": "00bd91c0",
  "target": "002aa91f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa91f",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "656d61696c2026262070617373776f726400",
  "capture_start": "002aa91f",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd91c4`](#insn-00bd91c4)

~~~json
{
  "source": "00bd91c4",
  "target": "00bd91dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91cc`](#insn-00bd91cc)

~~~json
{
  "source": "00bd91cc",
  "target": "002b7dd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7dd0",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7dd0",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd91d0`](#insn-00bd91d0)

~~~json
{
  "source": "00bd91d0",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd91d8`](#insn-00bd91d8)

~~~json
{
  "source": "00bd91d8",
  "target": "003100b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003100b0",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "003100b0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd91dc`](#insn-00bd91dc)

~~~json
{
  "source": "00bd91dc",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd91f4`](#insn-00bd91f4)

~~~json
{
  "source": "00bd91f4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd91fc`](#insn-00bd91fc)

~~~json
{
  "source": "00bd91fc",
  "target": "00bd9298",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9200`](#insn-00bd9200)

~~~json
{
  "source": "00bd9200",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9204`](#insn-00bd9204)

~~~json
{
  "source": "00bd9204",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9208`](#insn-00bd9208)

~~~json
{
  "source": "00bd9208",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd920c`](#insn-00bd920c)

~~~json
{
  "source": "00bd920c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9210`](#insn-00bd9210)

~~~json
{
  "source": "00bd9210",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9220`](#insn-00bd9220)

~~~json
{
  "source": "00bd9220",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9224`](#insn-00bd9224)

~~~json
{
  "source": "00bd9224",
  "target": "00bd9248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd922c`](#insn-00bd922c)

~~~json
{
  "source": "00bd922c",
  "target": "00c57be0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9230`](#insn-00bd9230)

~~~json
{
  "source": "00bd9230",
  "target": "00bd9270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd923c`](#insn-00bd923c)

~~~json
{
  "source": "00bd923c",
  "target": "00c5d910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9244`](#insn-00bd9244)

~~~json
{
  "source": "00bd9244",
  "target": "00bd913c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd924c`](#insn-00bd924c)

~~~json
{
  "source": "00bd924c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9254`](#insn-00bd9254)

~~~json
{
  "source": "00bd9254",
  "target": "002bfa44",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfa44",
  "offset": 0,
  "size": 35,
  "datatype": "string",
  "bytes": "416e20656d61696c2061646472657373206d7573742062652070726f76696465",
  "capture_start": "002bfa44",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd9260`](#insn-00bd9260)

~~~json
{
  "source": "00bd9260",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd926c`](#insn-00bd926c)

~~~json
{
  "source": "00bd926c",
  "target": "00bd913c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9274`](#insn-00bd9274)

~~~json
{
  "source": "00bd9274",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd927c`](#insn-00bd927c)

~~~json
{
  "source": "00bd927c",
  "target": "0029fbdb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fbdb",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "412070617373776f7264206d7573742062652070726f76696465642e00",
  "capture_start": "0029fbdb",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd9288`](#insn-00bd9288)

~~~json
{
  "source": "00bd9288",
  "target": "00c5acb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd9294`](#insn-00bd9294)

~~~json
{
  "source": "00bd9294",
  "target": "00bd913c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd9298`](#insn-00bd9298)

~~~json
{
  "source": "00bd9298",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
