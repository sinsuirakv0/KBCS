# 00b0aadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0aba4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0aba4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0002.md#compare-29e670da72a88890e003cbcab97d5eba)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0aadc",
  "name": "_ZN11flatbuffers10IDLOptionsC2ERKS0_",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2cb362fc9843e7c5ee3d6e91264b59b4ee1a053a159e27c025205c54adbab5c",
  "source_text_sha256": "a2cb362fc9843e7c5ee3d6e91264b59b4ee1a053a159e27c025205c54adbab5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0aadc",
        "00b0ac77"
      ]
    ],
    "bytes_sha256": "97dca154b727dac788098f3914e5d612786c3bd770fe4600777c224ea2428a9f",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde900](../00bde/00bde900.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde630](../00bde/00bde630.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3480 bytes

~~~c

void _ZN11flatbuffers10IDLOptionsC2ERKS0_(undefined8 *param_1,undefined8 *param_2)

{
  long lVar1;
  undefined4 uVar2;
  undefined1 uVar3;
  undefined2 uVar4;
  long lVar5;
  long lVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  undefined8 uVar9;
  
  uVar7 = *(undefined8 *)((long)param_2 + 9);
  uVar9 = param_2[1];
  uVar8 = *param_2;
  *(undefined8 *)((long)param_1 + 0x11) = *(undefined8 *)((long)param_2 + 0x11);
  *(undefined8 *)((long)param_1 + 9) = uVar7;
  param_1[1] = uVar9;
  *param_1 = uVar8;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 4,param_2 + 4);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 7,param_2 + 7);
  *(undefined4 *)(param_1 + 10) = *(undefined4 *)(param_2 + 10);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0xb,param_2 + 0xb);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0xe,param_2 + 0xe);
  uVar4 = *(undefined2 *)(param_2 + 0x11);
  *(undefined1 *)((long)param_1 + 0x8a) = *(undefined1 *)((long)param_2 + 0x8a);
  *(undefined2 *)(param_1 + 0x11) = uVar4;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x12,param_2 + 0x12);
  uVar2 = *(undefined4 *)(param_2 + 0x15);
  *(undefined1 *)((long)param_1 + 0xac) = *(undefined1 *)((long)param_2 + 0xac);
  *(undefined4 *)(param_1 + 0x15) = uVar2;
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x16,param_2 + 0x16);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x19,param_2 + 0x19);
  *(undefined4 *)(param_1 + 0x1c) = *(undefined4 *)(param_2 + 0x1c);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x1d,param_2 + 0x1d);
  uVar4 = *(undefined2 *)(param_2 + 0x20);
  uVar3 = *(undefined1 *)((long)param_2 + 0x102);
  param_1[0x22] = 0;
  param_1[0x23] = 0;
  param_1[0x21] = 0;
  *(undefined2 *)(param_1 + 0x20) = uVar4;
  *(undefined1 *)((long)param_1 + 0x102) = uVar3;
  if (param_2[0x22] - param_2[0x21] != 0) {
    lVar6 = (long)(param_2[0x22] - param_2[0x21]) >> 3;
    if (0xaaaaaaaaaaaaaaa < (ulong)(lVar6 * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar5 = _Znwm();
    param_1[0x21] = lVar5;
    param_1[0x22] = lVar5;
    param_1[0x23] = lVar5 + lVar6 * 8;
    lVar1 = param_2[0x22];
    for (lVar6 = param_2[0x21]; lVar6 != lVar1; lVar6 = lVar6 + 0x18) {
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(lVar5,lVar6);
      lVar5 = lVar5 + 0x18;
    }
    param_1[0x22] = lVar5;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x24,param_2 + 0x24);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x27,param_2 + 0x27);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x2a,param_2 + 0x2a);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_
            (param_1 + 0x2d,param_2 + 0x2d);
  uVar8 = param_2[0x31];
  uVar7 = param_2[0x30];
  *(undefined2 *)(param_1 + 0x32) = *(undefined2 *)(param_2 + 0x32);
  param_1[0x31] = uVar8;
  param_1[0x30] = uVar7;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0aadc"></a> `00b0aadc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b0aae0"></a> `00b0aae0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0aae4"></a> `00b0aae4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0aae8"></a> `00b0aae8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0aaec"></a> `00b0aaec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b0aaf0"></a> `00b0aaf0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b0aaf4"></a> `00b0aaf4` | `20 90 c0 3c` | ldur q0,[x1, #0x9] | `FALL_THROUGH`
<a id="insn-00b0aaf8"></a> `00b0aaf8` | `21 04 c2 3c` | ldr q1,[x1], #0x20 | `FALL_THROUGH`
<a id="insn-00b0aafc"></a> `00b0aafc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0ab00"></a> `00b0ab00` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00b0ab04"></a> `00b0ab04` | `60 92 80 3c` | stur q0,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00b0ab08"></a> `00b0ab08` | `61 02 80 3d` | str q1,[x19] | `FALL_THROUGH`
<a id="insn-00b0ab0c"></a> `00b0ab0c` | `c9 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab10"></a> `00b0ab10` | `60 e2 00 91` | add x0,x19,#0x38 | `FALL_THROUGH`
<a id="insn-00b0ab14"></a> `00b0ab14` | `81 e2 00 91` | add x1,x20,#0x38 | `FALL_THROUGH`
<a id="insn-00b0ab18"></a> `00b0ab18` | `c6 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab1c"></a> `00b0ab1c` | `88 52 40 b9` | ldr w8,[x20, #0x50] | `FALL_THROUGH`
<a id="insn-00b0ab20"></a> `00b0ab20` | `60 62 01 91` | add x0,x19,#0x58 | `FALL_THROUGH`
<a id="insn-00b0ab24"></a> `00b0ab24` | `81 62 01 91` | add x1,x20,#0x58 | `FALL_THROUGH`
<a id="insn-00b0ab28"></a> `00b0ab28` | `68 52 00 b9` | str w8,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b0ab2c"></a> `00b0ab2c` | `c1 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab30"></a> `00b0ab30` | `60 c2 01 91` | add x0,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00b0ab34"></a> `00b0ab34` | `81 c2 01 91` | add x1,x20,#0x70 | `FALL_THROUGH`
<a id="insn-00b0ab38"></a> `00b0ab38` | `be 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab3c"></a> `00b0ab3c` | `88 2a 42 39` | ldrb w8,[x20, #0x8a] | `FALL_THROUGH`
<a id="insn-00b0ab40"></a> `00b0ab40` | `89 12 41 79` | ldrh w9,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00b0ab44"></a> `00b0ab44` | `60 42 02 91` | add x0,x19,#0x90 | `FALL_THROUGH`
<a id="insn-00b0ab48"></a> `00b0ab48` | `81 42 02 91` | add x1,x20,#0x90 | `FALL_THROUGH`
<a id="insn-00b0ab4c"></a> `00b0ab4c` | `68 2a 02 39` | strb w8,[x19, #0x8a] | `FALL_THROUGH`
<a id="insn-00b0ab50"></a> `00b0ab50` | `69 12 01 79` | strh w9,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00b0ab54"></a> `00b0ab54` | `b7 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab58"></a> `00b0ab58` | `88 b2 42 39` | ldrb w8,[x20, #0xac] | `FALL_THROUGH`
<a id="insn-00b0ab5c"></a> `00b0ab5c` | `89 aa 40 b9` | ldr w9,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-00b0ab60"></a> `00b0ab60` | `60 c2 02 91` | add x0,x19,#0xb0 | `FALL_THROUGH`
<a id="insn-00b0ab64"></a> `00b0ab64` | `81 c2 02 91` | add x1,x20,#0xb0 | `FALL_THROUGH`
<a id="insn-00b0ab68"></a> `00b0ab68` | `68 b2 02 39` | strb w8,[x19, #0xac] | `FALL_THROUGH`
<a id="insn-00b0ab6c"></a> `00b0ab6c` | `69 aa 00 b9` | str w9,[x19, #0xa8] | `FALL_THROUGH`
<a id="insn-00b0ab70"></a> `00b0ab70` | `b0 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab74"></a> `00b0ab74` | `60 22 03 91` | add x0,x19,#0xc8 | `FALL_THROUGH`
<a id="insn-00b0ab78"></a> `00b0ab78` | `81 22 03 91` | add x1,x20,#0xc8 | `FALL_THROUGH`
<a id="insn-00b0ab7c"></a> `00b0ab7c` | `ad 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab80"></a> `00b0ab80` | `88 e2 40 b9` | ldr w8,[x20, #0xe0] | `FALL_THROUGH`
<a id="insn-00b0ab84"></a> `00b0ab84` | `60 a2 03 91` | add x0,x19,#0xe8 | `FALL_THROUGH`
<a id="insn-00b0ab88"></a> `00b0ab88` | `81 a2 03 91` | add x1,x20,#0xe8 | `FALL_THROUGH`
<a id="insn-00b0ab8c"></a> `00b0ab8c` | `68 e2 00 b9` | str w8,[x19, #0xe0] | `FALL_THROUGH`
<a id="insn-00b0ab90"></a> `00b0ab90` | `a8 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ab94"></a> `00b0ab94` | `88 02 42 79` | ldrh w8,[x20, #0x100] | `FALL_THROUGH`
<a id="insn-00b0ab98"></a> `00b0ab98` | `89 0a 44 39` | ldrb w9,[x20, #0x102] | `FALL_THROUGH`
<a id="insn-00b0ab9c"></a> `00b0ab9c` | `7f 7e 11 a9` | stp xzr,xzr,[x19, #0x110] | `FALL_THROUGH`
<a id="insn-00b0aba0"></a> `00b0aba0` | `7f 86 00 f9` | str xzr,[x19, #0x108] | `FALL_THROUGH`
<a id="insn-00b0aba4"></a> `00b0aba4` | `68 02 02 79` | strh w8,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-00b0aba8"></a> `00b0aba8` | `69 0a 04 39` | strb w9,[x19, #0x102] | `FALL_THROUGH`
<a id="insn-00b0abac"></a> `00b0abac` | `88 a6 50 a9` | ldp x8,x9,[x20, #0x108] | `FALL_THROUGH`
<a id="insn-00b0abb0"></a> `00b0abb0` | `20 01 08 eb` | subs x0,x9,x8 | `FALL_THROUGH`
<a id="insn-00b0abb4"></a> `00b0abb4` | `60 03 00 54` | b.eq 0x00b0ac20 | `CONDITIONAL_JUMP`
<a id="insn-00b0abb8"></a> `00b0abb8` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b0abbc"></a> `00b0abbc` | `08 fc 43 93` | asr x8,x0,#0x3 | `FALL_THROUGH`
<a id="insn-00b0abc0"></a> `00b0abc0` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00b0abc4"></a> `00b0abc4` | `16 7d 09 9b` | mul x22,x8,x9 | `FALL_THROUGH`
<a id="insn-00b0abc8"></a> `00b0abc8` | `e8 f3 01 b2` | orr x8,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00b0abcc"></a> `00b0abcc` | `68 55 95 f2` | movk x8,#0xaaab | `FALL_THROUGH`
<a id="insn-00b0abd0"></a> `00b0abd0` | `48 55 e1 f2` | movk x8,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00b0abd4"></a> `00b0abd4` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00b0abd8"></a> `00b0abd8` | `e2 04 00 54` | b.cs 0x00b0ac74 | `CONDITIONAL_JUMP`
<a id="insn-00b0abdc"></a> `00b0abdc` | `d9 40 03 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b0abe0"></a> `00b0abe0` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00b0abe4"></a> `00b0abe4` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00b0abe8"></a> `00b0abe8` | `60 82 10 a9` | stp x0,x0,[x19, #0x108] | `FALL_THROUGH`
<a id="insn-00b0abec"></a> `00b0abec` | `68 8e 00 f9` | str x8,[x19, #0x118] | `FALL_THROUGH`
<a id="insn-00b0abf0"></a> `00b0abf0` | `96 de 50 a9` | ldp x22,x23,[x20, #0x108] | `FALL_THROUGH`
<a id="insn-00b0abf4"></a> `00b0abf4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b0abf8"></a> `00b0abf8` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-00b0abfc"></a> `00b0abfc` | `00 01 00 54` | b.eq 0x00b0ac1c | `CONDITIONAL_JUMP`
<a id="insn-00b0ac00"></a> `00b0ac00` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b0ac04"></a> `00b0ac04` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b0ac08"></a> `00b0ac08` | `8a 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ac0c"></a> `00b0ac0c` | `d6 62 00 91` | add x22,x22,#0x18 | `FALL_THROUGH`
<a id="insn-00b0ac10"></a> `00b0ac10` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00b0ac14"></a> `00b0ac14` | `b5 62 00 91` | add x21,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00b0ac18"></a> `00b0ac18` | `41 ff ff 54` | b.ne 0x00b0ac00 | `CONDITIONAL_JUMP`
<a id="insn-00b0ac1c"></a> `00b0ac1c` | `75 8a 00 f9` | str x21,[x19, #0x110] | `FALL_THROUGH`
<a id="insn-00b0ac20"></a> `00b0ac20` | `60 82 04 91` | add x0,x19,#0x120 | `FALL_THROUGH`
<a id="insn-00b0ac24"></a> `00b0ac24` | `81 82 04 91` | add x1,x20,#0x120 | `FALL_THROUGH`
<a id="insn-00b0ac28"></a> `00b0ac28` | `82 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ac2c"></a> `00b0ac2c` | `60 e2 04 91` | add x0,x19,#0x138 | `FALL_THROUGH`
<a id="insn-00b0ac30"></a> `00b0ac30` | `81 e2 04 91` | add x1,x20,#0x138 | `FALL_THROUGH`
<a id="insn-00b0ac34"></a> `00b0ac34` | `7f 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ac38"></a> `00b0ac38` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00b0ac3c"></a> `00b0ac3c` | `81 42 05 91` | add x1,x20,#0x150 | `FALL_THROUGH`
<a id="insn-00b0ac40"></a> `00b0ac40` | `7c 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ac44"></a> `00b0ac44` | `60 a2 05 91` | add x0,x19,#0x168 | `FALL_THROUGH`
<a id="insn-00b0ac48"></a> `00b0ac48` | `81 a2 05 91` | add x1,x20,#0x168 | `FALL_THROUGH`
<a id="insn-00b0ac4c"></a> `00b0ac4c` | `79 4e 03 94` | bl 0x00bde630 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ac50"></a> `00b0ac50` | `88 22 43 79` | ldrh w8,[x20, #0x190] | `FALL_THROUGH`
<a id="insn-00b0ac54"></a> `00b0ac54` | `80 62 c0 3d` | ldr q0,[x20, #0x180] | `FALL_THROUGH`
<a id="insn-00b0ac58"></a> `00b0ac58` | `68 22 03 79` | strh w8,[x19, #0x190] | `FALL_THROUGH`
<a id="insn-00b0ac5c"></a> `00b0ac5c` | `60 62 80 3d` | str q0,[x19, #0x180] | `FALL_THROUGH`
<a id="insn-00b0ac60"></a> `00b0ac60` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0ac64"></a> `00b0ac64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ac68"></a> `00b0ac68` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ac6c"></a> `00b0ac6c` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b0ac70"></a> `00b0ac70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0ac74"></a> `00b0ac74` | `53 4d 03 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0aadc`](#insn-00b0aadc) 範囲 `[['00b0aadc', '00b0abb7']]`
  - `CONDITIONAL_JUMP` [`00b0abb4`](#insn-00b0abb4) → [`00b0ac20`](#insn-00b0ac20)
  - `FALL_THROUGH` [`00b0abb4`](#insn-00b0abb4) → [`00b0abb8`](#insn-00b0abb8)
- ブロック [`00b0abb8`](#insn-00b0abb8) 範囲 `[['00b0abb8', '00b0abdb']]`
  - `CONDITIONAL_JUMP` [`00b0abd8`](#insn-00b0abd8) → [`00b0ac74`](#insn-00b0ac74)
  - `FALL_THROUGH` [`00b0abd8`](#insn-00b0abd8) → [`00b0abdc`](#insn-00b0abdc)
- ブロック [`00b0abdc`](#insn-00b0abdc) 範囲 `[['00b0abdc', '00b0abff']]`
  - `CONDITIONAL_JUMP` [`00b0abfc`](#insn-00b0abfc) → [`00b0ac1c`](#insn-00b0ac1c)
  - `FALL_THROUGH` [`00b0abfc`](#insn-00b0abfc) → [`00b0ac00`](#insn-00b0ac00)
- ブロック [`00b0ac00`](#insn-00b0ac00) 範囲 `[['00b0ac00', '00b0ac1b']]`
  - `CONDITIONAL_JUMP` [`00b0ac18`](#insn-00b0ac18) → [`00b0ac00`](#insn-00b0ac00)
  - `FALL_THROUGH` [`00b0ac18`](#insn-00b0ac18) → [`00b0ac1c`](#insn-00b0ac1c)
- ブロック [`00b0ac1c`](#insn-00b0ac1c) 範囲 `[['00b0ac1c', '00b0ac1f']]`
  - `FALL_THROUGH` [`00b0ac1c`](#insn-00b0ac1c) → [`00b0ac20`](#insn-00b0ac20)
- ブロック [`00b0ac20`](#insn-00b0ac20) 範囲 `[['00b0ac20', '00b0ac73']]`
- ブロック [`00b0ac74`](#insn-00b0ac74) 範囲 `[['00b0ac74', '00b0ac77']]`

## 命令位置別の参照

- [`00b0aadc`](#insn-00b0aadc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0aae0`](#insn-00b0aae0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0aae4`](#insn-00b0aae4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0aae8`](#insn-00b0aae8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab0c`](#insn-00b0ab0c) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab18`](#insn-00b0ab18) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab2c`](#insn-00b0ab2c) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab38`](#insn-00b0ab38) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab54`](#insn-00b0ab54) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab70`](#insn-00b0ab70) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab7c`](#insn-00b0ab7c) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ab90`](#insn-00b0ab90) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0abb4`](#insn-00b0abb4) → [`00b0ac20`](#insn-00b0ac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0abd8`](#insn-00b0abd8) → [`00b0ac74`](#insn-00b0ac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0abdc`](#insn-00b0abdc) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b0abfc`](#insn-00b0abfc) → [`00b0ac1c`](#insn-00b0ac1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac08`](#insn-00b0ac08) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac18`](#insn-00b0ac18) → [`00b0ac00`](#insn-00b0ac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac28`](#insn-00b0ac28) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac34`](#insn-00b0ac34) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac40`](#insn-00b0ac40) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac4c`](#insn-00b0ac4c) → [`00bde630`](../00bde/00bde630.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde630` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac60`](#insn-00b0ac60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac64`](#insn-00b0ac64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac68`](#insn-00b0ac68) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ac74`](#insn-00b0ac74) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0aadc`](#insn-00b0aadc)

~~~json
{
  "source": "00b0aadc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0aae0`](#insn-00b0aae0)

~~~json
{
  "source": "00b0aae0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0aae4`](#insn-00b0aae4)

~~~json
{
  "source": "00b0aae4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0aae8`](#insn-00b0aae8)

~~~json
{
  "source": "00b0aae8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ab0c`](#insn-00b0ab0c)

~~~json
{
  "source": "00b0ab0c",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab18`](#insn-00b0ab18)

~~~json
{
  "source": "00b0ab18",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab2c`](#insn-00b0ab2c)

~~~json
{
  "source": "00b0ab2c",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab38`](#insn-00b0ab38)

~~~json
{
  "source": "00b0ab38",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab54`](#insn-00b0ab54)

~~~json
{
  "source": "00b0ab54",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab70`](#insn-00b0ab70)

~~~json
{
  "source": "00b0ab70",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab7c`](#insn-00b0ab7c)

~~~json
{
  "source": "00b0ab7c",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ab90`](#insn-00b0ab90)

~~~json
{
  "source": "00b0ab90",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0abb4`](#insn-00b0abb4)

~~~json
{
  "source": "00b0abb4",
  "target": "00b0ac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0abd8`](#insn-00b0abd8)

~~~json
{
  "source": "00b0abd8",
  "target": "00b0ac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0abdc`](#insn-00b0abdc)

~~~json
{
  "source": "00b0abdc",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0abfc`](#insn-00b0abfc)

~~~json
{
  "source": "00b0abfc",
  "target": "00b0ac1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ac08`](#insn-00b0ac08)

~~~json
{
  "source": "00b0ac08",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ac18`](#insn-00b0ac18)

~~~json
{
  "source": "00b0ac18",
  "target": "00b0ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ac28`](#insn-00b0ac28)

~~~json
{
  "source": "00b0ac28",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ac34`](#insn-00b0ac34)

~~~json
{
  "source": "00b0ac34",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ac40`](#insn-00b0ac40)

~~~json
{
  "source": "00b0ac40",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ac4c`](#insn-00b0ac4c)

~~~json
{
  "source": "00b0ac4c",
  "target": "00bde630",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0ac60`](#insn-00b0ac60)

~~~json
{
  "source": "00b0ac60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ac64`](#insn-00b0ac64)

~~~json
{
  "source": "00b0ac64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ac68`](#insn-00b0ac68)

~~~json
{
  "source": "00b0ac68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ac74`](#insn-00b0ac74)

~~~json
{
  "source": "00b0ac74",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
