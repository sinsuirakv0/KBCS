# 00bdaa5c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd9a68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9a68.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-61ae15b4095868017031ceabf7124194)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaa5c",
  "name": "_ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc",
  "size": 332,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce07d2f71c4bdeeb67d039230842751e709e8f1af69a5a7485b7b28292099e16",
  "source_text_sha256": "ce07d2f71c4bdeeb67d039230842751e709e8f1af69a5a7485b7b28292099e16",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaa5c",
        "00bdaba7"
      ]
    ],
    "bytes_sha256": "f543f477e3b378b42f2f6cbff3f7cbb782b068d87cd30c7286702af5c4943e0f",
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
"token"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1619 bytes

~~~c

void _ZN8firebase4auth18GitHubAuthProvider13GetCredentialEPKc(undefined8 *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  char *pcVar6;
  
  if (param_2 == 0) {
    pcVar6 = "token";
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
                        (plVar2,DAT_01127b68,DAT_01127b78,uVar3);
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
      goto LAB_00bdab84;
    }
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
    pcVar6 = 
    "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
    ;
  }
  _ZN8firebase9LogAssertEPKcz(pcVar6);
  uVar3 = 0;
LAB_00bdab84:
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
<a id="insn-00bdaa5c"></a> `00bdaa5c` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bdaa60"></a> `00bdaa60` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaa64"></a> `00bdaa64` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdaa68"></a> `00bdaa68` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdaa6c"></a> `00bdaa6c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdaa70"></a> `00bdaa70` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdaa74"></a> `00bdaa74` | `40 07 00 b4` | cbz x0,0x00bdab5c | `CONDITIONAL_JUMP`
<a id="insn-00bdaa78"></a> `00bdaa78` | `68 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdaa7c"></a> `00bdaa7c` | `08 e1 76 39` | ldrb w8,[x8, #0xdb8] | `FALL_THROUGH`
<a id="insn-00bdaa80"></a> `00bdaa80` | `48 07 00 34` | cbz w8,0x00bdab68 | `CONDITIONAL_JUMP`
<a id="insn-00bdaa84"></a> `00bdaa84` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdaa88"></a> `00bdaa88` | `1e 06 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaa8c"></a> `00bdaa8c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdaa90"></a> `00bdaa90` | `80 00 00 b5` | cbnz x0,0x00bdaaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bdaa94"></a> `00bdaa94` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdaa98"></a> `00bdaa98` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdaa9c"></a> `00bdaa9c` | `81 05 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaaa0"></a> `00bdaaa0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdaaa4"></a> `00bdaaa4` | `9f 05 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaaa8"></a> `00bdaaa8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdaaac"></a> `00bdaaac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdaab0"></a> `00bdaab0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdaab4"></a> `00bdaab4` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdaab8"></a> `00bdaab8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdaabc"></a> `00bdaabc` | `68 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdaac0"></a> `00bdaac0` | `69 2a 00 b0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdaac4"></a> `00bdaac4` | `01 b5 45 f9` | ldr x1,[x8, #0xb68] | `FALL_THROUGH`
<a id="insn-00bdaac8"></a> `00bdaac8` | `22 bd 45 f9` | ldr x2,[x9, #0xb78] | `FALL_THROUGH`
<a id="insn-00bdaacc"></a> `00bdaacc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdaad0"></a> `00bdaad0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdaad4"></a> `00bdaad4` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdaad8"></a> `00bdaad8` | `5a 04 02 94` | bl 0x00c5bc40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaadc"></a> `00bdaadc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdaae0"></a> `00bdaae0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdaae4"></a> `00bdaae4` | `47 05 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaae8"></a> `00bdaae8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bdaaec"></a> `00bdaaec` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bdaaf0"></a> `00bdaaf0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdaaf4"></a> `00bdaaf4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdaaf8"></a> `00bdaaf8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdaafc"></a> `00bdaafc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdab00"></a> `00bdab00` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdab04"></a> `00bdab04` | `17 04 00 37` | tbnz w23,#0x0,0x00bdab84 | `CONDITIONAL_JUMP`
<a id="insn-00bdab08"></a> `00bdab08` | `f4 03 00 b4` | cbz x20,0x00bdab84 | `CONDITIONAL_JUMP`
<a id="insn-00bdab0c"></a> `00bdab0c` | `fd 05 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab10"></a> `00bdab10` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdab14"></a> `00bdab14` | `80 00 00 b5` | cbnz x0,0x00bdab24 | `CONDITIONAL_JUMP`
<a id="insn-00bdab18"></a> `00bdab18` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdab1c"></a> `00bdab1c` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdab20"></a> `00bdab20` | `60 05 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab24"></a> `00bdab24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdab28"></a> `00bdab28` | `7e 05 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab2c"></a> `00bdab2c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdab30"></a> `00bdab30` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdab34"></a> `00bdab34` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdab38"></a> `00bdab38` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdab3c"></a> `00bdab3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdab40"></a> `00bdab40` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdab44"></a> `00bdab44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdab48"></a> `00bdab48` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdab4c"></a> `00bdab4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdab50"></a> `00bdab50` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdab54"></a> `00bdab54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdab58"></a> `00bdab58` | `0b 00 00 14` | b 0x00bdab84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdab5c"></a> `00bdab5c` | `40 b6 ff 90` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bdab60"></a> `00bdab60` | `00 34 3a 91` | add x0,x0,#0xe8d | `FALL_THROUGH`
<a id="insn-00bdab64"></a> `00bdab64` | `06 00 00 14` | b 0x00bdab7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdab68"></a> `00bdab68` | `e0 b6 ff b0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bdab6c"></a> `00bdab6c` | `00 7c 3c 91` | add x0,x0,#0xf1f | `FALL_THROUGH`
<a id="insn-00bdab70"></a> `00bdab70` | `74 04 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab74"></a> `00bdab74` | `a0 b9 ff d0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bdab78"></a> `00bdab78` | `00 c0 05 91` | add x0,x0,#0x170 | `FALL_THROUGH`
<a id="insn-00bdab7c"></a> `00bdab7c` | `49 05 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdab80"></a> `00bdab80` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00bdab84"></a> `00bdab84` | `75 02 00 f9` | str x21,[x19] | `FALL_THROUGH`
<a id="insn-00bdab88"></a> `00bdab88` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdab8c"></a> `00bdab8c` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bdab90"></a> `00bdab90` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab94"></a> `00bdab94` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdab98"></a> `00bdab98` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdab9c"></a> `00bdab9c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdaba0"></a> `00bdaba0` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdaba4"></a> `00bdaba4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaa5c`](#insn-00bdaa5c) 範囲 `[['00bdaa5c', '00bdaa77']]`
  - `CONDITIONAL_JUMP` [`00bdaa74`](#insn-00bdaa74) → [`00bdab5c`](#insn-00bdab5c)
  - `FALL_THROUGH` [`00bdaa74`](#insn-00bdaa74) → [`00bdaa78`](#insn-00bdaa78)
- ブロック [`00bdaa78`](#insn-00bdaa78) 範囲 `[['00bdaa78', '00bdaa83']]`
  - `CONDITIONAL_JUMP` [`00bdaa80`](#insn-00bdaa80) → [`00bdab68`](#insn-00bdab68)
  - `FALL_THROUGH` [`00bdaa80`](#insn-00bdaa80) → [`00bdaa84`](#insn-00bdaa84)
- ブロック [`00bdaa84`](#insn-00bdaa84) 範囲 `[['00bdaa84', '00bdaa93']]`
  - `CONDITIONAL_JUMP` [`00bdaa90`](#insn-00bdaa90) → [`00bdaaa0`](#insn-00bdaaa0)
  - `FALL_THROUGH` [`00bdaa90`](#insn-00bdaa90) → [`00bdaa94`](#insn-00bdaa94)
- ブロック [`00bdaa94`](#insn-00bdaa94) 範囲 `[['00bdaa94', '00bdaa9f']]`
  - `FALL_THROUGH` [`00bdaa9c`](#insn-00bdaa9c) → [`00bdaaa0`](#insn-00bdaaa0)
- ブロック [`00bdaaa0`](#insn-00bdaaa0) 範囲 `[['00bdaaa0', '00bdab07']]`
  - `CONDITIONAL_JUMP` [`00bdab04`](#insn-00bdab04) → [`00bdab84`](#insn-00bdab84)
  - `FALL_THROUGH` [`00bdab04`](#insn-00bdab04) → [`00bdab08`](#insn-00bdab08)
- ブロック [`00bdab08`](#insn-00bdab08) 範囲 `[['00bdab08', '00bdab0b']]`
  - `CONDITIONAL_JUMP` [`00bdab08`](#insn-00bdab08) → [`00bdab84`](#insn-00bdab84)
  - `FALL_THROUGH` [`00bdab08`](#insn-00bdab08) → [`00bdab0c`](#insn-00bdab0c)
- ブロック [`00bdab0c`](#insn-00bdab0c) 範囲 `[['00bdab0c', '00bdab17']]`
  - `CONDITIONAL_JUMP` [`00bdab14`](#insn-00bdab14) → [`00bdab24`](#insn-00bdab24)
  - `FALL_THROUGH` [`00bdab14`](#insn-00bdab14) → [`00bdab18`](#insn-00bdab18)
- ブロック [`00bdab18`](#insn-00bdab18) 範囲 `[['00bdab18', '00bdab23']]`
  - `FALL_THROUGH` [`00bdab20`](#insn-00bdab20) → [`00bdab24`](#insn-00bdab24)
- ブロック [`00bdab24`](#insn-00bdab24) 範囲 `[['00bdab24', '00bdab5b']]`
  - `UNCONDITIONAL_JUMP` [`00bdab58`](#insn-00bdab58) → [`00bdab84`](#insn-00bdab84)
- ブロック [`00bdab5c`](#insn-00bdab5c) 範囲 `[['00bdab5c', '00bdab67']]`
  - `UNCONDITIONAL_JUMP` [`00bdab64`](#insn-00bdab64) → [`00bdab7c`](#insn-00bdab7c)
- ブロック [`00bdab68`](#insn-00bdab68) 範囲 `[['00bdab68', '00bdab7b']]`
  - `FALL_THROUGH` [`00bdab78`](#insn-00bdab78) → [`00bdab7c`](#insn-00bdab7c)
- ブロック [`00bdab7c`](#insn-00bdab7c) 範囲 `[['00bdab7c', '00bdab83']]`
  - `FALL_THROUGH` [`00bdab80`](#insn-00bdab80) → [`00bdab84`](#insn-00bdab84)
- ブロック [`00bdab84`](#insn-00bdab84) 範囲 `[['00bdab84', '00bdaba7']]`

## 命令位置別の参照

- [`00bdaa5c`](#insn-00bdaa5c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa60`](#insn-00bdaa60) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa64`](#insn-00bdaa64) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa68`](#insn-00bdaa68) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa74`](#insn-00bdaa74) → [`00bdab5c`](#insn-00bdab5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa7c`](#insn-00bdaa7c) → `01127db8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdaa80`](#insn-00bdaa80) → [`00bdab68`](#insn-00bdab68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa88`](#insn-00bdaa88) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa90`](#insn-00bdaa90) → [`00bdaaa0`](#insn-00bdaaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaa98`](#insn-00bdaa98) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdaa9c`](#insn-00bdaa9c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdaaa4`](#insn-00bdaaa4) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdaac4`](#insn-00bdaac4) → `01127b68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdaac8`](#insn-00bdaac8) → `01127b78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdaad8`](#insn-00bdaad8) → [`00c5bc40`](../00c5b/00c5bc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc40` · 推定シンボル `None` · 推定型 `None`
- [`00bdaae4`](#insn-00bdaae4) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdab04`](#insn-00bdab04) → [`00bdab84`](#insn-00bdab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab08`](#insn-00bdab08) → [`00bdab84`](#insn-00bdab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab0c`](#insn-00bdab0c) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdab14`](#insn-00bdab14) → [`00bdab24`](#insn-00bdab24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab1c`](#insn-00bdab1c) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdab20`](#insn-00bdab20) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdab28`](#insn-00bdab28) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdab58`](#insn-00bdab58) → [`00bdab84`](#insn-00bdab84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab60`](#insn-00bdab60) → `002a2e8d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdab64`](#insn-00bdab64) → [`00bdab7c`](#insn-00bdab7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab6c`](#insn-00bdab6c) → `002b7f1f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdab70`](#insn-00bdab70) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bdab78`](#insn-00bdab78) → `00310170`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdab7c`](#insn-00bdab7c) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdab94`](#insn-00bdab94) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab98`](#insn-00bdab98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab9c`](#insn-00bdab9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaa5c`](#insn-00bdaa5c)

~~~json
{
  "source": "00bdaa5c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa60`](#insn-00bdaa60)

~~~json
{
  "source": "00bdaa60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa64`](#insn-00bdaa64)

~~~json
{
  "source": "00bdaa64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa68`](#insn-00bdaa68)

~~~json
{
  "source": "00bdaa68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa74`](#insn-00bdaa74)

~~~json
{
  "source": "00bdaa74",
  "target": "00bdab5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa7c`](#insn-00bdaa7c)

~~~json
{
  "source": "00bdaa7c",
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
- 参照命令 [`00bdaa80`](#insn-00bdaa80)

~~~json
{
  "source": "00bdaa80",
  "target": "00bdab68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa88`](#insn-00bdaa88)

~~~json
{
  "source": "00bdaa88",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaa90`](#insn-00bdaa90)

~~~json
{
  "source": "00bdaa90",
  "target": "00bdaaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaa98`](#insn-00bdaa98)

~~~json
{
  "source": "00bdaa98",
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
- 参照命令 [`00bdaa9c`](#insn-00bdaa9c)

~~~json
{
  "source": "00bdaa9c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaaa4`](#insn-00bdaaa4)

~~~json
{
  "source": "00bdaaa4",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaac4`](#insn-00bdaac4)

~~~json
{
  "source": "00bdaac4",
  "target": "01127b68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdaac8`](#insn-00bdaac8)

~~~json
{
  "source": "00bdaac8",
  "target": "01127b78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdaad8`](#insn-00bdaad8)

~~~json
{
  "source": "00bdaad8",
  "target": "00c5bc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaae4`](#insn-00bdaae4)

~~~json
{
  "source": "00bdaae4",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab04`](#insn-00bdab04)

~~~json
{
  "source": "00bdab04",
  "target": "00bdab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab08`](#insn-00bdab08)

~~~json
{
  "source": "00bdab08",
  "target": "00bdab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab0c`](#insn-00bdab0c)

~~~json
{
  "source": "00bdab0c",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab14`](#insn-00bdab14)

~~~json
{
  "source": "00bdab14",
  "target": "00bdab24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab1c`](#insn-00bdab1c)

~~~json
{
  "source": "00bdab1c",
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
- 参照命令 [`00bdab20`](#insn-00bdab20)

~~~json
{
  "source": "00bdab20",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab28`](#insn-00bdab28)

~~~json
{
  "source": "00bdab28",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab58`](#insn-00bdab58)

~~~json
{
  "source": "00bdab58",
  "target": "00bdab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab60`](#insn-00bdab60)

~~~json
{
  "source": "00bdab60",
  "target": "002a2e8d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2e8d",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "746f6b656e00",
  "capture_start": "002a2e8d",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdab64`](#insn-00bdab64)

~~~json
{
  "source": "00bdab64",
  "target": "00bdab7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab6c`](#insn-00bdab6c)

~~~json
{
  "source": "00bdab6c",
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
- 参照命令 [`00bdab70`](#insn-00bdab70)

~~~json
{
  "source": "00bdab70",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab78`](#insn-00bdab78)

~~~json
{
  "source": "00bdab78",
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
- 参照命令 [`00bdab7c`](#insn-00bdab7c)

~~~json
{
  "source": "00bdab7c",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdab94`](#insn-00bdab94)

~~~json
{
  "source": "00bdab94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab98`](#insn-00bdab98)

~~~json
{
  "source": "00bdab98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab9c`](#insn-00bdab9c)

~~~json
{
  "source": "00bdab9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
