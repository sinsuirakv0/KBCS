# 00b5cebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5cf84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0069.md#compare-454cc4392e53ffbfc1c4ee898abee0ab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cebc",
  "name": "_ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "627d3ee56ec0e22690632ad878b4ef97d0f210ff5f69b36acc90ce16f2542c6d",
  "source_text_sha256": "627d3ee56ec0e22690632ad878b4ef97d0f210ff5f69b36acc90ce16f2542c6d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cebc",
        "00b5cf2b"
      ]
    ],
    "bytes_sha256": "e0471dd63cc9f0e5d6eb2faf7c89d3b2effd04775f4809e468df2657b7ab3a40",
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

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 708 bytes

~~~c

void _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a13c8 == 0) {
    DAT_010a13c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult",0
                             );
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a13c8,&DAT_002f9220,1,&DAT_010a13e0,
             "com/google/firebase/auth/SignInMethodQueryResult");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cebc"></a> `00b5cebc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b5cec0"></a> `00b5cec0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cec4"></a> `00b5cec4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b5cec8"></a> `00b5cec8` | `34 2a 00 b0` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5cecc"></a> `00b5cecc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b5ced0"></a> `00b5ced0` | `81 e6 41 f9` | ldr x1,[x20, #0x3c8] | `FALL_THROUGH`
<a id="insn-00b5ced4"></a> `00b5ced4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5ced8"></a> `00b5ced8` | `41 01 00 b5` | cbnz x1,0x00b5cf00 | `CONDITIONAL_JUMP`
<a id="insn-00b5cedc"></a> `00b5cedc` | `a3 b9 ff f0` | adrp x3,0x293000 | `FALL_THROUGH`
<a id="insn-00b5cee0"></a> `00b5cee0` | `63 38 10 91` | add x3,x3,#0x40e | `FALL_THROUGH`
<a id="insn-00b5cee4"></a> `00b5cee4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cee8"></a> `00b5cee8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b5ceec"></a> `00b5ceec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b5cef0"></a> `00b5cef0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b5cef4"></a> `00b5cef4` | `27 04 02 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cef8"></a> `00b5cef8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b5cefc"></a> `00b5cefc` | `80 e6 01 f9` | str x0,[x20, #0x3c8] | `FALL_THROUGH`
<a id="insn-00b5cf00"></a> `00b5cf00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cf04"></a> `00b5cf04` | `e2 bc ff b0` | adrp x2,0x2f9000 | `FALL_THROUGH`
<a id="insn-00b5cf08"></a> `00b5cf08` | `24 2a 00 b0` | adrp x4,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5cf0c"></a> `00b5cf0c` | `a5 b9 ff f0` | adrp x5,0x293000 | `FALL_THROUGH`
<a id="insn-00b5cf10"></a> `00b5cf10` | `42 80 08 91` | add x2,x2,#0x220 | `FALL_THROUGH`
<a id="insn-00b5cf14"></a> `00b5cf14` | `84 80 0f 91` | add x4,x4,#0x3e0 | `FALL_THROUGH`
<a id="insn-00b5cf18"></a> `00b5cf18` | `a5 38 10 91` | add x5,x5,#0x40e | `FALL_THROUGH`
<a id="insn-00b5cf1c"></a> `00b5cf1c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cf20"></a> `00b5cf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cf24"></a> `00b5cf24` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5cf28"></a> `00b5cf28` | `12 04 02 14` | b 0x00bddf70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5cebc`](#insn-00b5cebc) 範囲 `[['00b5cebc', '00b5cedb']]`
  - `CONDITIONAL_JUMP` [`00b5ced8`](#insn-00b5ced8) → [`00b5cf00`](#insn-00b5cf00)
  - `FALL_THROUGH` [`00b5ced8`](#insn-00b5ced8) → [`00b5cedc`](#insn-00b5cedc)
- ブロック [`00b5cedc`](#insn-00b5cedc) 範囲 `[['00b5cedc', '00b5ceff']]`
  - `FALL_THROUGH` [`00b5cefc`](#insn-00b5cefc) → [`00b5cf00`](#insn-00b5cf00)
- ブロック [`00b5cf00`](#insn-00b5cf00) 範囲 `[['00b5cf00', '00b5cf2b']]`

## 命令位置別の参照

- [`00b5cebc`](#insn-00b5cebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cec0`](#insn-00b5cec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ced0`](#insn-00b5ced0) → `010a13c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ced8`](#insn-00b5ced8) → [`00b5cf00`](#insn-00b5cf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee0`](#insn-00b5cee0) → `0029340e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b5cef4`](#insn-00b5cef4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b5cefc`](#insn-00b5cefc) → `010a13c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cf00`](#insn-00b5cf00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf10`](#insn-00b5cf10) → `002f9220`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf14`](#insn-00b5cf14) → `010a13e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf18`](#insn-00b5cf18) → `0029340e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b5cf28`](#insn-00b5cf28) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cebc`](#insn-00b5cebc)

~~~json
{
  "source": "00b5cebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cec0`](#insn-00b5cec0)

~~~json
{
  "source": "00b5cec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ced0`](#insn-00b5ced0)

~~~json
{
  "source": "00b5ced0",
  "target": "010a13c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a13c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ced8`](#insn-00b5ced8)

~~~json
{
  "source": "00b5ced8",
  "target": "00b5cf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cee0`](#insn-00b5cee0)

~~~json
{
  "source": "00b5cee0",
  "target": "0029340e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029340a",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "0029340a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b5cef4`](#insn-00b5cef4)

~~~json
{
  "source": "00b5cef4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cefc`](#insn-00b5cefc)

~~~json
{
  "source": "00b5cefc",
  "target": "010a13c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a13c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cf00`](#insn-00b5cf00)

~~~json
{
  "source": "00b5cf00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf10`](#insn-00b5cf10)

~~~json
{
  "source": "00b5cf10",
  "target": "002f9220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf14`](#insn-00b5cf14)

~~~json
{
  "source": "00b5cf14",
  "target": "010a13e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf18`](#insn-00b5cf18)

~~~json
{
  "source": "00b5cf18",
  "target": "0029340e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029340a",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "0029340a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b5cf28`](#insn-00b5cf28)

~~~json
{
  "source": "00b5cf28",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
