# 00aeae2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aead64`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aead64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-32cc821a791afdf9b9d5c3e7475dad92)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeae70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-908949e0a082d4f046829cb02034c5ec)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeae2c",
  "name": "_ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2143cce59006ce100954b483854bbb002173e1fc9e722566a9c2206d76f8ba59",
  "source_text_sha256": "2143cce59006ce100954b483854bbb002173e1fc9e722566a9c2206d76f8ba59",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeae2c",
        "00aeaecb"
      ]
    ],
    "bytes_sha256": "50d7fd0ba11cdd74368e8919a69489ea52a8dfb64a9ea9c8c754eb644b811507",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 508 bytes

~~~c

void _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a0810 != 0) {
    if (DAT_010a0818 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a0818 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a0810);
    DAT_010a0810 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeae2c"></a> `00aeae2c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeae30"></a> `00aeae30` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeae34"></a> `00aeae34` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeae38"></a> `00aeae38` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeae3c"></a> `00aeae3c` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeae40"></a> `00aeae40` | `81 0a 44 f9` | ldr x1,[x20, #0x810] | `FALL_THROUGH`
<a id="insn-00aeae44"></a> `00aeae44` | `c1 03 00 b4` | cbz x1,0x00aeaebc | `CONDITIONAL_JUMP`
<a id="insn-00aeae48"></a> `00aeae48` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeae4c"></a> `00aeae4c` | `a8 62 60 39` | ldrb w8,[x21, #0x818] | `FALL_THROUGH`
<a id="insn-00aeae50"></a> `00aeae50` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeae54"></a> `00aeae54` | `c8 00 00 34` | cbz w8,0x00aeae6c | `CONDITIONAL_JUMP`
<a id="insn-00aeae58"></a> `00aeae58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae5c"></a> `00aeae5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae60"></a> `00aeae60` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aeae64"></a> `00aeae64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae68"></a> `00aeae68` | `bf 62 20 39` | strb wzr,[x21, #0x818] | `FALL_THROUGH`
<a id="insn-00aeae6c"></a> `00aeae6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae70"></a> `00aeae70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae74"></a> `00aeae74` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeae78"></a> `00aeae78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae7c"></a> `00aeae7c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeae80"></a> `00aeae80` | `20 01 00 54` | b.eq 0x00aeaea4 | `CONDITIONAL_JUMP`
<a id="insn-00aeae84"></a> `00aeae84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae88"></a> `00aeae88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae8c"></a> `00aeae8c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeae90"></a> `00aeae90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeae94"></a> `00aeae94` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeae98"></a> `00aeae98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeae9c"></a> `00aeae9c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeaea0"></a> `00aeaea0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaea4"></a> `00aeaea4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeaea8"></a> `00aeaea8` | `81 0a 44 f9` | ldr x1,[x20, #0x810] | `FALL_THROUGH`
<a id="insn-00aeaeac"></a> `00aeaeac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaeb0"></a> `00aeaeb0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeaeb4"></a> `00aeaeb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeaeb8"></a> `00aeaeb8` | `9f 0a 04 f9` | str xzr,[x20, #0x810] | `FALL_THROUGH`
<a id="insn-00aeaebc"></a> `00aeaebc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeaec0"></a> `00aeaec0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaec4"></a> `00aeaec4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeaec8"></a> `00aeaec8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeae2c`](#insn-00aeae2c) 範囲 `[['00aeae2c', '00aeae47']]`
  - `CONDITIONAL_JUMP` [`00aeae44`](#insn-00aeae44) → [`00aeaebc`](#insn-00aeaebc)
  - `FALL_THROUGH` [`00aeae44`](#insn-00aeae44) → [`00aeae48`](#insn-00aeae48)
- ブロック [`00aeae48`](#insn-00aeae48) 範囲 `[['00aeae48', '00aeae57']]`
  - `CONDITIONAL_JUMP` [`00aeae54`](#insn-00aeae54) → [`00aeae6c`](#insn-00aeae6c)
  - `FALL_THROUGH` [`00aeae54`](#insn-00aeae54) → [`00aeae58`](#insn-00aeae58)
- ブロック [`00aeae58`](#insn-00aeae58) 範囲 `[['00aeae58', '00aeae6b']]`
  - `FALL_THROUGH` [`00aeae68`](#insn-00aeae68) → [`00aeae6c`](#insn-00aeae6c)
- ブロック [`00aeae6c`](#insn-00aeae6c) 範囲 `[['00aeae6c', '00aeae83']]`
  - `CONDITIONAL_JUMP` [`00aeae80`](#insn-00aeae80) → [`00aeaea4`](#insn-00aeaea4)
  - `FALL_THROUGH` [`00aeae80`](#insn-00aeae80) → [`00aeae84`](#insn-00aeae84)
- ブロック [`00aeae84`](#insn-00aeae84) 範囲 `[['00aeae84', '00aeaea3']]`
  - `FALL_THROUGH` [`00aeaea0`](#insn-00aeaea0) → [`00aeaea4`](#insn-00aeaea4)
- ブロック [`00aeaea4`](#insn-00aeaea4) 範囲 `[['00aeaea4', '00aeaebb']]`
  - `FALL_THROUGH` [`00aeaeb8`](#insn-00aeaeb8) → [`00aeaebc`](#insn-00aeaebc)
- ブロック [`00aeaebc`](#insn-00aeaebc) 範囲 `[['00aeaebc', '00aeaecb']]`

## 命令位置別の参照

- [`00aeae2c`](#insn-00aeae2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae30`](#insn-00aeae30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae34`](#insn-00aeae34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae40`](#insn-00aeae40) → `010a0810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeae44`](#insn-00aeae44) → [`00aeaebc`](#insn-00aeaebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae4c`](#insn-00aeae4c) → `010a0818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeae54`](#insn-00aeae54) → [`00aeae6c`](#insn-00aeae6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeae68`](#insn-00aeae68) → `010a0818`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeae80`](#insn-00aeae80) → [`00aeaea4`](#insn-00aeaea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaea8`](#insn-00aeaea8) → `010a0810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaeb8`](#insn-00aeaeb8) → `010a0810`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaebc`](#insn-00aeaebc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaec0`](#insn-00aeaec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeae2c`](#insn-00aeae2c)

~~~json
{
  "source": "00aeae2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae30`](#insn-00aeae30)

~~~json
{
  "source": "00aeae30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae34`](#insn-00aeae34)

~~~json
{
  "source": "00aeae34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae40`](#insn-00aeae40)

~~~json
{
  "source": "00aeae40",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeae44`](#insn-00aeae44)

~~~json
{
  "source": "00aeae44",
  "target": "00aeaebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae4c`](#insn-00aeae4c)

~~~json
{
  "source": "00aeae4c",
  "target": "010a0818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0818",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeae54`](#insn-00aeae54)

~~~json
{
  "source": "00aeae54",
  "target": "00aeae6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeae68`](#insn-00aeae68)

~~~json
{
  "source": "00aeae68",
  "target": "010a0818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0818",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeae80`](#insn-00aeae80)

~~~json
{
  "source": "00aeae80",
  "target": "00aeaea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaea8`](#insn-00aeaea8)

~~~json
{
  "source": "00aeaea8",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaeb8`](#insn-00aeaeb8)

~~~json
{
  "source": "00aeaeb8",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaebc`](#insn-00aeaebc)

~~~json
{
  "source": "00aeaebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaec0`](#insn-00aeaec0)

~~~json
{
  "source": "00aeaec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
