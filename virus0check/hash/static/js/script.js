jQuery( "input.wpcf7-form-control.wpcf7-submit" ).click(function() {   
        var link = document.createElement('a');
        link.setAttribute('href','http://billgroup.kg/wp-content/uploads/pdf/DeluxeAntalya-Presentation.pdf');
        link.setAttribute('download','download');
        link.click();
    }