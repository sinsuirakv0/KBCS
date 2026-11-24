# 00bccb8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc764.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-edc92816fa3c1ef1daa35ef7391ab502)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bccc28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcc/00bccc28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-de210cef450213c6dc0295eef149d7ee)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccb8c",
  "name": "_ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1674f5aa3a543abc54449c8d653db7691ec5949c69e86875846edb2879369ec",
  "source_text_sha256": "a1674f5aa3a543abc54449c8d653db7691ec5949c69e86875846edb2879369ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccb8c",
        "00bccbfb"
      ]
    ],
    "bytes_sha256": "aea0b4260cc057003c967fa3d7dc7e6a96a96e37caa0f0fab8e792c1e603a9e7",
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

- [00c5af10](../00c5a/00c5af10.md)
- [00c5af30](../00c5a/00c5af30.md)

## 関連文字列（未確認候補）

~~~text
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 934 bytes

~~~c

void _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011267f0 == 0) {
                    /* try { // try from 00bccbbc to 00cccbd3 has its CatchHandler @ 00bce904 */
    DAT_011267f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0);
  }
                    /* try { // try from 00bccbd4 to 00cccc2f has its CatchHandler @ 00bcc5d0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011267f0,&PTR_s_<init>_00c91b50,2,&DAT_01126800,
             "com/google/firebase/auth/internal/cpp/JniAuthStateListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccb8c"></a> `00bccb8c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccb90"></a> `00bccb90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccb94"></a> `00bccb94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccb98"></a> `00bccb98` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccb9c"></a> `00bccb9c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bccba0"></a> `00bccba0` | `81 fa 43 f9` | ldr x1,[x20, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccba4"></a> `00bccba4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccba8"></a> `00bccba8` | `41 01 00 b5` | cbnz x1,0x00bccbd0 | `CONDITIONAL_JUMP`
<a id="insn-00bccbac"></a> `00bccbac` | `43 b7 ff b0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bccbb0"></a> `00bccbb0` | `63 68 2f 91` | add x3,x3,#0xbda | `FALL_THROUGH`
<a id="insn-00bccbb4"></a> `00bccbb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccbb8"></a> `00bccbb8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bccbbc"></a> `00bccbbc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccbc0"></a> `00bccbc0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccbc4"></a> `00bccbc4` | `d3 38 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccbc8"></a> `00bccbc8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bccbcc"></a> `00bccbcc` | `80 fa 03 f9` | str x0,[x20, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bccbd0"></a> `00bccbd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccbd4"></a> `00bccbd4` | `22 06 00 b0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bccbd8"></a> `00bccbd8` | `c4 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccbdc"></a> `00bccbdc` | `45 b7 ff b0` | adrp x5,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bccbe0"></a> `00bccbe0` | `42 40 2d 91` | add x2,x2,#0xb50 | `FALL_THROUGH`
<a id="insn-00bccbe4"></a> `00bccbe4` | `84 00 20 91` | add x4,x4,#0x800 | `FALL_THROUGH`
<a id="insn-00bccbe8"></a> `00bccbe8` | `a5 68 2f 91` | add x5,x5,#0xbda | `FALL_THROUGH`
<a id="insn-00bccbec"></a> `00bccbec` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bccbf0"></a> `00bccbf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccbf4"></a> `00bccbf4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccbf8"></a> `00bccbf8` | `ce 38 02 14` | b 0x00c5af30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccb8c`](#insn-00bccb8c) 範囲 `[['00bccb8c', '00bccbab']]`
  - `CONDITIONAL_JUMP` [`00bccba8`](#insn-00bccba8) → [`00bccbd0`](#insn-00bccbd0)
  - `FALL_THROUGH` [`00bccba8`](#insn-00bccba8) → [`00bccbac`](#insn-00bccbac)
- ブロック [`00bccbac`](#insn-00bccbac) 範囲 `[['00bccbac', '00bccbbb']]`
  - `FALL_THROUGH` [`00bccbb8`](#insn-00bccbb8) → [`00bccbbc`](#insn-00bccbbc)
- ブロック [`00bccbbc`](#insn-00bccbbc) 範囲 `[['00bccbbc', '00bccbcf']]`
  - `FALL_THROUGH` [`00bccbcc`](#insn-00bccbcc) → [`00bccbd0`](#insn-00bccbd0)
- ブロック [`00bccbd0`](#insn-00bccbd0) 範囲 `[['00bccbd0', '00bccbd3']]`
  - `FALL_THROUGH` [`00bccbd0`](#insn-00bccbd0) → [`00bccbd4`](#insn-00bccbd4)
- ブロック [`00bccbd4`](#insn-00bccbd4) 範囲 `[['00bccbd4', '00bccbfb']]`

## 命令位置別の参照

- [`00bccb8c`](#insn-00bccb8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb90`](#insn-00bccb90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccba0`](#insn-00bccba0) → `011267f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccba8`](#insn-00bccba8) → [`00bccbd0`](#insn-00bccbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbb0`](#insn-00bccbb0) → `002b5bda`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccbc4`](#insn-00bccbc4) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bccbcc`](#insn-00bccbcc) → `011267f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccbd0`](#insn-00bccbd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccbe0`](#insn-00bccbe0) → `00c91b50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bccbe4`](#insn-00bccbe4) → `01126800`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccbe8`](#insn-00bccbe8) → `002b5bda`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccbf8`](#insn-00bccbf8) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccb8c`](#insn-00bccb8c)

~~~json
{
  "source": "00bccb8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb90`](#insn-00bccb90)

~~~json
{
  "source": "00bccb90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccba0`](#insn-00bccba0)

~~~json
{
  "source": "00bccba0",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccba8`](#insn-00bccba8)

~~~json
{
  "source": "00bccba8",
  "target": "00bccbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbb0`](#insn-00bccbb0)

~~~json
{
  "source": "00bccbb0",
  "target": "002b5bda",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5bda",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5bda",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccbc4`](#insn-00bccbc4)

~~~json
{
  "source": "00bccbc4",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccbcc`](#insn-00bccbcc)

~~~json
{
  "source": "00bccbcc",
  "target": "011267f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccbd0`](#insn-00bccbd0)

~~~json
{
  "source": "00bccbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccbe0`](#insn-00bccbe0)

~~~json
{
  "source": "00bccbe0",
  "target": "00c91b50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91b50",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bccbe4`](#insn-00bccbe4)

~~~json
{
  "source": "00bccbe4",
  "target": "01126800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126800",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccbe8`](#insn-00bccbe8)

~~~json
{
  "source": "00bccbe8",
  "target": "002b5bda",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5bda",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5bda",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccbf8`](#insn-00bccbf8)

~~~json
{
  "source": "00bccbf8",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
