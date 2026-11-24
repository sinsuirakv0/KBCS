# 00bddee8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdcef4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdcef4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-886cb4f0d7ee5f6efe97adb7ba7b9ed2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddee8",
  "name": "_ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ebfcc855d7533b2d8ffe011b8ab439e74acb0c331f53affea9b0dbae72e25c09",
  "source_text_sha256": "ebfcc855d7533b2d8ffe011b8ab439e74acb0c331f53affea9b0dbae72e25c09",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddee8",
        "00bddf27"
      ]
    ],
    "bytes_sha256": "c21cf690ca48b0008d975832fb4cf1fa7ad8362484e02525f4a65f70452dd09d",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 431 bytes

~~~c

long _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_01127dc0 == 0) {
    DAT_01127dc0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01127dc0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddee8"></a> `00bddee8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddeec"></a> `00bddeec` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddef0"></a> `00bddef0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddef4"></a> `00bddef4` | `53 2a 00 d0` | adrp x19,0x1127000 | `FALL_THROUGH`
<a id="insn-00bddef8"></a> `00bddef8` | `68 e2 46 f9` | ldr x8,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddefc"></a> `00bddefc` | `e8 00 00 b5` | cbnz x8,0x00bddf18 | `CONDITIONAL_JUMP`
<a id="insn-00bddf00"></a> `00bddf00` | `e3 b6 ff f0` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bddf04"></a> `00bddf04` | `63 68 0b 91` | add x3,x3,#0x2da | `FALL_THROUGH`
<a id="insn-00bddf08"></a> `00bddf08` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddf0c"></a> `00bddf0c` | `29 f8 01 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddf10"></a> `00bddf10` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bddf14"></a> `00bddf14` | `60 e2 06 f9` | str x0,[x19, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bddf18"></a> `00bddf18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf1c"></a> `00bddf1c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bddf20"></a> `00bddf20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddf24"></a> `00bddf24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddee8`](#insn-00bddee8) 範囲 `[['00bddee8', '00bddeff']]`
  - `CONDITIONAL_JUMP` [`00bddefc`](#insn-00bddefc) → [`00bddf18`](#insn-00bddf18)
  - `FALL_THROUGH` [`00bddefc`](#insn-00bddefc) → [`00bddf00`](#insn-00bddf00)
- ブロック [`00bddf00`](#insn-00bddf00) 範囲 `[['00bddf00', '00bddf17']]`
  - `FALL_THROUGH` [`00bddf14`](#insn-00bddf14) → [`00bddf18`](#insn-00bddf18)
- ブロック [`00bddf18`](#insn-00bddf18) 範囲 `[['00bddf18', '00bddf27']]`

## 命令位置別の参照

- [`00bddee8`](#insn-00bddee8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddeec`](#insn-00bddeec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddef8`](#insn-00bddef8) → `01127dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddefc`](#insn-00bddefc) → [`00bddf18`](#insn-00bddf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf04`](#insn-00bddf04) → `002bc2da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddf0c`](#insn-00bddf0c) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bddf14`](#insn-00bddf14) → `01127dc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf18`](#insn-00bddf18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddee8`](#insn-00bddee8)

~~~json
{
  "source": "00bddee8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddeec`](#insn-00bddeec)

~~~json
{
  "source": "00bddeec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddef8`](#insn-00bddef8)

~~~json
{
  "source": "00bddef8",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddefc`](#insn-00bddefc)

~~~json
{
  "source": "00bddefc",
  "target": "00bddf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf04`](#insn-00bddf04)

~~~json
{
  "source": "00bddf04",
  "target": "002bc2da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc2d6",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc2d6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddf0c`](#insn-00bddf0c)

~~~json
{
  "source": "00bddf0c",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf14`](#insn-00bddf14)

~~~json
{
  "source": "00bddf14",
  "target": "01127dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf18`](#insn-00bddf18)

~~~json
{
  "source": "00bddf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
