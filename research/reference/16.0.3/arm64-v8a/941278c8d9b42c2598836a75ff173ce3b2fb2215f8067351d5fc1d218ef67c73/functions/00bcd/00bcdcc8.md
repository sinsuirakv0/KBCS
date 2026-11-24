# 00bcdcc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcccd4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bcccd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-326c57616edab7eeed0b27706d075c72)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdcc8",
  "name": "_ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "43bee76426aeaee224ad78a0af9b633cbf0226fcbba6f7733357eb8597556084",
  "source_text_sha256": "43bee76426aeaee224ad78a0af9b633cbf0226fcbba6f7733357eb8597556084",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdcc8",
        "00bcdd37"
      ]
    ],
    "bytes_sha256": "592df3c088aa7d6504891b7af30f50ba17f42ded81da741a0c898dc386f2b3df",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 723 bytes

~~~c

void _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011278b0 == 0) {
    DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_011278b0,&DAT_0030f128,1,&DAT_011278d0,
             "com/google/firebase/auth/internal/cpp/JniAuthStateListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdcc8"></a> `00bcdcc8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdccc"></a> `00bcdccc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdcd0"></a> `00bcdcd0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdcd4"></a> `00bcdcd4` | `d4 2a 00 d0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdcd8"></a> `00bcdcd8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bcdcdc"></a> `00bcdcdc` | `81 5a 44 f9` | ldr x1,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdce0"></a> `00bcdce0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcdce4"></a> `00bcdce4` | `41 01 00 b5` | cbnz x1,0x00bcdd0c | `CONDITIONAL_JUMP`
<a id="insn-00bcdce8"></a> `00bcdce8` | `43 b7 ff 90` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdcec"></a> `00bcdcec` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdcf0"></a> `00bcdcf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdcf4"></a> `00bcdcf4` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bcdcf8"></a> `00bcdcf8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcdcfc"></a> `00bcdcfc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bcdd00"></a> `00bcdd00` | `ac 38 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd04"></a> `00bcdd04` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bcdd08"></a> `00bcdd08` | `80 5a 04 f9` | str x0,[x20, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bcdd0c"></a> `00bcdd0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdd10"></a> `00bcdd10` | `02 ba ff d0` | adrp x2,0x30f000 | `FALL_THROUGH`
<a id="insn-00bcdd14"></a> `00bcdd14` | `c4 2a 00 d0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bcdd18"></a> `00bcdd18` | `45 b7 ff 90` | adrp x5,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcdd1c"></a> `00bcdd1c` | `42 a0 04 91` | add x2,x2,#0x128 | `FALL_THROUGH`
<a id="insn-00bcdd20"></a> `00bcdd20` | `84 40 23 91` | add x4,x4,#0x8d0 | `FALL_THROUGH`
<a id="insn-00bcdd24"></a> `00bcdd24` | `a5 a4 33 91` | add x5,x5,#0xce9 | `FALL_THROUGH`
<a id="insn-00bcdd28"></a> `00bcdd28` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdd2c"></a> `00bcdd2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdd30"></a> `00bcdd30` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdd34"></a> `00bcdd34` | `97 38 02 14` | b 0x00c5bf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdcc8`](#insn-00bcdcc8) 範囲 `[['00bcdcc8', '00bcdce7']]`
  - `CONDITIONAL_JUMP` [`00bcdce4`](#insn-00bcdce4) → [`00bcdd0c`](#insn-00bcdd0c)
  - `FALL_THROUGH` [`00bcdce4`](#insn-00bcdce4) → [`00bcdce8`](#insn-00bcdce8)
- ブロック [`00bcdce8`](#insn-00bcdce8) 範囲 `[['00bcdce8', '00bcdd0b']]`
  - `FALL_THROUGH` [`00bcdd08`](#insn-00bcdd08) → [`00bcdd0c`](#insn-00bcdd0c)
- ブロック [`00bcdd0c`](#insn-00bcdd0c) 範囲 `[['00bcdd0c', '00bcdd37']]`

## 命令位置別の参照

- [`00bcdcc8`](#insn-00bcdcc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdccc`](#insn-00bcdccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcdc`](#insn-00bcdcdc) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdce4`](#insn-00bcdce4) → [`00bcdd0c`](#insn-00bcdd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcec`](#insn-00bcdcec) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdd00`](#insn-00bcdd00) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd08`](#insn-00bcdd08) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdd0c`](#insn-00bcdd0c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd1c`](#insn-00bcdd1c) → `0030f128`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd20`](#insn-00bcdd20) → `011278d0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd24`](#insn-00bcdd24) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdd34`](#insn-00bcdd34) → [`00c5bf90`](../00c5b/00c5bf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdcc8`](#insn-00bcdcc8)

~~~json
{
  "source": "00bcdcc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdccc`](#insn-00bcdccc)

~~~json
{
  "source": "00bcdccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcdc`](#insn-00bcdcdc)

~~~json
{
  "source": "00bcdcdc",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdce4`](#insn-00bcdce4)

~~~json
{
  "source": "00bcdce4",
  "target": "00bcdd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcec`](#insn-00bcdcec)

~~~json
{
  "source": "00bcdcec",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcdd00`](#insn-00bcdd00)

~~~json
{
  "source": "00bcdd00",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd08`](#insn-00bcdd08)

~~~json
{
  "source": "00bcdd08",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdd0c`](#insn-00bcdd0c)

~~~json
{
  "source": "00bcdd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd1c`](#insn-00bcdd1c)

~~~json
{
  "source": "00bcdd1c",
  "target": "0030f128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd20`](#insn-00bcdd20)

~~~json
{
  "source": "00bcdd20",
  "target": "011278d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd24`](#insn-00bcdd24)

~~~json
{
  "source": "00bcdd24",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcdd34`](#insn-00bcdd34)

~~~json
{
  "source": "00bcdd34",
  "target": "00c5bf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
