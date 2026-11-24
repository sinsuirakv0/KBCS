# 00bcccd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccc38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccc38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-5143f5f92d648ac52ffdefa5bdacb908)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcdcc8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcd/00bcdcc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-326c57616edab7eeed0b27706d075c72)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcccd4",
  "name": "_ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f2c8d292bc3b10d9e752e47e66db358147aedad26a543e889c904608eabd0ce",
  "source_text_sha256": "5f2c8d292bc3b10d9e752e47e66db358147aedad26a543e889c904608eabd0ce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcccd4",
        "00bccd43"
      ]
    ],
    "bytes_sha256": "4ca3c357af342de4f907aa7229255cff48fdd57a480a5de820fbbd067e7200be",
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

- [00c5afc0](../00c5a/00c5afc0.md)
- [00c5afe0](../00c5a/00c5afe0.md)

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
  if (DAT_011268f0 == 0) {
    DAT_011268f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_011268f0,&DAT_0030f0e8,1,&DAT_01126910,
             "com/google/firebase/auth/internal/cpp/JniAuthStateListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcccd4"></a> `00bcccd4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcccd8"></a> `00bcccd8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcccdc"></a> `00bcccdc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccce0"></a> `00bccce0` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccce4"></a> `00bccce4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bccce8"></a> `00bccce8` | `81 7a 44 f9` | ldr x1,[x20, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bcccec"></a> `00bcccec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcccf0"></a> `00bcccf0` | `41 01 00 b5` | cbnz x1,0x00bccd18 | `CONDITIONAL_JUMP`
<a id="insn-00bcccf4"></a> `00bcccf4` | `43 b7 ff b0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bcccf8"></a> `00bcccf8` | `63 68 30 91` | add x3,x3,#0xc1a | `FALL_THROUGH`
<a id="insn-00bcccfc"></a> `00bcccfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccd00"></a> `00bccd00` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bccd04"></a> `00bccd04` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccd08"></a> `00bccd08` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccd0c"></a> `00bccd0c` | `b5 38 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bccd10"></a> `00bccd10` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bccd14"></a> `00bccd14` | `80 7a 04 f9` | str x0,[x20, #0x8f0] | `FALL_THROUGH`
<a id="insn-00bccd18"></a> `00bccd18` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccd1c"></a> `00bccd1c` | `02 ba ff f0` | adrp x2,0x30f000 | `FALL_THROUGH`
<a id="insn-00bccd20"></a> `00bccd20` | `c4 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccd24"></a> `00bccd24` | `45 b7 ff b0` | adrp x5,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bccd28"></a> `00bccd28` | `42 a0 03 91` | add x2,x2,#0xe8 | `FALL_THROUGH`
<a id="insn-00bccd2c"></a> `00bccd2c` | `84 40 24 91` | add x4,x4,#0x910 | `FALL_THROUGH`
<a id="insn-00bccd30"></a> `00bccd30` | `a5 68 30 91` | add x5,x5,#0xc1a | `FALL_THROUGH`
<a id="insn-00bccd34"></a> `00bccd34` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bccd38"></a> `00bccd38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccd3c"></a> `00bccd3c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccd40"></a> `00bccd40` | `a0 38 02 14` | b 0x00c5afc0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcccd4`](#insn-00bcccd4) 範囲 `[['00bcccd4', '00bcccf3']]`
  - `CONDITIONAL_JUMP` [`00bcccf0`](#insn-00bcccf0) → [`00bccd18`](#insn-00bccd18)
  - `FALL_THROUGH` [`00bcccf0`](#insn-00bcccf0) → [`00bcccf4`](#insn-00bcccf4)
- ブロック [`00bcccf4`](#insn-00bcccf4) 範囲 `[['00bcccf4', '00bccd17']]`
  - `FALL_THROUGH` [`00bccd14`](#insn-00bccd14) → [`00bccd18`](#insn-00bccd18)
- ブロック [`00bccd18`](#insn-00bccd18) 範囲 `[['00bccd18', '00bccd43']]`

## 命令位置別の参照

- [`00bcccd4`](#insn-00bcccd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccd8`](#insn-00bcccd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccce8`](#insn-00bccce8) → `011268f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcccf0`](#insn-00bcccf0) → [`00bccd18`](#insn-00bccd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcccf8`](#insn-00bcccf8) → `002b5c1a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccd0c`](#insn-00bccd0c) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bccd14`](#insn-00bccd14) → `011268f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccd18`](#insn-00bccd18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccd28`](#insn-00bccd28) → `0030f0e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccd2c`](#insn-00bccd2c) → `01126910`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccd30`](#insn-00bccd30) → `002b5c1a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccd40`](#insn-00bccd40) → [`00c5afc0`](../00c5a/00c5afc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afc0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcccd4`](#insn-00bcccd4)

~~~json
{
  "source": "00bcccd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccd8`](#insn-00bcccd8)

~~~json
{
  "source": "00bcccd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccce8`](#insn-00bccce8)

~~~json
{
  "source": "00bccce8",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcccf0`](#insn-00bcccf0)

~~~json
{
  "source": "00bcccf0",
  "target": "00bccd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcccf8`](#insn-00bcccf8)

~~~json
{
  "source": "00bcccf8",
  "target": "002b5c1a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5c1a",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5c1a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccd0c`](#insn-00bccd0c)

~~~json
{
  "source": "00bccd0c",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccd14`](#insn-00bccd14)

~~~json
{
  "source": "00bccd14",
  "target": "011268f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccd18`](#insn-00bccd18)

~~~json
{
  "source": "00bccd18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccd28`](#insn-00bccd28)

~~~json
{
  "source": "00bccd28",
  "target": "0030f0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccd2c`](#insn-00bccd2c)

~~~json
{
  "source": "00bccd2c",
  "target": "01126910",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccd30`](#insn-00bccd30)

~~~json
{
  "source": "00bccd30",
  "target": "002b5c1a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5c1a",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5c1a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccd40`](#insn-00bccd40)

~~~json
{
  "source": "00bccd40",
  "target": "00c5afc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
