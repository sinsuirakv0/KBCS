# 00b0ddbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0dcf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0d/00b0dcf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0064.md#compare-949310eb6db5c9afbcf0359bd31e11dd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b0de00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0067.md#compare-2ff4e646e69f6966f4e3b41284aed0b9)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0ddbc",
  "name": "_ZN20google_play_services17CallMakeAvailableEPv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee4322456d2cb960c5b47c2ccd997e1a1c8e90126b76ba72cefce69d4eb2623f",
  "source_text_sha256": "ee4322456d2cb960c5b47c2ccd997e1a1c8e90126b76ba72cefce69d4eb2623f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0ddbc",
        "00b0de93"
      ]
    ],
    "bytes_sha256": "9f0ddd47296be540cfc5168e349306b6718cfb8d7c5d254757dd0567d456aab9",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bddbf0](../00bdd/00bddbf0.md)
- [00bddf30](../00bdd/00bddf30.md)
- [00bde090](../00bde/00bde090.md)
- [00bde4f0](../00bde/00bde4f0.md)
- [00bdedb0](../00bde/00bdedb0.md)
- [00bdf040](../00bdf/00bdf040.md)

## 関連文字列（未確認候補）

~~~text
"Call to makeGooglePlayServicesAvailable failed."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1463 bytes

~~~c

void _ZN20google_play_services17CallMakeAvailableEPv(undefined8 *param_1)

{
  long lVar1;
  long lVar2;
  char cVar3;
  long *plVar4;
  undefined1 auStack_50 [16];
  undefined1 auStack_40 [8];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)_ZN8firebase4util19GetThreadsafeJNIEnvEP7_JavaVM(*param_1);
  if (plVar4 != (long *)0x0) {
    cVar3 = _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz
                      (plVar4,DAT_010a0eb8,DAT_010a0ec8,param_1[1]);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar4);
    (**(code **)(*plVar4 + 0xb0))(plVar4,param_1[1]);
    lVar2 = DAT_010a0e98;
    if (cVar3 == '\0') {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_50,DAT_010a0e98 + 0x130);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (lVar2,auStack_50,0xffffffff,"Call to makeGooglePlayServicesAvailable failed.",
                 auStack_40);
      _ZN8firebase12FutureHandleD1Ev(auStack_50);
    }
  }
                    /* try { // try from 00b0de64 to 00c0de6b has its CatchHandler @ 00b0dfec */
  _ZdlPv(param_1);
                    /* try { // try from 00b0de6c to 00c0df63 has its CatchHandler @ 00b0d964 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00b0ddbc"></a> `00b0ddbc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b0ddc0"></a> `00b0ddc0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ddc4"></a> `00b0ddc4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0ddc8"></a> `00b0ddc8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0ddcc"></a> `00b0ddcc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b0ddd0"></a> `00b0ddd0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b0ddd4"></a> `00b0ddd4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b0ddd8"></a> `00b0ddd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0dddc"></a> `00b0dddc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b0dde0"></a> `00b0dde0` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00b0dde4"></a> `00b0dde4` | `c3 41 03 94` | bl 0x00bde4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0dde8"></a> `00b0dde8` | `e0 03 00 b4` | cbz x0,0x00b0de64 | `CONDITIONAL_JUMP`
<a id="insn-00b0ddec"></a> `00b0ddec` | `88 2c 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b0ddf0"></a> `00b0ddf0` | `89 2c 00 f0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b0ddf4"></a> `00b0ddf4` | `01 5d 47 f9` | ldr x1,[x8, #0xeb8] | `FALL_THROUGH`
<a id="insn-00b0ddf8"></a> `00b0ddf8` | `22 65 47 f9` | ldr x2,[x9, #0xec8] | `FALL_THROUGH`
<a id="insn-00b0ddfc"></a> `00b0ddfc` | `63 06 40 f9` | ldr x3,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0de00"></a> `00b0de00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b0de04"></a> `00b0de04` | `8f 44 03 94` | bl 0x00bdf040 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de08"></a> `00b0de08` | `16 1c 00 12` | and w22,w0,#0xff | `FALL_THROUGH`
<a id="insn-00b0de0c"></a> `00b0de0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0de10"></a> `00b0de10` | `a0 40 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de14"></a> `00b0de14` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00b0de18"></a> `00b0de18` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0de1c"></a> `00b0de1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0de20"></a> `00b0de20` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b0de24"></a> `00b0de24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b0de28"></a> `00b0de28` | `f6 01 00 35` | cbnz w22,0x00b0de64 | `CONDITIONAL_JUMP`
<a id="insn-00b0de2c"></a> `00b0de2c` | `88 2c 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b0de30"></a> `00b0de30` | `14 4d 47 f9` | ldr x20,[x8, #0xe98] | `FALL_THROUGH`
<a id="insn-00b0de34"></a> `00b0de34` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b0de38"></a> `00b0de38` | `81 c2 04 91` | add x1,x20,#0x130 | `FALL_THROUGH`
<a id="insn-00b0de3c"></a> `00b0de3c` | `3d 40 03 94` | bl 0x00bddf30 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de40"></a> `00b0de40` | `a3 bc ff f0` | adrp x3,0x2a4000 | `FALL_THROUGH`
<a id="insn-00b0de44"></a> `00b0de44` | `63 74 3f 91` | add x3,x3,#0xfdd | `FALL_THROUGH`
<a id="insn-00b0de48"></a> `00b0de48` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00b0de4c"></a> `00b0de4c` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0de50"></a> `00b0de50` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b0de54"></a> `00b0de54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0de58"></a> `00b0de58` | `d6 43 03 94` | bl 0x00bdedb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de5c"></a> `00b0de5c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b0de60"></a> `00b0de60` | `64 3f 03 94` | bl 0x00bddbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de64"></a> `00b0de64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b0de68"></a> `00b0de68` | `6a 34 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b0de6c"></a> `00b0de6c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b0de70"></a> `00b0de70` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b0de74"></a> `00b0de74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b0de78"></a> `00b0de78` | `c1 00 00 54` | b.ne 0x00b0de90 | `CONDITIONAL_JUMP`
<a id="insn-00b0de7c"></a> `00b0de7c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0de80"></a> `00b0de80` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b0de84"></a> `00b0de84` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0de88"></a> `00b0de88` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b0de8c"></a> `00b0de8c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0de90"></a> `00b0de90` | `6c 34 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0ddbc`](#insn-00b0ddbc) 範囲 `[['00b0ddbc', '00b0ddeb']]`
  - `CONDITIONAL_JUMP` [`00b0dde8`](#insn-00b0dde8) → [`00b0de64`](#insn-00b0de64)
  - `FALL_THROUGH` [`00b0dde8`](#insn-00b0dde8) → [`00b0ddec`](#insn-00b0ddec)
- ブロック [`00b0ddec`](#insn-00b0ddec) 範囲 `[['00b0ddec', '00b0de2b']]`
  - `CONDITIONAL_JUMP` [`00b0de28`](#insn-00b0de28) → [`00b0de64`](#insn-00b0de64)
  - `FALL_THROUGH` [`00b0de28`](#insn-00b0de28) → [`00b0de2c`](#insn-00b0de2c)
- ブロック [`00b0de2c`](#insn-00b0de2c) 範囲 `[['00b0de2c', '00b0de63']]`
  - `FALL_THROUGH` [`00b0de60`](#insn-00b0de60) → [`00b0de64`](#insn-00b0de64)
- ブロック [`00b0de64`](#insn-00b0de64) 範囲 `[['00b0de64', '00b0de6b']]`
  - `FALL_THROUGH` [`00b0de68`](#insn-00b0de68) → [`00b0de6c`](#insn-00b0de6c)
- ブロック [`00b0de6c`](#insn-00b0de6c) 範囲 `[['00b0de6c', '00b0de7b']]`
  - `CONDITIONAL_JUMP` [`00b0de78`](#insn-00b0de78) → [`00b0de90`](#insn-00b0de90)
  - `FALL_THROUGH` [`00b0de78`](#insn-00b0de78) → [`00b0de7c`](#insn-00b0de7c)
- ブロック [`00b0de7c`](#insn-00b0de7c) 範囲 `[['00b0de7c', '00b0de8f']]`
- ブロック [`00b0de90`](#insn-00b0de90) 範囲 `[['00b0de90', '00b0de93']]`

## 命令位置別の参照

- [`00b0ddc0`](#insn-00b0ddc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddc4`](#insn-00b0ddc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddc8`](#insn-00b0ddc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dddc`](#insn-00b0dddc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dde4`](#insn-00b0dde4) → [`00bde4f0`](../00bde/00bde4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde4f0` · 推定シンボル `None` · 推定型 `None`
- [`00b0dde8`](#insn-00b0dde8) → [`00b0de64`](#insn-00b0de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddf4`](#insn-00b0ddf4) → `010a0eb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b0ddf8`](#insn-00b0ddf8) → `010a0ec8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b0de04`](#insn-00b0de04) → [`00bdf040`](../00bdf/00bdf040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdf040` · 推定シンボル `None` · 推定型 `None`
- [`00b0de10`](#insn-00b0de10) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b0de28`](#insn-00b0de28) → [`00b0de64`](#insn-00b0de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de30`](#insn-00b0de30) → `010a0e98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b0de3c`](#insn-00b0de3c) → [`00bddf30`](../00bdd/00bddf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf30` · 推定シンボル `None` · 推定型 `None`
- [`00b0de44`](#insn-00b0de44) → `002a4fdd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b0de58`](#insn-00b0de58) → [`00bdedb0`](../00bde/00bdedb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdedb0` · 推定シンボル `None` · 推定型 `None`
- [`00b0de60`](#insn-00b0de60) → [`00bddbf0`](../00bdd/00bddbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbf0` · 推定シンボル `None` · 推定型 `None`
- [`00b0de68`](#insn-00b0de68) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b0de70`](#insn-00b0de70) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de78`](#insn-00b0de78) → [`00b0de90`](#insn-00b0de90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de7c`](#insn-00b0de7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de80`](#insn-00b0de80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de84`](#insn-00b0de84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de90`](#insn-00b0de90) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0ddc0`](#insn-00b0ddc0)

~~~json
{
  "source": "00b0ddc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddc4`](#insn-00b0ddc4)

~~~json
{
  "source": "00b0ddc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddc8`](#insn-00b0ddc8)

~~~json
{
  "source": "00b0ddc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dddc`](#insn-00b0dddc)

~~~json
{
  "source": "00b0dddc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dde4`](#insn-00b0dde4)

~~~json
{
  "source": "00b0dde4",
  "target": "00bde4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0dde8`](#insn-00b0dde8)

~~~json
{
  "source": "00b0dde8",
  "target": "00b0de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddf4`](#insn-00b0ddf4)

~~~json
{
  "source": "00b0ddf4",
  "target": "010a0eb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0eb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b0ddf8`](#insn-00b0ddf8)

~~~json
{
  "source": "00b0ddf8",
  "target": "010a0ec8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ec8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b0de04`](#insn-00b0de04)

~~~json
{
  "source": "00b0de04",
  "target": "00bdf040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de10`](#insn-00b0de10)

~~~json
{
  "source": "00b0de10",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de28`](#insn-00b0de28)

~~~json
{
  "source": "00b0de28",
  "target": "00b0de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de30`](#insn-00b0de30)

~~~json
{
  "source": "00b0de30",
  "target": "010a0e98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0e98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b0de3c`](#insn-00b0de3c)

~~~json
{
  "source": "00b0de3c",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de44`](#insn-00b0de44)

~~~json
{
  "source": "00b0de44",
  "target": "002a4fdd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4fdd",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "43616c6c20746f206d616b65476f6f676c65506c617953657276696365734176",
  "capture_start": "002a4fdd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b0de58`](#insn-00b0de58)

~~~json
{
  "source": "00b0de58",
  "target": "00bdedb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de60`](#insn-00b0de60)

~~~json
{
  "source": "00b0de60",
  "target": "00bddbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de68`](#insn-00b0de68)

~~~json
{
  "source": "00b0de68",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0de70`](#insn-00b0de70)

~~~json
{
  "source": "00b0de70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de78`](#insn-00b0de78)

~~~json
{
  "source": "00b0de78",
  "target": "00b0de90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de7c`](#insn-00b0de7c)

~~~json
{
  "source": "00b0de7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de80`](#insn-00b0de80)

~~~json
{
  "source": "00b0de80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de84`](#insn-00b0de84)

~~~json
{
  "source": "00b0de84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de90`](#insn-00b0de90)

~~~json
{
  "source": "00b0de90",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
