# 00bdad4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd9d58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9d58.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-bed3deeca863876d644878af0b0bdcd3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdad4c",
  "name": "_ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e35942d024fdbde5bc670aa9262167405c962b627ed2606a41e92bb22e0910f",
  "source_text_sha256": "9e35942d024fdbde5bc670aa9262167405c962b627ed2606a41e92bb22e0910f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdad4c",
        "00bdae97"
      ]
    ],
    "bytes_sha256": "fa3a2f216a2719cc00f1a620b8e8b5173b027d4839a1e48d1d7e37e004812e0b",
    "instruction_count": 83,
    "instruction_bytes": 332,
    "body_bytes": 332,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"server_auth_code"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1633 bytes

~~~c

void _ZN8firebase4auth21PlayGamesAuthProvider13GetCredentialEPKc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  char *pcVar6;
  
  if (param_2 == 0) {
    pcVar6 = "server_auth_code";
  }
  else {
    if (DAT_01127db8 != '\0') {
      lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar1 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
      uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_2);
      lVar1 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                        (plVar2,DAT_01127ba8,DAT_01127bb8,uVar3);
      uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
      uVar3 = 0;
      if (((uVar4 & 1) == 0) && (lVar1 != 0)) {
        lVar5 = _ZN8firebase10app_common9GetAnyAppEv();
        if (lVar5 == 0) {
          _ZN8firebase9LogAssertEPKcz("app != nullptr");
        }
        plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar5);
        uVar3 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar1);
        (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      }
      goto LAB_00bdae74;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar6 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar6);
  uVar3 = 0;
LAB_00bdae74:
  *param_1 = uVar3;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdad4c"></a> `00bdad4c` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bdad50"></a> `00bdad50` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdad54"></a> `00bdad54` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdad58"></a> `00bdad58` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdad5c"></a> `00bdad5c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdad60"></a> `00bdad60` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdad64"></a> `00bdad64` | `40 07 00 b4` | cbz x0,0x00bdae4c | `CONDITIONAL_JUMP`
<a id="insn-00bdad68"></a> `00bdad68` | `68 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdad6c"></a> `00bdad6c` | `08 e1 76 39` | ldrb w8,[x8, #0xdb8] | `FALL_THROUGH`
<a id="insn-00bdad70"></a> `00bdad70` | `48 07 00 34` | cbz w8,0x00bdae58 | `CONDITIONAL_JUMP`
<a id="insn-00bdad74"></a> `00bdad74` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdad78"></a> `00bdad78` | `62 05 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad7c"></a> `00bdad7c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdad80"></a> `00bdad80` | `80 00 00 b5` | cbnz x0,0x00bdad90 | `CONDITIONAL_JUMP`
<a id="insn-00bdad84"></a> `00bdad84` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdad88"></a> `00bdad88` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdad8c"></a> `00bdad8c` | `c5 04 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad90"></a> `00bdad90` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdad94"></a> `00bdad94` | `e3 04 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad98"></a> `00bdad98` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdad9c"></a> `00bdad9c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdada0"></a> `00bdada0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdada4"></a> `00bdada4` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdada8"></a> `00bdada8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdadac"></a> `00bdadac` | `68 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdadb0"></a> `00bdadb0` | `69 2a 00 b0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdadb4"></a> `00bdadb4` | `01 d5 45 f9` | ldr x1,[x8, #0xba8] | `FALL_THROUGH`
<a id="insn-00bdadb8"></a> `00bdadb8` | `22 dd 45 f9` | ldr x2,[x9, #0xbb8] | `FALL_THROUGH`
<a id="insn-00bdadbc"></a> `00bdadbc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdadc0"></a> `00bdadc0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdadc4"></a> `00bdadc4` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdadc8"></a> `00bdadc8` | `9e 03 02 94` | bl 0x00c5bc40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadcc"></a> `00bdadcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdadd0"></a> `00bdadd0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdadd4"></a> `00bdadd4` | `8b 04 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdadd8"></a> `00bdadd8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdaddc"></a> `00bdaddc` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bdade0"></a> `00bdade0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdade4"></a> `00bdade4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdade8"></a> `00bdade8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdadec"></a> `00bdadec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdadf0"></a> `00bdadf0` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdadf4"></a> `00bdadf4` | `17 04 00 37` | tbnz w23,#0x0,0x00bdae74 | `CONDITIONAL_JUMP`
<a id="insn-00bdadf8"></a> `00bdadf8` | `f4 03 00 b4` | cbz x20,0x00bdae74 | `CONDITIONAL_JUMP`
<a id="insn-00bdadfc"></a> `00bdadfc` | `41 05 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae00"></a> `00bdae00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdae04"></a> `00bdae04` | `80 00 00 b5` | cbnz x0,0x00bdae14 | `CONDITIONAL_JUMP`
<a id="insn-00bdae08"></a> `00bdae08` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdae0c"></a> `00bdae0c` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdae10"></a> `00bdae10` | `a4 04 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae14"></a> `00bdae14` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdae18"></a> `00bdae18` | `c2 04 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae1c"></a> `00bdae1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdae20"></a> `00bdae20` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdae24"></a> `00bdae24` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdae28"></a> `00bdae28` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdae2c"></a> `00bdae2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdae30"></a> `00bdae30` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdae34"></a> `00bdae34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdae38"></a> `00bdae38` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdae3c"></a> `00bdae3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdae40"></a> `00bdae40` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdae44"></a> `00bdae44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdae48"></a> `00bdae48` | `0b 00 00 14` | b 0x00bdae74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdae4c"></a> `00bdae4c` | `e0 b6 ff d0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bdae50"></a> `00bdae50` | `00 54 36 91` | add x0,x0,#0xd95 | `FALL_THROUGH`
<a id="insn-00bdae54"></a> `00bdae54` | `06 00 00 14` | b 0x00bdae6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdae58"></a> `00bdae58` | `e0 b6 ff b0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bdae5c"></a> `00bdae5c` | `00 7c 3c 91` | add x0,x0,#0xf1f | `FALL_THROUGH`
<a id="insn-00bdae60"></a> `00bdae60` | `b8 03 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae64"></a> `00bdae64` | `a0 b9 ff d0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bdae68"></a> `00bdae68` | `00 c0 05 91` | add x0,x0,#0x170 | `FALL_THROUGH`
<a id="insn-00bdae6c"></a> `00bdae6c` | `8d 04 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdae70"></a> `00bdae70` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdae74"></a> `00bdae74` | `75 02 00 f9` | str x21,[x19] | `FALL_THROUGH`
<a id="insn-00bdae78"></a> `00bdae78` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdae7c"></a> `00bdae7c` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bdae80"></a> `00bdae80` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdae84"></a> `00bdae84` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdae88"></a> `00bdae88` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdae8c"></a> `00bdae8c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdae90"></a> `00bdae90` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdae94"></a> `00bdae94` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdad4c`](#insn-00bdad4c) 範囲 `[['00bdad4c', '00bdad67']]`
  - `CONDITIONAL_JUMP` [`00bdad64`](#insn-00bdad64) → [`00bdae4c`](#insn-00bdae4c)
  - `FALL_THROUGH` [`00bdad64`](#insn-00bdad64) → [`00bdad68`](#insn-00bdad68)
- ブロック [`00bdad68`](#insn-00bdad68) 範囲 `[['00bdad68', '00bdad73']]`
  - `CONDITIONAL_JUMP` [`00bdad70`](#insn-00bdad70) → [`00bdae58`](#insn-00bdae58)
  - `FALL_THROUGH` [`00bdad70`](#insn-00bdad70) → [`00bdad74`](#insn-00bdad74)
- ブロック [`00bdad74`](#insn-00bdad74) 範囲 `[['00bdad74', '00bdad83']]`
  - `CONDITIONAL_JUMP` [`00bdad80`](#insn-00bdad80) → [`00bdad90`](#insn-00bdad90)
  - `FALL_THROUGH` [`00bdad80`](#insn-00bdad80) → [`00bdad84`](#insn-00bdad84)
- ブロック [`00bdad84`](#insn-00bdad84) 範囲 `[['00bdad84', '00bdad8f']]`
  - `FALL_THROUGH` [`00bdad8c`](#insn-00bdad8c) → [`00bdad90`](#insn-00bdad90)
- ブロック [`00bdad90`](#insn-00bdad90) 範囲 `[['00bdad90', '00bdadf7']]`
  - `CONDITIONAL_JUMP` [`00bdadf4`](#insn-00bdadf4) → [`00bdae74`](#insn-00bdae74)
  - `FALL_THROUGH` [`00bdadf4`](#insn-00bdadf4) → [`00bdadf8`](#insn-00bdadf8)
- ブロック [`00bdadf8`](#insn-00bdadf8) 範囲 `[['00bdadf8', '00bdadfb']]`
  - `CONDITIONAL_JUMP` [`00bdadf8`](#insn-00bdadf8) → [`00bdae74`](#insn-00bdae74)
  - `FALL_THROUGH` [`00bdadf8`](#insn-00bdadf8) → [`00bdadfc`](#insn-00bdadfc)
- ブロック [`00bdadfc`](#insn-00bdadfc) 範囲 `[['00bdadfc', '00bdae07']]`
  - `CONDITIONAL_JUMP` [`00bdae04`](#insn-00bdae04) → [`00bdae14`](#insn-00bdae14)
  - `FALL_THROUGH` [`00bdae04`](#insn-00bdae04) → [`00bdae08`](#insn-00bdae08)
- ブロック [`00bdae08`](#insn-00bdae08) 範囲 `[['00bdae08', '00bdae13']]`
  - `FALL_THROUGH` [`00bdae10`](#insn-00bdae10) → [`00bdae14`](#insn-00bdae14)
- ブロック [`00bdae14`](#insn-00bdae14) 範囲 `[['00bdae14', '00bdae4b']]`
  - `UNCONDITIONAL_JUMP` [`00bdae48`](#insn-00bdae48) → [`00bdae74`](#insn-00bdae74)
- ブロック [`00bdae4c`](#insn-00bdae4c) 範囲 `[['00bdae4c', '00bdae57']]`
  - `UNCONDITIONAL_JUMP` [`00bdae54`](#insn-00bdae54) → [`00bdae6c`](#insn-00bdae6c)
- ブロック [`00bdae58`](#insn-00bdae58) 範囲 `[['00bdae58', '00bdae6b']]`
  - `FALL_THROUGH` [`00bdae68`](#insn-00bdae68) → [`00bdae6c`](#insn-00bdae6c)
- ブロック [`00bdae6c`](#insn-00bdae6c) 範囲 `[['00bdae6c', '00bdae73']]`
  - `FALL_THROUGH` [`00bdae70`](#insn-00bdae70) → [`00bdae74`](#insn-00bdae74)
- ブロック [`00bdae74`](#insn-00bdae74) 範囲 `[['00bdae74', '00bdae97']]`

## 命令位置別の参照

- [`00bdad4c`](#insn-00bdad4c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad50`](#insn-00bdad50) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad54`](#insn-00bdad54) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad58`](#insn-00bdad58) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad64`](#insn-00bdad64) → [`00bdae4c`](#insn-00bdae4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad6c`](#insn-00bdad6c) → `01127db8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdad70`](#insn-00bdad70) → [`00bdae58`](#insn-00bdae58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad78`](#insn-00bdad78) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdad80`](#insn-00bdad80) → [`00bdad90`](#insn-00bdad90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad88`](#insn-00bdad88) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdad8c`](#insn-00bdad8c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdad94`](#insn-00bdad94) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdadb4`](#insn-00bdadb4) → `01127ba8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdadb8`](#insn-00bdadb8) → `01127bb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdadc8`](#insn-00bdadc8) → [`00c5bc40`](../00c5b/00c5bc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc40` · 推定シンボル `None` · 推定型 `None`
- [`00bdadd4`](#insn-00bdadd4) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdadf4`](#insn-00bdadf4) → [`00bdae74`](#insn-00bdae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadf8`](#insn-00bdadf8) → [`00bdae74`](#insn-00bdae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdadfc`](#insn-00bdadfc) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdae04`](#insn-00bdae04) → [`00bdae14`](#insn-00bdae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae0c`](#insn-00bdae0c) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdae10`](#insn-00bdae10) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdae18`](#insn-00bdae18) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdae48`](#insn-00bdae48) → [`00bdae74`](#insn-00bdae74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae50`](#insn-00bdae50) → `002b8d95`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdae54`](#insn-00bdae54) → [`00bdae6c`](#insn-00bdae6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae5c`](#insn-00bdae5c) → `002b7f1f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdae60`](#insn-00bdae60) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bdae68`](#insn-00bdae68) → `00310170`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdae6c`](#insn-00bdae6c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdae84`](#insn-00bdae84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae88`](#insn-00bdae88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdae8c`](#insn-00bdae8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdad4c`](#insn-00bdad4c)

~~~json
{
  "source": "00bdad4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad50`](#insn-00bdad50)

~~~json
{
  "source": "00bdad50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad54`](#insn-00bdad54)

~~~json
{
  "source": "00bdad54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad58`](#insn-00bdad58)

~~~json
{
  "source": "00bdad58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad64`](#insn-00bdad64)

~~~json
{
  "source": "00bdad64",
  "target": "00bdae4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad6c`](#insn-00bdad6c)

~~~json
{
  "source": "00bdad6c",
  "target": "01127db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127db8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdad70`](#insn-00bdad70)

~~~json
{
  "source": "00bdad70",
  "target": "00bdae58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad78`](#insn-00bdad78)

~~~json
{
  "source": "00bdad78",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad80`](#insn-00bdad80)

~~~json
{
  "source": "00bdad80",
  "target": "00bdad90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad88`](#insn-00bdad88)

~~~json
{
  "source": "00bdad88",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdad8c`](#insn-00bdad8c)

~~~json
{
  "source": "00bdad8c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad94`](#insn-00bdad94)

~~~json
{
  "source": "00bdad94",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadb4`](#insn-00bdadb4)

~~~json
{
  "source": "00bdadb4",
  "target": "01127ba8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ba8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdadb8`](#insn-00bdadb8)

~~~json
{
  "source": "00bdadb8",
  "target": "01127bb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127bb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdadc8`](#insn-00bdadc8)

~~~json
{
  "source": "00bdadc8",
  "target": "00c5bc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadd4`](#insn-00bdadd4)

~~~json
{
  "source": "00bdadd4",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdadf4`](#insn-00bdadf4)

~~~json
{
  "source": "00bdadf4",
  "target": "00bdae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadf8`](#insn-00bdadf8)

~~~json
{
  "source": "00bdadf8",
  "target": "00bdae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdadfc`](#insn-00bdadfc)

~~~json
{
  "source": "00bdadfc",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae04`](#insn-00bdae04)

~~~json
{
  "source": "00bdae04",
  "target": "00bdae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae0c`](#insn-00bdae0c)

~~~json
{
  "source": "00bdae0c",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdae10`](#insn-00bdae10)

~~~json
{
  "source": "00bdae10",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae18`](#insn-00bdae18)

~~~json
{
  "source": "00bdae18",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae48`](#insn-00bdae48)

~~~json
{
  "source": "00bdae48",
  "target": "00bdae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae50`](#insn-00bdae50)

~~~json
{
  "source": "00bdae50",
  "target": "002b8d95",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8d95",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "7365727665725f617574685f636f646500",
  "capture_start": "002b8d95",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdae54`](#insn-00bdae54)

~~~json
{
  "source": "00bdae54",
  "target": "00bdae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae5c`](#insn-00bdae5c)

~~~json
{
  "source": "00bdae5c",
  "target": "002b7f1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f1f",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7f1f",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdae60`](#insn-00bdae60)

~~~json
{
  "source": "00bdae60",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae68`](#insn-00bdae68)

~~~json
{
  "source": "00bdae68",
  "target": "00310170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310170",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "00310170",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdae6c`](#insn-00bdae6c)

~~~json
{
  "source": "00bdae6c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdae84`](#insn-00bdae84)

~~~json
{
  "source": "00bdae84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae88`](#insn-00bdae88)

~~~json
{
  "source": "00bdae88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdae8c`](#insn-00bdae8c)

~~~json
{
  "source": "00bdae8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
