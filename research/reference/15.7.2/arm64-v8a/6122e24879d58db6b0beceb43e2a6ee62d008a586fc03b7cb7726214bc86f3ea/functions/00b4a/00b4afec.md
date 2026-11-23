# 00b4afec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4b0b4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0067.md#compare-eeec7e655c9d647a8741281cb0036b3e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4afec",
  "name": "_ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2dcba016422c37eba8a4cc7b071a5d9ea7b09013204c6ab10ba8fc1d8cb1e7cc",
  "source_text_sha256": "2dcba016422c37eba8a4cc7b071a5d9ea7b09013204c6ab10ba8fc1d8cb1e7cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4afec",
        "00b4b05b"
      ]
    ],
    "bytes_sha256": "208ec7bfe488f07902e1e57274c473386f86191d2eb6b4d084dbc2513fbec2b4",
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
"%PG%com/google/firebase/messaging/cpp/RegistrationIntentService"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1037 bytes

~~~c

void _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00b4b000 to 00c4b00b has its CatchHandler @ 00b4b140 */
  if (DAT_010a0f58 == 0) {
    DAT_010a0f58 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/messaging/cpp/RegistrationIntentService",0);
  }
                    /* try { // try from 00b4b030 to 00c4b03b has its CatchHandler @ 00b4b13c */
                    /* try { // try from 00b4b054 to 00c4b05f has its CatchHandler @ 00b4b138 */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0f58,&DAT_002f8900,1,&DAT_010a0f70,
             "com/google/firebase/messaging/cpp/RegistrationIntentService");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4afec"></a> `00b4afec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4aff0"></a> `00b4aff0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4aff4"></a> `00b4aff4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4aff8"></a> `00b4aff8` | `b4 2a 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4affc"></a> `00b4affc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b4b000"></a> `00b4b000` | `81 ae 47 f9` | ldr x1,[x20, #0xf58] | `FALL_THROUGH`
<a id="insn-00b4b004"></a> `00b4b004` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4b008"></a> `00b4b008` | `41 01 00 b5` | cbnz x1,0x00b4b030 | `CONDITIONAL_JUMP`
<a id="insn-00b4b00c"></a> `00b4b00c` | `e3 ba ff b0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4b010"></a> `00b4b010` | `63 68 3a 91` | add x3,x3,#0xe9a | `FALL_THROUGH`
<a id="insn-00b4b014"></a> `00b4b014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4b018"></a> `00b4b018` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b4b01c"></a> `00b4b01c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4b020"></a> `00b4b020` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4b024"></a> `00b4b024` | `db 4b 02 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b4b028"></a> `00b4b028` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b4b02c"></a> `00b4b02c` | `80 ae 07 f9` | str x0,[x20, #0xf58] | `FALL_THROUGH`
<a id="insn-00b4b030"></a> `00b4b030` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4b034"></a> `00b4b034` | `62 bd ff b0` | adrp x2,0x2f8000 | `FALL_THROUGH`
<a id="insn-00b4b038"></a> `00b4b038` | `a4 2a 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00b4b03c"></a> `00b4b03c` | `e5 ba ff b0` | adrp x5,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4b040"></a> `00b4b040` | `42 00 24 91` | add x2,x2,#0x900 | `FALL_THROUGH`
<a id="insn-00b4b044"></a> `00b4b044` | `84 c0 3d 91` | add x4,x4,#0xf70 | `FALL_THROUGH`
<a id="insn-00b4b048"></a> `00b4b048` | `a5 68 3a 91` | add x5,x5,#0xe9a | `FALL_THROUGH`
<a id="insn-00b4b04c"></a> `00b4b04c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00b4b050"></a> `00b4b050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4b054"></a> `00b4b054` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4b058"></a> `00b4b058` | `c6 4b 02 14` | b 0x00bddf70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4afec`](#insn-00b4afec) 範囲 `[['00b4afec', '00b4afff']]`
  - `FALL_THROUGH` [`00b4affc`](#insn-00b4affc) → [`00b4b000`](#insn-00b4b000)
- ブロック [`00b4b000`](#insn-00b4b000) 範囲 `[['00b4b000', '00b4b00b']]`
  - `CONDITIONAL_JUMP` [`00b4b008`](#insn-00b4b008) → [`00b4b030`](#insn-00b4b030)
  - `FALL_THROUGH` [`00b4b008`](#insn-00b4b008) → [`00b4b00c`](#insn-00b4b00c)
- ブロック [`00b4b00c`](#insn-00b4b00c) 範囲 `[['00b4b00c', '00b4b02f']]`
  - `FALL_THROUGH` [`00b4b02c`](#insn-00b4b02c) → [`00b4b030`](#insn-00b4b030)
- ブロック [`00b4b030`](#insn-00b4b030) 範囲 `[['00b4b030', '00b4b053']]`
  - `FALL_THROUGH` [`00b4b050`](#insn-00b4b050) → [`00b4b054`](#insn-00b4b054)
- ブロック [`00b4b054`](#insn-00b4b054) 範囲 `[['00b4b054', '00b4b05b']]`

## 命令位置別の参照

- [`00b4afec`](#insn-00b4afec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4aff0`](#insn-00b4aff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b000`](#insn-00b4b000) → `010a0f58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4b008`](#insn-00b4b008) → [`00b4b030`](#insn-00b4b030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b010`](#insn-00b4b010) → `002a8e9a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4b024`](#insn-00b4b024) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b4b02c`](#insn-00b4b02c) → `010a0f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4b030`](#insn-00b4b030) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b040`](#insn-00b4b040) → `002f8900`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b044`](#insn-00b4b044) → `010a0f70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4b048`](#insn-00b4b048) → `002a8e9a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4b058`](#insn-00b4b058) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4afec`](#insn-00b4afec)

~~~json
{
  "source": "00b4afec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4aff0`](#insn-00b4aff0)

~~~json
{
  "source": "00b4aff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b000`](#insn-00b4b000)

~~~json
{
  "source": "00b4b000",
  "target": "010a0f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b008`](#insn-00b4b008)

~~~json
{
  "source": "00b4b008",
  "target": "00b4b030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b010`](#insn-00b4b010)

~~~json
{
  "source": "00b4b010",
  "target": "002a8e9a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8e96",
  "offset": 4,
  "size": 64,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002a8e96",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4b024`](#insn-00b4b024)

~~~json
{
  "source": "00b4b024",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4b02c`](#insn-00b4b02c)

~~~json
{
  "source": "00b4b02c",
  "target": "010a0f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4b030`](#insn-00b4b030)

~~~json
{
  "source": "00b4b030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b040`](#insn-00b4b040)

~~~json
{
  "source": "00b4b040",
  "target": "002f8900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b044`](#insn-00b4b044)

~~~json
{
  "source": "00b4b044",
  "target": "010a0f70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4b048`](#insn-00b4b048)

~~~json
{
  "source": "00b4b048",
  "target": "002a8e9a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8e96",
  "offset": 4,
  "size": 64,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002a8e96",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b4b058`](#insn-00b4b058)

~~~json
{
  "source": "00b4b058",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
