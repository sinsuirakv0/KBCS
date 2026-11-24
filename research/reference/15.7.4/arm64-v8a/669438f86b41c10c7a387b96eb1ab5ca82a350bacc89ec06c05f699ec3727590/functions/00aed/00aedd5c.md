# 00aedd5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aedd18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-1e6230e7fee5ce7636ee54a5e26aabcf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4dae0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4d/00b4dae0.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-42bd8ec937d74c9559df2767d03654a0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedd5c",
  "name": "_ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "764123b9d7436e6f8292e1f369d2ea3c482ea8747a1995e727d901313a9b4316",
  "source_text_sha256": "764123b9d7436e6f8292e1f369d2ea3c482ea8747a1995e727d901313a9b4316",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedd5c",
        "00aeddf7"
      ]
    ],
    "bytes_sha256": "d6c9cb8f335d5c6eee636df9a81273e42e2e922a5cb6dd23cdc726380d690da3",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 601 bytes

~~~c

bool _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0a68 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0a60,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0a68 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0a68;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedd5c"></a> `00aedd5c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aedd60"></a> `00aedd60` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedd64"></a> `00aedd64` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aedd68"></a> `00aedd68` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aedd6c"></a> `00aedd6c` | `95 2d 00 f0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd70"></a> `00aedd70` | `a8 a2 69 39` | ldrb w8,[x21, #0xa68] | `FALL_THROUGH`
<a id="insn-00aedd74"></a> `00aedd74` | `68 00 00 34` | cbz w8,0x00aedd80 | `CONDITIONAL_JUMP`
<a id="insn-00aedd78"></a> `00aedd78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aedd7c"></a> `00aedd7c` | `1b 00 00 14` | b 0x00aedde8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aedd80"></a> `00aedd80` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aedd84"></a> `00aedd84` | `89 2d 00 f0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedd88"></a> `00aedd88` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aedd8c"></a> `00aedd8c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aedd90"></a> `00aedd90` | `21 31 45 f9` | ldr x1,[x9, #0xa60] | `FALL_THROUGH`
<a id="insn-00aedd94"></a> `00aedd94` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aedd98"></a> `00aedd98` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedd9c"></a> `00aedd9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedda0"></a> `00aedda0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aedda4"></a> `00aedda4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aedda8"></a> `00aedda8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddac"></a> `00aeddac` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aeddb0"></a> `00aeddb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeddb4"></a> `00aeddb4` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aeddb8"></a> `00aeddb8` | `20 01 00 54` | b.eq 0x00aedddc | `CONDITIONAL_JUMP`
<a id="insn-00aeddbc"></a> `00aeddbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeddc0"></a> `00aeddc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddc4"></a> `00aeddc4` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeddc8"></a> `00aeddc8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeddcc"></a> `00aeddcc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeddd0"></a> `00aeddd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeddd4"></a> `00aeddd4` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aeddd8"></a> `00aeddd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aedddc"></a> `00aedddc` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aedde0"></a> `00aedde0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aedde4"></a> `00aedde4` | `a0 a2 29 39` | strb w0,[x21, #0xa68] | `FALL_THROUGH`
<a id="insn-00aedde8"></a> `00aedde8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeddec"></a> `00aeddec` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeddf0"></a> `00aeddf0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aeddf4"></a> `00aeddf4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedd5c`](#insn-00aedd5c) 範囲 `[['00aedd5c', '00aedd77']]`
  - `CONDITIONAL_JUMP` [`00aedd74`](#insn-00aedd74) → [`00aedd80`](#insn-00aedd80)
  - `FALL_THROUGH` [`00aedd74`](#insn-00aedd74) → [`00aedd78`](#insn-00aedd78)
- ブロック [`00aedd78`](#insn-00aedd78) 範囲 `[['00aedd78', '00aedd7f']]`
  - `UNCONDITIONAL_JUMP` [`00aedd7c`](#insn-00aedd7c) → [`00aedde8`](#insn-00aedde8)
- ブロック [`00aedd80`](#insn-00aedd80) 範囲 `[['00aedd80', '00aeddbb']]`
  - `CONDITIONAL_JUMP` [`00aeddb8`](#insn-00aeddb8) → [`00aedddc`](#insn-00aedddc)
  - `FALL_THROUGH` [`00aeddb8`](#insn-00aeddb8) → [`00aeddbc`](#insn-00aeddbc)
- ブロック [`00aeddbc`](#insn-00aeddbc) 範囲 `[['00aeddbc', '00aedddb']]`
  - `FALL_THROUGH` [`00aeddd8`](#insn-00aeddd8) → [`00aedddc`](#insn-00aedddc)
- ブロック [`00aedddc`](#insn-00aedddc) 範囲 `[['00aedddc', '00aedde7']]`
  - `FALL_THROUGH` [`00aedde4`](#insn-00aedde4) → [`00aedde8`](#insn-00aedde8)
- ブロック [`00aedde8`](#insn-00aedde8) 範囲 `[['00aedde8', '00aeddf7']]`

## 命令位置別の参照

- [`00aedd5c`](#insn-00aedd5c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd60`](#insn-00aedd60) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd64`](#insn-00aedd64) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd70`](#insn-00aedd70) → `010a0a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aedd74`](#insn-00aedd74) → [`00aedd80`](#insn-00aedd80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd7c`](#insn-00aedd7c) → [`00aedde8`](#insn-00aedde8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedd90`](#insn-00aedd90) → `010a0a60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeddb8`](#insn-00aeddb8) → [`00aedddc`](#insn-00aedddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedde4`](#insn-00aedde4) → `010a0a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aedde8`](#insn-00aedde8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeddec`](#insn-00aeddec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedd5c`](#insn-00aedd5c)

~~~json
{
  "source": "00aedd5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd60`](#insn-00aedd60)

~~~json
{
  "source": "00aedd60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd64`](#insn-00aedd64)

~~~json
{
  "source": "00aedd64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd70`](#insn-00aedd70)

~~~json
{
  "source": "00aedd70",
  "target": "010a0a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedd74`](#insn-00aedd74)

~~~json
{
  "source": "00aedd74",
  "target": "00aedd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd7c`](#insn-00aedd7c)

~~~json
{
  "source": "00aedd7c",
  "target": "00aedde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedd90`](#insn-00aedd90)

~~~json
{
  "source": "00aedd90",
  "target": "010a0a60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeddb8`](#insn-00aeddb8)

~~~json
{
  "source": "00aeddb8",
  "target": "00aedddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedde4`](#insn-00aedde4)

~~~json
{
  "source": "00aedde4",
  "target": "010a0a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a68",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedde8`](#insn-00aedde8)

~~~json
{
  "source": "00aedde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeddec`](#insn-00aeddec)

~~~json
{
  "source": "00aeddec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
