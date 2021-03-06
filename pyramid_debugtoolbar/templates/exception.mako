<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">

<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>${title} // Werkzeug Debugger</title>
    <link rel="stylesheet" href="${static_path}css/debugger.css"
          type="text/css">
    <script type="text/javascript"
          src="${static_path}js/jquery-1.6.4.min.js"></script>
    <script type="text/javascript">var jq = jQuery.noConflict(true);</script>
    <script type="text/javascript"
          src="${static_path}js/debugger.js"></script>
    <script type="text/javascript">
      var TRACEBACK = ${traceback_id},
          DEBUGGER_TOKEN = "${token}",
          CONSOLE_MODE = ${console},
          EVALEX = ${evalex},
          DEBUG_TOOLBAR_STATIC_PATH = "${static_path}",
          DEBUG_TOOLBAR_ROOT_PATH = "${root_path}";
    </script>
  </head>
  <body>
    <div class="debugger">

    <h1>${exception_type}</h1>
    <div class="detail">
      <pre class= "errormsg">${exception|n}</pre>
    </div>
    <h2 class="traceback">Traceback <em>(most recent call last)</em></h2>
    ${summary|n}
    <div class="plain">
      <p>
        <input type="hidden" name="language" value="pytb">
          This is the Copy/Paste friendly version of the traceback.
        </p>
        <textarea cols="50" rows="10" name="code"
                  readonly>${plaintext}</textarea>
      </div>

    <div class="explanation">
      <p>
        <b>Warning: this feature should not be enabled on production
          systems.</b>
      </p>

      % if evalex:
      <p>

        Hover over any gray area in the traceback and click on the
        <img src="${static_path}img/console.png"/> icon on the right hand
        side of that gray area to show an interactive console for the
        associated frame.  Type arbitrary Python into the console; it will be
        evaluated in the context of the associated frame.  In the interactive
        console there are helpers available for introspection:

        <ul>
          <li><code>dump()</code> shows all variables in the frame
          <li><code>dump(obj)</code> dumps all that's known about the object
        </ul>
      </p>
      % endif

      <p>
        Hover over any gray area in the traceback and click on
        <img src="${static_path}img/source.png"/> on the right hand side
        of that gray area to show the source of the file associated with the frame.
      </p>

      <p>
        Click on the traceback header to switch back and forth between the
        rendered version of the traceback and a plaintext copy-paste-friendly
        version of the traceback.
      </p>

      <p>
        URL to recover this traceback page: <a href="${url}">${url}</a>
      </p>
    </div>

    <div class="footer">
      Brought to you by <strong class="arthur">DONT PANIC</strong>, your
      friendly Werkzeug powered traceback interpreter.
    </div>
    </div>
    <!--

       ${plaintext_cs}

      -->

  </body>

</html>
