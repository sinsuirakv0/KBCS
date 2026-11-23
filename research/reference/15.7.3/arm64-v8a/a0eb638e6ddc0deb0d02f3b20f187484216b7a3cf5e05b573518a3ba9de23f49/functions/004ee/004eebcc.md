# 004eebcc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `004eebcc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004ee/004eebcc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0002.md#compare-6e3294b41d0843180b044a0ad9c66941)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `004eebcc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eebcc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0002.md#compare-bc46d1189d6c231f86a717049d13182d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eebcc",
  "name": "_ZN5Botan11X509_Object11make_signedEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE",
  "size": 488,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "292c4f57b5dc4a7d3e55a66373ef9f8f6335d003f3c5bea451e9413f4fa76b8a",
  "source_text_sha256": "292c4f57b5dc4a7d3e55a66373ef9f8f6335d003f3c5bea451e9413f4fa76b8a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004eebcc",
        "004eedaf"
      ],
      [
        "004eede8",
        "004eedeb"
      ]
    ],
    "bytes_sha256": "87091c697aa0d8d3b3365d59296673b22d6e977b6cf3ab7902ccca93d62e4ad3",
    "instruction_count": 122,
    "instruction_bytes": 488,
    "body_bytes": 488,
    "indirect": 3,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bdcec0](../00bdc/00bdcec0.md)

## 呼び出し先

- [00483ed8](../00483/00483ed8.md)
- [00512ca8](../00512/00512ca8.md)
- [0051d614](../0051d/0051d614.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bdb810](../00bdb/00bdb810.md)
- [00bdb820](../00bdb/00bdb820.md)
- [00bdb830](../00bdb/00bdb830.md)
- [00bdbc90](../00bdb/00bdbc90.md)
- [00bdc3b0](../00bdc/00bdc3b0.md)
- [010a5058](../010a5/010a5058.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2506 bytes

~~~c

void _ZN5Botan11X509_Object11make_signedEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE
               (undefined8 param_1,undefined8 *param_2,undefined8 param_3,undefined8 *param_4,
               long *param_5)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  long lVar4;
  size_t __n;
  ulong uVar5;
  void *local_a0;
  void *pvStack_98;
  long local_90;
  void *pvStack_88;
  void *local_80;
  undefined8 uStack_78;
  void *local_70;
  void *local_68;
  long local_58;
  
  lVar4 = tpidr_el0;
  local_58 = *(long *)(lVar4 + 0x28);
  (*(code *)**(undefined8 **)*param_2)((undefined8 *)*param_2,*param_5,param_5[1] - *param_5);
  _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE(&local_70,param_2,param_3);
  pvStack_88 = (void *)0x0;
  local_90 = 0;
  uStack_78 = 0;
  local_80 = (void *)0x0;
  pvStack_98 = (void *)0x0;
  local_a0 = (void *)0x0;
  _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_(&local_a0,0x10,0);
  pvVar2 = (void *)*param_5;
  pvVar3 = (void *)param_5[1];
  __n = (long)pvVar3 - (long)pvVar2;
  if (local_80 == pvStack_88) {
    uVar5 = (long)pvStack_98 - (long)local_a0;
    uVar1 = uVar5 + __n;
    if (uVar5 < uVar1) {
      FUN_0051d614(&local_a0,__n);
    }
    else if (uVar5 != uVar1) {
      pvStack_98 = (void *)((long)local_a0 + uVar1);
    }
    if (pvVar3 != pvVar2) {
      memmove((void *)((long)local_a0 + uVar5),pvVar2,__n);
    }
  }
  else {
    _ZN5Botan11DER_Encoder12DER_Sequence9add_bytesEPKhm((long)local_80 + -0x38,pvVar2);
  }
  (**(code **)*param_4)(param_4,&local_a0);
  _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_
            (&local_a0,local_70,(long)local_68 - (long)local_70,3,3,0);
  _ZN5Botan11DER_Encoder8end_consEv(&local_a0);
  FUN_00483ed8(param_1,&local_a0);
  pvVar3 = pvStack_88;
  pvVar2 = local_80;
  if (pvStack_88 != (void *)0x0) {
    while (pvVar2 != pvVar3) {
      FUN_00512ca8(&uStack_78,(void *)((long)pvVar2 + -0x38));
      pvVar2 = (void *)((long)pvVar2 + -0x38);
    }
    local_80 = pvVar3;
    _ZdlPv(pvStack_88);
  }
  pvVar2 = local_a0;
  if (local_a0 != (void *)0x0) {
    pvStack_98 = local_a0;
    (*(code *)PTR_memset_00bea728)(local_a0,0,local_90 - (long)local_a0);
    free(pvVar2);
  }
  if (local_70 != (void *)0x0) {
    local_68 = local_70;
    _ZdlPv(local_70);
  }
  if (*(long *)(lVar4 + 0x28) != local_58) {
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
<a id="insn-004eebcc"></a> `004eebcc` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004eebd0"></a> `004eebd0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004eebd4"></a> `004eebd4` | `f9 33 00 f9` | str x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004eebd8"></a> `004eebd8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004eebdc"></a> `004eebdc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004eebe0"></a> `004eebe0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004eebe4"></a> `004eebe4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004eebe8"></a> `004eebe8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004eebec"></a> `004eebec` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004eebf0"></a> `004eebf0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-004eebf4"></a> `004eebf4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004eebf8"></a> `004eebf8` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-004eebfc"></a> `004eebfc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-004eec00"></a> `004eec00` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-004eec04"></a> `004eec04` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eec08"></a> `004eec08` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-004eec0c"></a> `004eec0c` | `61 24 40 a9` | ldp x1,x9,[x3] | `FALL_THROUGH`
<a id="insn-004eec10"></a> `004eec10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004eec14"></a> `004eec14` | `22 01 01 cb` | sub x2,x9,x1 | `FALL_THROUGH`
<a id="insn-004eec18"></a> `004eec18` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004eec1c"></a> `004eec1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004eec20"></a> `004eec20` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-004eec24"></a> `004eec24` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004eec28"></a> `004eec28` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004eec2c"></a> `004eec2c` | `e1 b5 1b 94` | bl 0x00bdc3b0 | `UNCONDITIONAL_CALL`
<a id="insn-004eec30"></a> `004eec30` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004eec34"></a> `004eec34` | `e0 83 00 ad` | stp q0,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004eec38"></a> `004eec38` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-004eec3c"></a> `004eec3c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004eec40"></a> `004eec40` | `01 02 80 52` | mov w1,#0x10 | `FALL_THROUGH`
<a id="insn-004eec44"></a> `004eec44` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-004eec48"></a> `004eec48` | `f2 b2 1b 94` | bl 0x00bdb810 | `UNCONDITIONAL_CALL`
<a id="insn-004eec4c"></a> `004eec4c` | `e9 a3 41 a9` | ldp x9,x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004eec50"></a> `004eec50` | `b6 56 40 a9` | ldp x22,x21,[x21] | `FALL_THROUGH`
<a id="insn-004eec54"></a> `004eec54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004eec58"></a> `004eec58` | `a2 02 16 cb` | sub x2,x21,x22 | `FALL_THROUGH`
<a id="insn-004eec5c"></a> `004eec5c` | `a0 00 00 54` | b.eq 0x004eec70 | `CONDITIONAL_JUMP`
<a id="insn-004eec60"></a> `004eec60` | `00 e1 00 d1` | sub x0,x8,#0x38 | `FALL_THROUGH`
<a id="insn-004eec64"></a> `004eec64` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004eec68"></a> `004eec68` | `ee b2 1b 94` | bl 0x00bdb820 | `UNCONDITIONAL_CALL`
<a id="insn-004eec6c"></a> `004eec6c` | `15 00 00 14` | b 0x004eecc0 | `UNCONDITIONAL_JUMP`
<a id="insn-004eec70"></a> `004eec70` | `e8 27 40 a9` | ldp x8,x9,[sp] | `FALL_THROUGH`
<a id="insn-004eec74"></a> `004eec74` | `37 01 08 cb` | sub x23,x9,x8 | `FALL_THROUGH`
<a id="insn-004eec78"></a> `004eec78` | `e9 02 02 8b` | add x9,x23,x2 | `FALL_THROUGH`
<a id="insn-004eec7c"></a> `004eec7c` | `ff 02 09 eb` | cmp x23,x9 | `FALL_THROUGH`
<a id="insn-004eec80"></a> `004eec80` | `e2 00 00 54` | b.cs 0x004eec9c | `CONDITIONAL_JUMP`
<a id="insn-004eec84"></a> `004eec84` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004eec88"></a> `004eec88` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-004eec8c"></a> `004eec8c` | `f9 03 02 aa` | mov x25,x2 | `FALL_THROUGH`
<a id="insn-004eec90"></a> `004eec90` | `61 ba 00 94` | bl 0x0051d614 | `UNCONDITIONAL_CALL`
<a id="insn-004eec94"></a> `004eec94` | `e2 03 19 aa` | mov x2,x25 | `FALL_THROUGH`
<a id="insn-004eec98"></a> `004eec98` | `04 00 00 14` | b 0x004eeca8 | `UNCONDITIONAL_JUMP`
<a id="insn-004eec9c"></a> `004eec9c` | `69 00 00 54` | b.ls 0x004eeca8 | `CONDITIONAL_JUMP`
<a id="insn-004eeca0"></a> `004eeca0` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004eeca4"></a> `004eeca4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004eeca8"></a> `004eeca8` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-004eecac"></a> `004eecac` | `a0 00 00 54` | b.eq 0x004eecc0 | `CONDITIONAL_JUMP`
<a id="insn-004eecb0"></a> `004eecb0` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-004eecb4"></a> `004eecb4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004eecb8"></a> `004eecb8` | `00 01 17 8b` | add x0,x8,x23 | `FALL_THROUGH`
<a id="insn-004eecbc"></a> `004eecbc` | `f9 b0 1b 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-004eecc0"></a> `004eecc0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004eecc4"></a> `004eecc4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-004eecc8"></a> `004eecc8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004eeccc"></a> `004eeccc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004eecd0"></a> `004eecd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004eecd4"></a> `004eecd4` | `a1 23 7e a9` | ldp x1,x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004eecd8"></a> `004eecd8` | `02 01 01 cb` | sub x2,x8,x1 | `FALL_THROUGH`
<a id="insn-004eecdc"></a> `004eecdc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004eece0"></a> `004eece0` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-004eece4"></a> `004eece4` | `64 00 80 52` | mov w4,#0x3 | `FALL_THROUGH`
<a id="insn-004eece8"></a> `004eece8` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-004eecec"></a> `004eecec` | `e9 b3 1b 94` | bl 0x00bdbc90 | `UNCONDITIONAL_CALL`
<a id="insn-004eecf0"></a> `004eecf0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004eecf4"></a> `004eecf4` | `cf b2 1b 94` | bl 0x00bdb830 | `UNCONDITIONAL_CALL`
<a id="insn-004eecf8"></a> `004eecf8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-004eecfc"></a> `004eecfc` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004eed00"></a> `004eed00` | `76 54 fe 97` | bl 0x00483ed8 | `UNCONDITIONAL_CALL`
<a id="insn-004eed04"></a> `004eed04` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004eed08"></a> `004eed08` | `f4 01 00 b4` | cbz x20,0x004eed44 | `CONDITIONAL_JUMP`
<a id="insn-004eed0c"></a> `004eed0c` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004eed10"></a> `004eed10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004eed14"></a> `004eed14` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004eed18"></a> `004eed18` | `20 01 00 54` | b.eq 0x004eed3c | `CONDITIONAL_JUMP`
<a id="insn-004eed1c"></a> `004eed1c` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-004eed20"></a> `004eed20` | `73 e2 00 d1` | sub x19,x19,#0x38 | `FALL_THROUGH`
<a id="insn-004eed24"></a> `004eed24` | `a0 a2 00 91` | add x0,x21,#0x28 | `FALL_THROUGH`
<a id="insn-004eed28"></a> `004eed28` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-004eed2c"></a> `004eed2c` | `df 8f 00 94` | bl 0x00512ca8 | `UNCONDITIONAL_CALL`
<a id="insn-004eed30"></a> `004eed30` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-004eed34"></a> `004eed34` | `61 ff ff 54` | b.ne 0x004eed20 | `CONDITIONAL_JUMP`
<a id="insn-004eed38"></a> `004eed38` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004eed3c"></a> `004eed3c` | `f4 13 00 f9` | str x20,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004eed40"></a> `004eed40` | `b4 b0 1b 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-004eed44"></a> `004eed44` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-004eed48"></a> `004eed48` | `73 01 00 b4` | cbz x19,0x004eed74 | `CONDITIONAL_JUMP`
<a id="insn-004eed4c"></a> `004eed4c` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004eed50"></a> `004eed50` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004eed54"></a> `004eed54` | `e9 37 00 90` | adrp x9,0xbea000 | `FALL_THROUGH`
<a id="insn-004eed58"></a> `004eed58` | `29 95 43 f9` | ldr x9,[x9, #0x728] | `FALL_THROUGH`
<a id="insn-004eed5c"></a> `004eed5c` | `02 01 13 cb` | sub x2,x8,x19 | `FALL_THROUGH`
<a id="insn-004eed60"></a> `004eed60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004eed64"></a> `004eed64` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-004eed68"></a> `004eed68` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004eed6c"></a> `004eed6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004eed70"></a> `004eed70` | `94 b2 1b 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-004eed74"></a> `004eed74` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004eed78"></a> `004eed78` | `60 00 00 b4` | cbz x0,0x004eed84 | `CONDITIONAL_JUMP`
<a id="insn-004eed7c"></a> `004eed7c` | `a0 83 1e f8` | stur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-004eed80"></a> `004eed80` | `a4 b0 1b 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-004eed84"></a> `004eed84` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004eed88"></a> `004eed88` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004eed8c"></a> `004eed8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004eed90"></a> `004eed90` | `c1 02 00 54` | b.ne 0x004eede8 | `CONDITIONAL_JUMP`
<a id="insn-004eed94"></a> `004eed94` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004eed98"></a> `004eed98` | `f9 33 40 f9` | ldr x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004eed9c"></a> `004eed9c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004eeda0"></a> `004eeda0` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004eeda4"></a> `004eeda4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004eeda8"></a> `004eeda8` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004eedac"></a> `004eedac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004eede8"></a> `004eede8` | `96 b0 1b 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004eebcc`](#insn-004eebcc) 範囲 `[['004eebcc', '004eec5f']]`
  - `CONDITIONAL_JUMP` [`004eec5c`](#insn-004eec5c) → [`004eec70`](#insn-004eec70)
  - `FALL_THROUGH` [`004eec5c`](#insn-004eec5c) → [`004eec60`](#insn-004eec60)
- ブロック [`004eec60`](#insn-004eec60) 範囲 `[['004eec60', '004eec6f']]`
  - `UNCONDITIONAL_JUMP` [`004eec6c`](#insn-004eec6c) → [`004eecc0`](#insn-004eecc0)
- ブロック [`004eec70`](#insn-004eec70) 範囲 `[['004eec70', '004eec83']]`
  - `CONDITIONAL_JUMP` [`004eec80`](#insn-004eec80) → [`004eec9c`](#insn-004eec9c)
  - `FALL_THROUGH` [`004eec80`](#insn-004eec80) → [`004eec84`](#insn-004eec84)
- ブロック [`004eec84`](#insn-004eec84) 範囲 `[['004eec84', '004eec9b']]`
  - `UNCONDITIONAL_JUMP` [`004eec98`](#insn-004eec98) → [`004eeca8`](#insn-004eeca8)
- ブロック [`004eec9c`](#insn-004eec9c) 範囲 `[['004eec9c', '004eec9f']]`
  - `CONDITIONAL_JUMP` [`004eec9c`](#insn-004eec9c) → [`004eeca8`](#insn-004eeca8)
  - `FALL_THROUGH` [`004eec9c`](#insn-004eec9c) → [`004eeca0`](#insn-004eeca0)
- ブロック [`004eeca0`](#insn-004eeca0) 範囲 `[['004eeca0', '004eeca7']]`
  - `FALL_THROUGH` [`004eeca4`](#insn-004eeca4) → [`004eeca8`](#insn-004eeca8)
- ブロック [`004eeca8`](#insn-004eeca8) 範囲 `[['004eeca8', '004eecaf']]`
  - `CONDITIONAL_JUMP` [`004eecac`](#insn-004eecac) → [`004eecc0`](#insn-004eecc0)
  - `FALL_THROUGH` [`004eecac`](#insn-004eecac) → [`004eecb0`](#insn-004eecb0)
- ブロック [`004eecb0`](#insn-004eecb0) 範囲 `[['004eecb0', '004eecbf']]`
  - `FALL_THROUGH` [`004eecbc`](#insn-004eecbc) → [`004eecc0`](#insn-004eecc0)
- ブロック [`004eecc0`](#insn-004eecc0) 範囲 `[['004eecc0', '004eed0b']]`
  - `CONDITIONAL_JUMP` [`004eed08`](#insn-004eed08) → [`004eed44`](#insn-004eed44)
  - `FALL_THROUGH` [`004eed08`](#insn-004eed08) → [`004eed0c`](#insn-004eed0c)
- ブロック [`004eed0c`](#insn-004eed0c) 範囲 `[['004eed0c', '004eed1b']]`
  - `CONDITIONAL_JUMP` [`004eed18`](#insn-004eed18) → [`004eed3c`](#insn-004eed3c)
  - `FALL_THROUGH` [`004eed18`](#insn-004eed18) → [`004eed1c`](#insn-004eed1c)
- ブロック [`004eed1c`](#insn-004eed1c) 範囲 `[['004eed1c', '004eed1f']]`
  - `FALL_THROUGH` [`004eed1c`](#insn-004eed1c) → [`004eed20`](#insn-004eed20)
- ブロック [`004eed20`](#insn-004eed20) 範囲 `[['004eed20', '004eed37']]`
  - `CONDITIONAL_JUMP` [`004eed34`](#insn-004eed34) → [`004eed20`](#insn-004eed20)
  - `FALL_THROUGH` [`004eed34`](#insn-004eed34) → [`004eed38`](#insn-004eed38)
- ブロック [`004eed38`](#insn-004eed38) 範囲 `[['004eed38', '004eed3b']]`
  - `FALL_THROUGH` [`004eed38`](#insn-004eed38) → [`004eed3c`](#insn-004eed3c)
- ブロック [`004eed3c`](#insn-004eed3c) 範囲 `[['004eed3c', '004eed43']]`
  - `FALL_THROUGH` [`004eed40`](#insn-004eed40) → [`004eed44`](#insn-004eed44)
- ブロック [`004eed44`](#insn-004eed44) 範囲 `[['004eed44', '004eed4b']]`
  - `CONDITIONAL_JUMP` [`004eed48`](#insn-004eed48) → [`004eed74`](#insn-004eed74)
  - `FALL_THROUGH` [`004eed48`](#insn-004eed48) → [`004eed4c`](#insn-004eed4c)
- ブロック [`004eed4c`](#insn-004eed4c) 範囲 `[['004eed4c', '004eed73']]`
  - `FALL_THROUGH` [`004eed70`](#insn-004eed70) → [`004eed74`](#insn-004eed74)
- ブロック [`004eed74`](#insn-004eed74) 範囲 `[['004eed74', '004eed7b']]`
  - `CONDITIONAL_JUMP` [`004eed78`](#insn-004eed78) → [`004eed84`](#insn-004eed84)
  - `FALL_THROUGH` [`004eed78`](#insn-004eed78) → [`004eed7c`](#insn-004eed7c)
- ブロック [`004eed7c`](#insn-004eed7c) 範囲 `[['004eed7c', '004eed83']]`
  - `FALL_THROUGH` [`004eed80`](#insn-004eed80) → [`004eed84`](#insn-004eed84)
- ブロック [`004eed84`](#insn-004eed84) 範囲 `[['004eed84', '004eed93']]`
  - `CONDITIONAL_JUMP` [`004eed90`](#insn-004eed90) → [`004eede8`](#insn-004eede8)
  - `FALL_THROUGH` [`004eed90`](#insn-004eed90) → [`004eed94`](#insn-004eed94)
- ブロック [`004eed94`](#insn-004eed94) 範囲 `[['004eed94', '004eedaf']]`
- ブロック [`004eede8`](#insn-004eede8) 範囲 `[['004eede8', '004eedeb']]`

## 命令位置別の参照

- [`004eebd0`](#insn-004eebd0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eebd4`](#insn-004eebd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eebd8`](#insn-004eebd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eebdc`](#insn-004eebdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eebe0`](#insn-004eebe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec04`](#insn-004eec04) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec2c`](#insn-004eec2c) → [`00bdc3b0`](../00bdc/00bdc3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdc3b0` · 推定シンボル `None` · 推定型 `None`
- [`004eec34`](#insn-004eec34) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec38`](#insn-004eec38) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec48`](#insn-004eec48) → [`00bdb810`](../00bdb/00bdb810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb810` · 推定シンボル `None` · 推定型 `None`
- [`004eec4c`](#insn-004eec4c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec5c`](#insn-004eec5c) → [`004eec70`](#insn-004eec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec68`](#insn-004eec68) → [`00bdb820`](../00bdb/00bdb820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb820` · 推定シンボル `None` · 推定型 `None`
- [`004eec6c`](#insn-004eec6c) → [`004eecc0`](#insn-004eecc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec70`](#insn-004eec70) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec80`](#insn-004eec80) → [`004eec9c`](#insn-004eec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec90`](#insn-004eec90) → [`0051d614`](../0051d/0051d614.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0051d614` · 推定シンボル `None` · 推定型 `None`
- [`004eec98`](#insn-004eec98) → [`004eeca8`](#insn-004eeca8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eec9c`](#insn-004eec9c) → [`004eeca8`](#insn-004eeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eeca4`](#insn-004eeca4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eecac`](#insn-004eecac) → [`004eecc0`](#insn-004eecc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eecb0`](#insn-004eecb0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eecbc`](#insn-004eecbc) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`004eecd4`](#insn-004eecd4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eecec`](#insn-004eecec) → [`00bdbc90`](../00bdb/00bdbc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdbc90` · 推定シンボル `None` · 推定型 `None`
- [`004eecf4`](#insn-004eecf4) → [`00bdb830`](../00bdb/00bdb830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb830` · 推定シンボル `None` · 推定型 `None`
- [`004eed00`](#insn-004eed00) → [`00483ed8`](../00483/00483ed8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00483ed8` · 推定シンボル `None` · 推定型 `None`
- [`004eed04`](#insn-004eed04) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed08`](#insn-004eed08) → [`004eed44`](#insn-004eed44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed0c`](#insn-004eed0c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed18`](#insn-004eed18) → [`004eed3c`](#insn-004eed3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed2c`](#insn-004eed2c) → [`00512ca8`](../00512/00512ca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00512ca8` · 推定シンボル `None` · 推定型 `None`
- [`004eed34`](#insn-004eed34) → [`004eed20`](#insn-004eed20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed38`](#insn-004eed38) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed3c`](#insn-004eed3c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed40`](#insn-004eed40) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`004eed44`](#insn-004eed44) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed48`](#insn-004eed48) → [`004eed74`](#insn-004eed74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed4c`](#insn-004eed4c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed50`](#insn-004eed50) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed58`](#insn-004eed58) → `00bea728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004eed68`](#insn-004eed68) → [`010a5058`](../010a5/010a5058.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5058` · 推定シンボル `None` · 推定型 `None`
- [`004eed70`](#insn-004eed70) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`004eed74`](#insn-004eed74) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed78`](#insn-004eed78) → [`004eed84`](#insn-004eed84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed7c`](#insn-004eed7c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed80`](#insn-004eed80) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`004eed88`](#insn-004eed88) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed90`](#insn-004eed90) → [`004eede8`](#insn-004eede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed94`](#insn-004eed94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed98`](#insn-004eed98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eed9c`](#insn-004eed9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eeda0`](#insn-004eeda0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eeda4`](#insn-004eeda4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eede8`](#insn-004eede8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004eebd0`](#insn-004eebd0)

~~~json
{
  "source": "004eebd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eebd4`](#insn-004eebd4)

~~~json
{
  "source": "004eebd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eebd8`](#insn-004eebd8)

~~~json
{
  "source": "004eebd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eebdc`](#insn-004eebdc)

~~~json
{
  "source": "004eebdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eebe0`](#insn-004eebe0)

~~~json
{
  "source": "004eebe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec04`](#insn-004eec04)

~~~json
{
  "source": "004eec04",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec2c`](#insn-004eec2c)

~~~json
{
  "source": "004eec2c",
  "target": "00bdc3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eec34`](#insn-004eec34)

~~~json
{
  "source": "004eec34",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec38`](#insn-004eec38)

~~~json
{
  "source": "004eec38",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec48`](#insn-004eec48)

~~~json
{
  "source": "004eec48",
  "target": "00bdb810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eec4c`](#insn-004eec4c)

~~~json
{
  "source": "004eec4c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec5c`](#insn-004eec5c)

~~~json
{
  "source": "004eec5c",
  "target": "004eec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec68`](#insn-004eec68)

~~~json
{
  "source": "004eec68",
  "target": "00bdb820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eec6c`](#insn-004eec6c)

~~~json
{
  "source": "004eec6c",
  "target": "004eecc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec70`](#insn-004eec70)

~~~json
{
  "source": "004eec70",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec80`](#insn-004eec80)

~~~json
{
  "source": "004eec80",
  "target": "004eec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec90`](#insn-004eec90)

~~~json
{
  "source": "004eec90",
  "target": "0051d614",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eec98`](#insn-004eec98)

~~~json
{
  "source": "004eec98",
  "target": "004eeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eec9c`](#insn-004eec9c)

~~~json
{
  "source": "004eec9c",
  "target": "004eeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eeca4`](#insn-004eeca4)

~~~json
{
  "source": "004eeca4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eecac`](#insn-004eecac)

~~~json
{
  "source": "004eecac",
  "target": "004eecc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eecb0`](#insn-004eecb0)

~~~json
{
  "source": "004eecb0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eecbc`](#insn-004eecbc)

~~~json
{
  "source": "004eecbc",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eecd4`](#insn-004eecd4)

~~~json
{
  "source": "004eecd4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eecec`](#insn-004eecec)

~~~json
{
  "source": "004eecec",
  "target": "00bdbc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eecf4`](#insn-004eecf4)

~~~json
{
  "source": "004eecf4",
  "target": "00bdb830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed00`](#insn-004eed00)

~~~json
{
  "source": "004eed00",
  "target": "00483ed8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed04`](#insn-004eed04)

~~~json
{
  "source": "004eed04",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed08`](#insn-004eed08)

~~~json
{
  "source": "004eed08",
  "target": "004eed44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed0c`](#insn-004eed0c)

~~~json
{
  "source": "004eed0c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed18`](#insn-004eed18)

~~~json
{
  "source": "004eed18",
  "target": "004eed3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed2c`](#insn-004eed2c)

~~~json
{
  "source": "004eed2c",
  "target": "00512ca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed34`](#insn-004eed34)

~~~json
{
  "source": "004eed34",
  "target": "004eed20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed38`](#insn-004eed38)

~~~json
{
  "source": "004eed38",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed3c`](#insn-004eed3c)

~~~json
{
  "source": "004eed3c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed40`](#insn-004eed40)

~~~json
{
  "source": "004eed40",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed44`](#insn-004eed44)

~~~json
{
  "source": "004eed44",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed48`](#insn-004eed48)

~~~json
{
  "source": "004eed48",
  "target": "004eed74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed4c`](#insn-004eed4c)

~~~json
{
  "source": "004eed4c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed50`](#insn-004eed50)

~~~json
{
  "source": "004eed50",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed58`](#insn-004eed58)

~~~json
{
  "source": "004eed58",
  "target": "00bea728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bea728",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004eed68`](#insn-004eed68)

~~~json
{
  "source": "004eed68",
  "target": "010a5058",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed70`](#insn-004eed70)

~~~json
{
  "source": "004eed70",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed74`](#insn-004eed74)

~~~json
{
  "source": "004eed74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed78`](#insn-004eed78)

~~~json
{
  "source": "004eed78",
  "target": "004eed84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed7c`](#insn-004eed7c)

~~~json
{
  "source": "004eed7c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed80`](#insn-004eed80)

~~~json
{
  "source": "004eed80",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eed88`](#insn-004eed88)

~~~json
{
  "source": "004eed88",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed90`](#insn-004eed90)

~~~json
{
  "source": "004eed90",
  "target": "004eede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed94`](#insn-004eed94)

~~~json
{
  "source": "004eed94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed98`](#insn-004eed98)

~~~json
{
  "source": "004eed98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eed9c`](#insn-004eed9c)

~~~json
{
  "source": "004eed9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eeda0`](#insn-004eeda0)

~~~json
{
  "source": "004eeda0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eeda4`](#insn-004eeda4)

~~~json
{
  "source": "004eeda4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eede8`](#insn-004eede8)

~~~json
{
  "source": "004eede8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
