# 00aebca4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebd6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-a5a2174ccaeb00e99dd3c05601fd8b82)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebca4",
  "name": "_ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5aa4a5bf8c3d7e5983d3be90916d25247fcb31adef954068a37200aa30075d27",
  "source_text_sha256": "5aa4a5bf8c3d7e5983d3be90916d25247fcb31adef954068a37200aa30075d27",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebca4",
        "00aebd13"
      ]
    ],
    "bytes_sha256": "dd5abdb44390613ffb8caf2d2449cd2115660227031dd261f54e536eec22566e",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 806 bytes

~~~c

void _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aebcb0 to 00bebcc3 has its CatchHandler @ 00af19a4 */
  if (DAT_010a07f8 == 0) {
                    /* try { // try from 00aebcc4 to 00bebcdb has its CatchHandler @ 00af1978 */
    DAT_010a07f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a07f8,&PTR_s_hasNext_00c10390,2,&DAT_010a0808,"java/util/Iterator");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebca4"></a> `00aebca4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebca8"></a> `00aebca8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebcac"></a> `00aebcac` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebcb0"></a> `00aebcb0` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebcb4"></a> `00aebcb4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aebcb8"></a> `00aebcb8` | `81 fe 43 f9` | ldr x1,[x20, #0x7f8] | `FALL_THROUGH`
<a id="insn-00aebcbc"></a> `00aebcbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebcc0"></a> `00aebcc0` | `41 01 00 b5` | cbnz x1,0x00aebce8 | `CONDITIONAL_JUMP`
<a id="insn-00aebcc4"></a> `00aebcc4` | `63 bd ff 90` | adrp x3,0x297000 | `FALL_THROUGH`
<a id="insn-00aebcc8"></a> `00aebcc8` | `63 68 13 91` | add x3,x3,#0x4da | `FALL_THROUGH`
<a id="insn-00aebccc"></a> `00aebccc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebcd0"></a> `00aebcd0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aebcd4"></a> `00aebcd4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebcd8"></a> `00aebcd8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebcdc"></a> `00aebcdc` | `ad c8 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aebce0"></a> `00aebce0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebce4"></a> `00aebce4` | `80 fe 03 f9` | str x0,[x20, #0x7f8] | `FALL_THROUGH`
<a id="insn-00aebce8"></a> `00aebce8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebcec"></a> `00aebcec` | `22 09 00 b0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aebcf0"></a> `00aebcf0` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebcf4"></a> `00aebcf4` | `65 bd ff 90` | adrp x5,0x297000 | `FALL_THROUGH`
<a id="insn-00aebcf8"></a> `00aebcf8` | `42 40 0e 91` | add x2,x2,#0x390 | `FALL_THROUGH`
<a id="insn-00aebcfc"></a> `00aebcfc` | `84 20 20 91` | add x4,x4,#0x808 | `FALL_THROUGH`
<a id="insn-00aebd00"></a> `00aebd00` | `a5 68 13 91` | add x5,x5,#0x4da | `FALL_THROUGH`
<a id="insn-00aebd04"></a> `00aebd04` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00aebd08"></a> `00aebd08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebd0c"></a> `00aebd0c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebd10"></a> `00aebd10` | `a8 c8 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebca4`](#insn-00aebca4) 範囲 `[['00aebca4', '00aebcaf']]`
  - `FALL_THROUGH` [`00aebcac`](#insn-00aebcac) → [`00aebcb0`](#insn-00aebcb0)
- ブロック [`00aebcb0`](#insn-00aebcb0) 範囲 `[['00aebcb0', '00aebcc3']]`
  - `CONDITIONAL_JUMP` [`00aebcc0`](#insn-00aebcc0) → [`00aebce8`](#insn-00aebce8)
  - `FALL_THROUGH` [`00aebcc0`](#insn-00aebcc0) → [`00aebcc4`](#insn-00aebcc4)
- ブロック [`00aebcc4`](#insn-00aebcc4) 範囲 `[['00aebcc4', '00aebce7']]`
  - `FALL_THROUGH` [`00aebce4`](#insn-00aebce4) → [`00aebce8`](#insn-00aebce8)
- ブロック [`00aebce8`](#insn-00aebce8) 範囲 `[['00aebce8', '00aebd13']]`

## 命令位置別の参照

- [`00aebca4`](#insn-00aebca4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebca8`](#insn-00aebca8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcb8`](#insn-00aebcb8) → `010a07f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebcc0`](#insn-00aebcc0) → [`00aebce8`](#insn-00aebce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcc8`](#insn-00aebcc8) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebcdc`](#insn-00aebcdc) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aebce4`](#insn-00aebce4) → `010a07f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebce8`](#insn-00aebce8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebcf8`](#insn-00aebcf8) → `00c10390`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aebcfc`](#insn-00aebcfc) → `010a0808`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebd00`](#insn-00aebd00) → `002974da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebd10`](#insn-00aebd10) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebca4`](#insn-00aebca4)

~~~json
{
  "source": "00aebca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebca8`](#insn-00aebca8)

~~~json
{
  "source": "00aebca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcb8`](#insn-00aebcb8)

~~~json
{
  "source": "00aebcb8",
  "target": "010a07f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebcc0`](#insn-00aebcc0)

~~~json
{
  "source": "00aebcc0",
  "target": "00aebce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcc8`](#insn-00aebcc8)

~~~json
{
  "source": "00aebcc8",
  "target": "002974da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002974da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebcdc`](#insn-00aebcdc)

~~~json
{
  "source": "00aebcdc",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebce4`](#insn-00aebce4)

~~~json
{
  "source": "00aebce4",
  "target": "010a07f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebce8`](#insn-00aebce8)

~~~json
{
  "source": "00aebce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebcf8`](#insn-00aebcf8)

~~~json
{
  "source": "00aebcf8",
  "target": "00c10390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10390",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aebcfc`](#insn-00aebcfc)

~~~json
{
  "source": "00aebcfc",
  "target": "010a0808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebd00`](#insn-00aebd00)

~~~json
{
  "source": "00aebd00",
  "target": "002974da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002974da",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002974da",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebd10`](#insn-00aebd10)

~~~json
{
  "source": "00aebd10",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
