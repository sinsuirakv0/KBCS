# 00bdafb8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdab90`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bdab90.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-caab69e68c2adabf0245ede7255c22ae)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdb054`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdb054.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-ce965b8d02b71b24c11f49b8e145b863)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafb8",
  "name": "_ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff09e9dc10e55673ab4e84ab23ad0be64e7804f82d52baf166339cad6aafe459",
  "source_text_sha256": "ff09e9dc10e55673ab4e84ab23ad0be64e7804f82d52baf166339cad6aafe459",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafb8",
        "00bdb133"
      ]
    ],
    "bytes_sha256": "4b4807dd091f55b5a9064d4bac2963f084ae07fc9a37fba8f455bb4f2db92ebd",
    "instruction_count": 95,
    "instruction_bytes": 380,
    "body_bytes": 380,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aba0](../00c5a/00c5aba0.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b260](../00c5b/00c5b260.md)
- [00c5db30](../00c5d/00c5db30.md)
- [00c5db40](../00c5d/00c5db40.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"verification_id && verification_code"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1711 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_
               (undefined8 param_1,undefined8 *param_2,long param_3,long param_4)

{
  long *plVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  long lVar4;
  ulong uVar5;
  long lVar6;
  char *pcVar7;
  
  if ((param_3 == 0) || (param_4 == 0)) {
    pcVar7 = "verification_id && verification_code";
  }
  else {
    if (DAT_01126cf8 != '\0') {
      plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)*param_2);
      uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_3);
      uVar3 = (**(code **)(*plVar1 + 0x538))(plVar1,param_4);
      lVar4 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar1,DAT_01126bd0,DAT_01126be8,uVar2,uVar3);
      uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
      (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
      (**(code **)(*plVar1 + 0xb8))(plVar1,uVar3);
      uVar2 = 0;
      if (((uVar5 & 1) == 0) && (lVar4 != 0)) {
        lVar6 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar6 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar6);
        uVar2 = (**(code **)(*plVar1 + 0xa8))(plVar1,lVar4);
        (**(code **)(*plVar1 + 0xb8))(plVar1,lVar4);
      }
      _ZN8firebase4auth19PhoneAuthCredentialC2EPv(param_1,uVar2);
      return;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar7 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar7);
  _ZN8firebase4auth19PhoneAuthCredentialC1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafb8"></a> `00bdafb8` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bdafbc"></a> `00bdafbc` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdafc0"></a> `00bdafc0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdafc4"></a> `00bdafc4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdafc8"></a> `00bdafc8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdafcc"></a> `00bdafcc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdafd0"></a> `00bdafd0` | `41 09 00 b4` | cbz x1,0x00bdb0f8 | `CONDITIONAL_JUMP`
<a id="insn-00bdafd4"></a> `00bdafd4` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bdafd8"></a> `00bdafd8` | `02 09 00 b4` | cbz x2,0x00bdb0f8 | `CONDITIONAL_JUMP`
<a id="insn-00bdafdc"></a> `00bdafdc` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdafe0"></a> `00bdafe0` | `08 e1 73 39` | ldrb w8,[x8, #0xcf8] | `FALL_THROUGH`
<a id="insn-00bdafe4"></a> `00bdafe4` | `08 09 00 34` | cbz w8,0x00bdb104 | `CONDITIONAL_JUMP`
<a id="insn-00bdafe8"></a> `00bdafe8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdafec"></a> `00bdafec` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdaff0"></a> `00bdaff0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bdaff4"></a> `00bdaff4` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bdaff8"></a> `00bdaff8` | `22 00 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaffc"></a> `00bdaffc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdb000"></a> `00bdb000` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdb004"></a> `00bdb004` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdb008"></a> `00bdb008` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdb00c"></a> `00bdb00c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb010"></a> `00bdb010` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdb014"></a> `00bdb014` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdb018"></a> `00bdb018` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb01c"></a> `00bdb01c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdb020"></a> `00bdb020` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdb024"></a> `00bdb024` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb028"></a> `00bdb028` | `48 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdb02c"></a> `00bdb02c` | `49 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdb030"></a> `00bdb030` | `01 e9 45 f9` | ldr x1,[x8, #0xbd0] | `FALL_THROUGH`
<a id="insn-00bdb034"></a> `00bdb034` | `22 f5 45 f9` | ldr x2,[x9, #0xbe8] | `FALL_THROUGH`
<a id="insn-00bdb038"></a> `00bdb038` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdb03c"></a> `00bdb03c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb040"></a> `00bdb040` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bdb044"></a> `00bdb044` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdb048"></a> `00bdb048` | `d6 fe 01 94` | bl 0x00c5aba0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb04c"></a> `00bdb04c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdb050"></a> `00bdb050` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb054"></a> `00bdb054` | `c3 ff 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb058"></a> `00bdb058` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdb05c"></a> `00bdb05c` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00bdb060"></a> `00bdb060` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb064"></a> `00bdb064` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdb068"></a> `00bdb068` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdb06c"></a> `00bdb06c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb070"></a> `00bdb070` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdb074"></a> `00bdb074` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb078"></a> `00bdb078` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdb07c"></a> `00bdb07c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdb080"></a> `00bdb080` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb084"></a> `00bdb084` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdb088"></a> `00bdb088` | `b8 02 00 37` | tbnz w24,#0x0,0x00bdb0dc | `CONDITIONAL_JUMP`
<a id="insn-00bdb08c"></a> `00bdb08c` | `94 02 00 b4` | cbz x20,0x00bdb0dc | `CONDITIONAL_JUMP`
<a id="insn-00bdb090"></a> `00bdb090` | `74 00 02 94` | bl 0x00c5b260 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb094"></a> `00bdb094` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdb098"></a> `00bdb098` | `80 00 00 b5` | cbnz x0,0x00bdb0a8 | `CONDITIONAL_JUMP`
<a id="insn-00bdb09c"></a> `00bdb09c` | `a0 b6 ff f0` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdb0a0"></a> `00bdb0a0` | `00 60 17 91` | add x0,x0,#0x5d8 | `FALL_THROUGH`
<a id="insn-00bdb0a4"></a> `00bdb0a4` | `d7 ff 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb0a8"></a> `00bdb0a8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdb0ac"></a> `00bdb0ac` | `f5 ff 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb0b0"></a> `00bdb0b0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdb0b4"></a> `00bdb0b4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdb0b8"></a> `00bdb0b8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdb0bc"></a> `00bdb0bc` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdb0c0"></a> `00bdb0c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb0c4"></a> `00bdb0c4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdb0c8"></a> `00bdb0c8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdb0cc"></a> `00bdb0cc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdb0d0"></a> `00bdb0d0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdb0d4"></a> `00bdb0d4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdb0d8"></a> `00bdb0d8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdb0dc"></a> `00bdb0dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdb0e0"></a> `00bdb0e0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdb0e4"></a> `00bdb0e4` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdb0e8"></a> `00bdb0e8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdb0ec"></a> `00bdb0ec` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdb0f0"></a> `00bdb0f0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdb0f4"></a> `00bdb0f4` | `8f 0a 02 14` | b 0x00c5db30 | `CALL_TERMINATOR`
<a id="insn-00bdb0f8"></a> `00bdb0f8` | `20 b6 ff 90` | adrp x0,0x29f000 | `FALL_THROUGH`
<a id="insn-00bdb0fc"></a> `00bdb0fc` | `00 20 34 91` | add x0,x0,#0xd08 | `FALL_THROUGH`
<a id="insn-00bdb100"></a> `00bdb100` | `06 00 00 14` | b 0x00bdb118 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdb104"></a> `00bdb104` | `e0 b6 ff 90` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bdb108"></a> `00bdb108` | `00 40 38 91` | add x0,x0,#0xe10 | `FALL_THROUGH`
<a id="insn-00bdb10c"></a> `00bdb10c` | `e5 fe 01 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb110"></a> `00bdb110` | `a0 b9 ff b0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bdb114"></a> `00bdb114` | `00 c0 03 91` | add x0,x0,#0xf0 | `FALL_THROUGH`
<a id="insn-00bdb118"></a> `00bdb118` | `ba ff 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdb11c"></a> `00bdb11c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdb120"></a> `00bdb120` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdb124"></a> `00bdb124` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdb128"></a> `00bdb128` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdb12c"></a> `00bdb12c` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdb130"></a> `00bdb130` | `84 0a 02 14` | b 0x00c5db40 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafb8`](#insn-00bdafb8) 範囲 `[['00bdafb8', '00bdafd3']]`
  - `CONDITIONAL_JUMP` [`00bdafd0`](#insn-00bdafd0) → [`00bdb0f8`](#insn-00bdb0f8)
  - `FALL_THROUGH` [`00bdafd0`](#insn-00bdafd0) → [`00bdafd4`](#insn-00bdafd4)
- ブロック [`00bdafd4`](#insn-00bdafd4) 範囲 `[['00bdafd4', '00bdafdb']]`
  - `CONDITIONAL_JUMP` [`00bdafd8`](#insn-00bdafd8) → [`00bdb0f8`](#insn-00bdb0f8)
  - `FALL_THROUGH` [`00bdafd8`](#insn-00bdafd8) → [`00bdafdc`](#insn-00bdafdc)
- ブロック [`00bdafdc`](#insn-00bdafdc) 範囲 `[['00bdafdc', '00bdafe7']]`
  - `CONDITIONAL_JUMP` [`00bdafe4`](#insn-00bdafe4) → [`00bdb104`](#insn-00bdb104)
  - `FALL_THROUGH` [`00bdafe4`](#insn-00bdafe4) → [`00bdafe8`](#insn-00bdafe8)
- ブロック [`00bdafe8`](#insn-00bdafe8) 範囲 `[['00bdafe8', '00bdb08b']]`
  - `CONDITIONAL_JUMP` [`00bdb088`](#insn-00bdb088) → [`00bdb0dc`](#insn-00bdb0dc)
  - `FALL_THROUGH` [`00bdb088`](#insn-00bdb088) → [`00bdb08c`](#insn-00bdb08c)
- ブロック [`00bdb08c`](#insn-00bdb08c) 範囲 `[['00bdb08c', '00bdb08f']]`
  - `CONDITIONAL_JUMP` [`00bdb08c`](#insn-00bdb08c) → [`00bdb0dc`](#insn-00bdb0dc)
  - `FALL_THROUGH` [`00bdb08c`](#insn-00bdb08c) → [`00bdb090`](#insn-00bdb090)
- ブロック [`00bdb090`](#insn-00bdb090) 範囲 `[['00bdb090', '00bdb09b']]`
  - `CONDITIONAL_JUMP` [`00bdb098`](#insn-00bdb098) → [`00bdb0a8`](#insn-00bdb0a8)
  - `FALL_THROUGH` [`00bdb098`](#insn-00bdb098) → [`00bdb09c`](#insn-00bdb09c)
- ブロック [`00bdb09c`](#insn-00bdb09c) 範囲 `[['00bdb09c', '00bdb0a7']]`
  - `FALL_THROUGH` [`00bdb0a4`](#insn-00bdb0a4) → [`00bdb0a8`](#insn-00bdb0a8)
- ブロック [`00bdb0a8`](#insn-00bdb0a8) 範囲 `[['00bdb0a8', '00bdb0db']]`
  - `FALL_THROUGH` [`00bdb0d8`](#insn-00bdb0d8) → [`00bdb0dc`](#insn-00bdb0dc)
- ブロック [`00bdb0dc`](#insn-00bdb0dc) 範囲 `[['00bdb0dc', '00bdb0f7']]`
- ブロック [`00bdb0f8`](#insn-00bdb0f8) 範囲 `[['00bdb0f8', '00bdb103']]`
  - `UNCONDITIONAL_JUMP` [`00bdb100`](#insn-00bdb100) → [`00bdb118`](#insn-00bdb118)
- ブロック [`00bdb104`](#insn-00bdb104) 範囲 `[['00bdb104', '00bdb117']]`
  - `FALL_THROUGH` [`00bdb114`](#insn-00bdb114) → [`00bdb118`](#insn-00bdb118)
- ブロック [`00bdb118`](#insn-00bdb118) 範囲 `[['00bdb118', '00bdb133']]`

## 命令位置別の参照

- [`00bdafb8`](#insn-00bdafb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafbc`](#insn-00bdafbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafc0`](#insn-00bdafc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafc4`](#insn-00bdafc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafd0`](#insn-00bdafd0) → [`00bdb0f8`](#insn-00bdb0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafd8`](#insn-00bdafd8) → [`00bdb0f8`](#insn-00bdb0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdafe0`](#insn-00bdafe0) → `01126cf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdafe4`](#insn-00bdafe4) → [`00bdb104`](#insn-00bdb104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaff8`](#insn-00bdaff8) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdb030`](#insn-00bdb030) → `01126bd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdb034`](#insn-00bdb034) → `01126be8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdb048`](#insn-00bdb048) → [`00c5aba0`](../00c5a/00c5aba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aba0` · 推定シンボル `None` · 推定型 `None`
- [`00bdb054`](#insn-00bdb054) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdb088`](#insn-00bdb088) → [`00bdb0dc`](#insn-00bdb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb08c`](#insn-00bdb08c) → [`00bdb0dc`](#insn-00bdb0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb090`](#insn-00bdb090) → [`00c5b260`](../00c5b/00c5b260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b260` · 推定シンボル `None` · 推定型 `None`
- [`00bdb098`](#insn-00bdb098) → [`00bdb0a8`](#insn-00bdb0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0a0`](#insn-00bdb0a0) → `002b25d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdb0a4`](#insn-00bdb0a4) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0ac`](#insn-00bdb0ac) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0e4`](#insn-00bdb0e4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0e8`](#insn-00bdb0e8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0ec`](#insn-00bdb0ec) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0f4`](#insn-00bdb0f4) → [`00c5db30`](../00c5d/00c5db30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db30` · 推定シンボル `None` · 推定型 `None`
- [`00bdb0fc`](#insn-00bdb0fc) → `0029fd08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdb100`](#insn-00bdb100) → [`00bdb118`](#insn-00bdb118) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb108`](#insn-00bdb108) → `002b7e10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdb10c`](#insn-00bdb10c) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00bdb114`](#insn-00bdb114) → `003100f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdb118`](#insn-00bdb118) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bdb120`](#insn-00bdb120) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb124`](#insn-00bdb124) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb128`](#insn-00bdb128) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdb130`](#insn-00bdb130) → [`00c5db40`](../00c5d/00c5db40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5db40` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafb8`](#insn-00bdafb8)

~~~json
{
  "source": "00bdafb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafbc`](#insn-00bdafbc)

~~~json
{
  "source": "00bdafbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafc0`](#insn-00bdafc0)

~~~json
{
  "source": "00bdafc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafc4`](#insn-00bdafc4)

~~~json
{
  "source": "00bdafc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafd0`](#insn-00bdafd0)

~~~json
{
  "source": "00bdafd0",
  "target": "00bdb0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafd8`](#insn-00bdafd8)

~~~json
{
  "source": "00bdafd8",
  "target": "00bdb0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdafe0`](#insn-00bdafe0)

~~~json
{
  "source": "00bdafe0",
  "target": "01126cf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126cf8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdafe4`](#insn-00bdafe4)

~~~json
{
  "source": "00bdafe4",
  "target": "00bdb104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaff8`](#insn-00bdaff8)

~~~json
{
  "source": "00bdaff8",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb030`](#insn-00bdb030)

~~~json
{
  "source": "00bdb030",
  "target": "01126bd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126bd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdb034`](#insn-00bdb034)

~~~json
{
  "source": "00bdb034",
  "target": "01126be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdb048`](#insn-00bdb048)

~~~json
{
  "source": "00bdb048",
  "target": "00c5aba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb054`](#insn-00bdb054)

~~~json
{
  "source": "00bdb054",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb088`](#insn-00bdb088)

~~~json
{
  "source": "00bdb088",
  "target": "00bdb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb08c`](#insn-00bdb08c)

~~~json
{
  "source": "00bdb08c",
  "target": "00bdb0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb090`](#insn-00bdb090)

~~~json
{
  "source": "00bdb090",
  "target": "00c5b260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb098`](#insn-00bdb098)

~~~json
{
  "source": "00bdb098",
  "target": "00bdb0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb0a0`](#insn-00bdb0a0)

~~~json
{
  "source": "00bdb0a0",
  "target": "002b25d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b25d8",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b25d8",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdb0a4`](#insn-00bdb0a4)

~~~json
{
  "source": "00bdb0a4",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb0ac`](#insn-00bdb0ac)

~~~json
{
  "source": "00bdb0ac",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb0e4`](#insn-00bdb0e4)

~~~json
{
  "source": "00bdb0e4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb0e8`](#insn-00bdb0e8)

~~~json
{
  "source": "00bdb0e8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb0ec`](#insn-00bdb0ec)

~~~json
{
  "source": "00bdb0ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb0f4`](#insn-00bdb0f4)

~~~json
{
  "source": "00bdb0f4",
  "target": "00c5db30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb0fc`](#insn-00bdb0fc)

~~~json
{
  "source": "00bdb0fc",
  "target": "0029fd08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fd08",
  "offset": 0,
  "size": 37,
  "datatype": "string",
  "bytes": "766572696669636174696f6e5f696420262620766572696669636174696f6e5f",
  "capture_start": "0029fd08",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdb100`](#insn-00bdb100)

~~~json
{
  "source": "00bdb100",
  "target": "00bdb118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb108`](#insn-00bdb108)

~~~json
{
  "source": "00bdb108",
  "target": "002b7e10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7e10",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7e10",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdb10c`](#insn-00bdb10c)

~~~json
{
  "source": "00bdb10c",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb114`](#insn-00bdb114)

~~~json
{
  "source": "00bdb114",
  "target": "003100f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003100f0",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "003100f0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdb118`](#insn-00bdb118)

~~~json
{
  "source": "00bdb118",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdb120`](#insn-00bdb120)

~~~json
{
  "source": "00bdb120",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb124`](#insn-00bdb124)

~~~json
{
  "source": "00bdb124",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb128`](#insn-00bdb128)

~~~json
{
  "source": "00bdb128",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdb130`](#insn-00bdb130)

~~~json
{
  "source": "00bdb130",
  "target": "00c5db40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
